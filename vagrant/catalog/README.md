# Udacity Project: Item Catalog
This project implements the Udacity Project Item Catalog

## /templates

Here is all of the HTML that is used. Most items are named after their intended use. For instance, edititem.html allows the user to edit the item. The use of a header file and main file for some general templating was used.

## /static

Here is where the CSS & JS files are located. Index.js has the primary javascript which deals with setting up buttons on the page. There is very minimal css in the dashboard.css as well to help with minor formatting.

Also included is some third party vendor libraries such as angular, bootstrap, and jquery.

##database_setup.py

Is used for database creation. There are a total of 3 tables created Users, CatalogItem, and Category. These are declared with sqlalchemy which allows them to be referenced easily from python.

##tournament_test.py

- Validates the project

##To run the program
Please run the tournament_test.py file to see the results. This should printout the following into your terminal:
```text
1. countPlayers() returns 0 after initial deletePlayers() execution.
2. countPlayers() returns 1 after one player is registered.
3. countPlayers() returns 2 after two players are registered.
4. countPlayers() returns zero after registered players are deleted.
5. Player records successfully deleted.
6. Newly registered players appear in the standings with no matches.
7. After a match, players have updated standings.
8. After match deletion, player standings are properly reset.
9. Matches are properly deleted.
10. After one match, players with one win are properly paired.
Success!  All tests pass!
```
