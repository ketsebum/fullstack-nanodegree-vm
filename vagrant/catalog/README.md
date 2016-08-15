# Udacity Project: Item Catalog
This project implements the Udacity Project Item Catalog. Running the application.py creates a webserver located at http://localhost:5000/, that hosts a catalog that uses security credentials from Google OAuth2 to give access.

## /templates

Here is all of the HTML that is used. Most items are named after their intended use. For instance, edititem.html allows the user to edit the item. The use of a header file and main file for some general templating was used.

## /static

Here is where the CSS & JS files are located. Index.js has the primary javascript which deals with setting up buttons on the page. There is very minimal css in the dashboard.css as well to help with minor formatting.

Also included is some third party vendor libraries such as angular, bootstrap, and jquery.

## Database Setup

In order to create the database run the following commands:
```
python database_setup.py
python databaseSeed.py
```
database_setup.py does the work of creating 3 tables and classes Users, CatalogItem, and Category. These are declared with sqlalchemy which allows them to be referenced easily from python.

databaseSeed.py does the work of seeding the tables with data.

##application.py

Here is a list of endpoints configured in python.
http://localhost:5000/

http://localhost:5000/login

http://localhost:5000/additem

http://localhost:5000/success

http://localhost:5000/category/<int:category_id>/

http://localhost:5000/catalogItem/<int:catalog_id>/

http://localhost:5000/editItem/<int:catalog_id>/

http://localhost:5000/catalogItem/<int:catalog_id>/delete

http://localhost:5000/catalog.json

http://localhost:5000/gconnect

http://localhost:5000/gdisconnect

- / base page
- /login the login page for the application
- /additem the add item page and where to post to create new items in the database
- /success is the successful page sent after deleting an item
- /category/<int:category_id>/ is used to display a category list of items
- /catalogItem/<int:catalog_id>/ is used to show the item details for a specific catalog item
- /editItem/<int:catalog_id>/ is used to edit the item details for a specific catalog item
- /catalogItem/<int:catalog_id>/delete is used to delete a specific catalog item
- /catalog.json gives a json of the catalog
- /gconnect uses Google OAuth2 provider to give access to the application
- /gdisconnect disconnects from Google OAuth2

##To run the program
Please run the application.py file to see the results. Then proceed to http://localhost:5000/ and see the list. Go to http://localhost:5000/login to login and make adjustments to the list
