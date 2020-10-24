import csv, sqlite3

con = sqlite3.connect("ipl.db")
cur = con.cursor()
cur.execute("CREATE TABLE TEAM (team_id INT,team_name TEXT, PRIMARY KEY(team_id, team_name));")


cur = con.cursor()
cur.execute("CREATE TABLE PLAYER (player_id INT, player_name TEXT, dob TIMESTAMP,batting_hand TEXT,bowling_skill TEXT,country_name TEXT, PRIMARY KEY(player_id));")

cur = con.cursor()
cur.execute("CREATE TABLE MATCH (match_id INT,season_year INT,team1 INT ,team2 INT,battedfirst INT,battedsecond INT,venue_name TEXT,city_name TEXT,country_name TEXT,toss_winner INT,match_winner TEXT,toss_name TEXT,win_type TEXT,man_of_match INT,win_margin INT, PRIMARY KEY(match_id));")

cur = con.cursor()
cur.execute("CREATE TABLE PLAYER_MATCH (playermatch_key INT,match_id INT,player_id INT,batting_hand TEXT,bowling_skill TEXT,role_desc TEXT,team_id INT, FOREIGN KEY (match_id) REFERENCES MATCH (match_id), FOREIGN KEY (player_id) REFERENCES PLAYER (player_id), FOREIGN KEY (batting_hand) REFERENCES MATCH (batting_hand), FOREIGN KEY (bowling_skill) REFERENCES MATCH (bowling_skill), FOREIGN KEY (team_id) REFERENCES TEAM (team_id));")

cur = con.cursor()
cur.execute("CREATE TABLE BALL_BY_BALL (match_id INT,innings_no INT,over_id INT,ball_id INT,striker_batting_position INT,runs_scored INT,extra_runs INT,out_type TEXT,striker INT,non_striker INT,bowler INT, FOREIGN KEY (match_id) REFERENCES MATCH (match_id));")