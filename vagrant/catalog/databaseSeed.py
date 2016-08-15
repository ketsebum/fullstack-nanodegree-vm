from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Category, Base, CatalogItem, User

engine = create_engine('sqlite:///catalogitems.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Sean Nunley", email="snunleys@gmail.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Categories
category1 = Category(user_id=1, name="Burger")
session.add(category1)
session.commit()

category2 = Category(user_id=1, name="Fries")
session.add(category2)
session.commit()

category3 = Category(user_id=1, name="Beverages")
session.add(category3)
session.commit()

category4 = Category(user_id=1, name="Asian")
session.add(category4)
session.commit()

category5 = Category(user_id=1, name="Indian")
session.add(category5)
session.commit()

category6 = Category(user_id=1, name="Dessert")
session.add(category6)
session.commit()

category7 = Category(user_id=1, name="Other")
session.add(category7)
session.commit()

# Catalog Items
catalogItem1 = CatalogItem(user_id=1, name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     category=category1)
session.add(catalogItem1)
session.commit()


catalogItem2 = CatalogItem(user_id=1, name="French Fries", description="with garlic and parmesan",
                     category=category2)
session.add(catalogItem2)
session.commit()

catalogItem3 = CatalogItem(user_id=1, name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                     category=category1)
session.add(catalogItem3)
session.commit()

catalogItem4 = CatalogItem(user_id=1, name="Sirloin Burger", description="Made with grade A beef",
                     category=category1)
session.add(catalogItem4)
session.commit()

catalogItem5 = CatalogItem(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                     category=category3)

session.add(catalogItem5)
session.commit()

catalogItem6 = CatalogItem(user_id=1, name="Iced Tea", description="with Lemon",
                     category=category3)

session.add(catalogItem6)
session.commit()

catalogItem7 = CatalogItem(user_id=1, name="Grilled Cheese Sandwich",
                     description="On texas toast with American Cheese", category=category7)

session.add(catalogItem7)
session.commit()

catalogItem8 = CatalogItem(user_id=1, name="Vegentarian Burger", description="Made with freshest of ingredients and home grown spices",
                     category=category1)

session.add(catalogItem8)
session.commit()

catalogItem9 = CatalogItem(user_id=1, name="Chicken Stir Fry", description="With your choice of noodles vegetables and sauces",
                     category=category4)

session.add(catalogItem9)
session.commit()

catalogItem10 = CatalogItem(user_id=1, name="Peking Duck",
                     description=" A famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", category=category4)

session.add(catalogItem10)
session.commit()

catalogItem11 = CatalogItem(user_id=1, name="Spicy Tuna Roll", description="Seared rare ahi, avocado, edamame, cucumber with wasabi soy sauce ",
                     category=category4)

session.add(catalogItem11)
session.commit()

catalogItem12 = CatalogItem(user_id=1, name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     category=category4)

session.add(catalogItem12)
session.commit()

catalogItem13 = CatalogItem(user_id=1, name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     category=category4)

session.add(catalogItem13)
session.commit()

catalogItem14 = CatalogItem(user_id=1, name="Ramen", description="a Japanese noodle soup dish. It consists of Chinese-style wheat noodles served in a meat- or (occasionally) fish-based broth, often flavored with soy sauce or miso, and uses toppings such as sliced pork, dried seaweed, kamaboko, and green onions.",
                     category=category4)

session.add(catalogItem14)
session.commit()

catalogItem15 = CatalogItem(user_id=1, name="Pho", description="a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.",
                     category=category4)

session.add(catalogItem15)
session.commit()

catalogItem16 = CatalogItem(user_id=1, name="Chinese Dumplings", description="a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.",
                     category=category4)

session.add(catalogItem16)
session.commit()

catalogItem17 = CatalogItem(user_id=1, name="Gyoza", description="light seasoning of Japanese gyoza with salt and soy sauce, and in a thin gyoza wrapper",
                     category=category4)

session.add(catalogItem17)
session.commit()

catalogItem18 = CatalogItem(user_id=1, name="Stinky Tofu", description="Taiwanese dish, deep fried fermented tofu served with pickled cabbage.",
                     category=category4)

session.add(catalogItem18)
session.commit()

catalogItem19 = CatalogItem(user_id=1, name="No Meat Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                     category=category1)

session.add(catalogItem19)
session.commit()


catalogItem20 = CatalogItem(user_id=1, name="Tres Leches Cake", description="Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.",
                     category=category6)

session.add(catalogItem20)
session.commit()

catalogItem21 = CatalogItem(user_id=1, name="Honey Boba Shaved Snow",
                     description="Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi",
                     category=category6)

session.add(catalogItem21)
session.commit()

catalogItem22 = CatalogItem(user_id=1, name="Chicken and Rice", description="Chicken... and rice",
                     category=category4)

session.add(catalogItem22)
session.commit()

catalogItem23 = CatalogItem(user_id=1, name="Choc Full O\' Mint (Smitten\'s Fresh Mint Chip ice cream)",
                     description="Milk, cream, salt, ..., Liquid nitrogen magic",
                     category=category6)

session.add(catalogItem23)
session.commit()

catalogItem24 = CatalogItem(user_id=1, name="Tonkatsu Ramen", description="Noodles in a delicious pork-based broth with a soft-boiled egg",
                     category=category4)

session.add(catalogItem24)
session.commit()


catalogItem25 = CatalogItem(user_id=1, name="Lamb Curry", description="Slow cook that thang in a pool of tomatoes, onions and alllll those tasty Indian spices. Mmmm.",
                     category=category5)

session.add(catalogItem25)
session.commit()

catalogItem26 = CatalogItem(user_id=1, name="Chicken Masala", description="Chicken cooked in Masala wine sauce with mushrooms",
                     category=category5)
session.add(catalogItem26)
session.commit()

catalogItem27 = CatalogItem(user_id=1, name="Potstickers", description="Delicious chicken and veggies encapsulated in fried dough.",
                     category=category4)
session.add(catalogItem27)
session.commit()

catalogItem28 = CatalogItem(user_id=1, name="Nigiri Sampler", description="Maguro, Sake, Hamachi, Unagi, Uni, TORO!",
                     category=category4)
session.add(catalogItem28)
session.commit()

catalogItem29 = CatalogItem(user_id=1, name="Tikka Masala", description="Tasty",
                     category=category5)
session.add(catalogItem29)
session.commit()

catalogItem30 = CatalogItem(user_id=1, name="Chicken Fried Steak",
                     description="Fresh battered sirloin steak fried and smothered with cream gravy",
                     category=category7)
session.add(catalogItem30)
session.commit()


print "Added the database"
