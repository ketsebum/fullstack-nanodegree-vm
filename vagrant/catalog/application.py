from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem, User

from flask import session as login_session
import random, string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Restaurant Menu Application"

engine = create_engine('sqlite:///catalogitems.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route("/")
def showIndex():
    categories = session.query(Category).all()
    items = session.query(CatalogItem).all()
    if 'username' not in login_session:
      return render_template('index.html', categories=categories, items=items)
    user = getUserInfo(getUserID(login_session.get('email')))
    return render_template('index.html', categories=categories, items=items, user=user, username=login_session.get('username'))

@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)

@app.route('/additem', methods=['GET','POST'])
def showAddItem():
    if 'username' not in login_session:
      return redirect('/login')
    categories = session.query(Category).all()
    if request.method == 'GET':
        return render_template('additem.html', categories=categories, username=login_session['username'])
    if request.method == 'POST':
        category = session.query(Category).filter_by(name=request.form['category']).one()
        user = session.query(User).filter_by(id=login_session.get("user_id")).one()
        catalogItem = CatalogItem(name=request.form['title'], description=request.form['description'],
         category=category, user=user)
        session.add(catalogItem)
        session.commit()
        return "Success!"

@app.route('/success')
def showSuccess():
    if 'username' not in login_session:
      return redirect('/login')
    return render_template('success.html', username=login_session['username'])

@app.route("/category/<int:category_id>/")
def showCategoryItems(category_id):
    categories = session.query(Category).all()
    items = session.query(CatalogItem).filter_by(category_id=category_id).all()
    category = session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
      return render_template('category.html', categories=categories, items=items, category=category)
    user = getUserInfo(getUserID(login_session.get('email')))
    return render_template('category.html', categories=categories, items=items, user=user, username=login_session.get('username'), category=category)


@app.route("/catalogItem/<int:catalog_id>/")
def showItemDetails(catalog_id):
    catalogItem = session.query(CatalogItem).filter_by(id=catalog_id).one()
    categories = session.query(Category).all()
    if 'email' in login_session:
        user = getUserInfo(getUserID(login_session.get('email')))
        return render_template('itemdetails.html', item=catalogItem, user=user, categories=categories, username=login_session.get('username'))
    return render_template('itemdetails.html', item=catalogItem, categories=categories)

@app.route("/editItem/<int:catalog_id>/", methods=['GET','POST'])
def editCatalogItem(catalog_id):
    if 'username' not in login_session:
        return redirect('/login')
    catalogItem = session.query(CatalogItem).filter_by(id=catalog_id).one()
    user = getUserInfo(getUserID(login_session.get('email')))
    if catalogItem.user_id != user.id:
        return redirect('/')
    categories = session.query(Category).all()
    if request.method == 'GET':
        return render_template('edititem.html', item=catalogItem, categories=categories, username=login_session.get('username'))
    if request.method == 'POST':
        catalogItem.name = request.form['title']
        catalogItem.description = request.form['description']
        category = session.query(Category).filter_by(name=request.form['category']).one()
        catalogItem.category = category
        session.commit()
        print "yes"
        return "WOA!"

@app.route("/catalogItem/<int:catalog_id>/delete", methods=['GET','DELETE'])
def deleteCatalogItem(catalog_id):
    if 'username' not in login_session:
        return "Not Logged In"
    catalogItem = session.query(CatalogItem).filter_by(id=catalog_id).one()
    user = getUserInfo(getUserID(login_session.get('email')))
    if catalogItem.user_id != user.id:
        return "Not Able to Delete"
    if request.method == 'GET':
        return render_template('delete.html', item=catalogItem, username=login_session.get('username'))
    if request.method == 'DELETE':
        session.delete(catalogItem)
        session.commit()
        return "Success"

@app.route("/catalog.json")
def catalogJson():
    catalog = session.query(CatalogItem).all()
    return jsonify(CatalogItems=[i.serialize for i in catalog])

# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user

def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data
    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already connected.'),
                                 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = 'success'
    return output

@app.route('/gdisconnect')
def gdisconnect():
    print login_session
    credentials = login_session.get('credentials')
    if credentials is None:
 	print 'Access Token is None'
        response = make_response(
            json.dumps('User was not logged in.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
    	# return render_template('logout.html')

    access_token = credentials.access_token
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
	del login_session['credentials']
    	del login_session['gplus_id']
    	del login_session['username']
    	del login_session['email']
    	del login_session['picture']
        del login_session['user_id']
    	return render_template('logout.html')
    else:
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
    	# return render_template('logout.html')

if __name__ == "__main__":
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
