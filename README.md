# UdacityProject2
This code was developed for the completion of the first project in Udacities Nano Degree program for Project 2.

The premise of this project, is to create simple python code that utilizes a database to regulate a tournament through the registration of players, reporting of matches, and finding the next match using Swiss pairing method.

The primary code is located in the vagrant/tournament subdirectory in this project.

##tournament.sql

The tournament.sql has the table definitions used to solve this project. There are two tables created:
- player
  - ID - Primary Key Serial Integer
  - Name - TEXT
- matches
  - ID - Primary Key Serial Integer
  - WINNERID - Foreign key into player table
  - LOSERID - Foreign key into player table

##tournament.py

tournament.py handles all of the interactions with the database, in several simple functions. The following functions are defined in the tournament.py:
- connect()
  - Creates a connection with the PostgreSQL Database
- deleteMatches()
  - Deletes all matches in database
- deletePlayers()
  - Deletes all players in database
- countPlayers()
  - Counts all players in database
- registerPlayer(name)
  - Registers a player in database
- playerStandings()
  - Reports the current players standings in a tuple, ordered by their current wins
- reportMatch(winner, loser)
  - Registers the winner & loser for match and stores in the database
- swissPairings()
  - Reports a set of tuples for the next matchup according to swiss pairing rules

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
