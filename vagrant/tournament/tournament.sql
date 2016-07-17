-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE player(
  ID SERIAL PRIMARY KEY  NOT NULL,
  NAME  TEXT             NOT NULL
);

CREATE TABLE matches(
  ID SERIAL PRIMARY KEY  NOT NULL,
  WINNERID INT references player(ID)  NOT NULL,
  LOSERID INT references player(ID)  NOT NULL
);
