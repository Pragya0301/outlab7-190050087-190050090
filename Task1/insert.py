import csv, sqlite3
import itertools

con = sqlite3.connect("ipl.db")
cur = con.cursor()

with open('team.csv','r') as fin:
    dr = csv.DictReader(fin)
    #next(dr)
    #print(dr)
    to_db = [(i['team_id'], i['team_name']) for i in dr]

cur.executemany("INSERT INTO TEAM (team_id,team_name) VALUES (?, ?);", to_db)
con.commit()
con.close()

con = sqlite3.connect("ipl.db")
cur = con.cursor()
with open('player.csv','r') as fin:
    dr = csv.DictReader(fin)
    #next(dr)
    to_db = [(i['player_id'], i['player_name'], i['dob'], i['batting_hand'], i['bowling_skill'], i['country_name'], ) for i in dr]

cur.executemany("INSERT INTO PLAYER (player_id,player_name,dob,batting_hand,bowling_skill,country_name) VALUES (?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

con = sqlite3.connect("ipl.db")
cur = con.cursor()
with open('match.csv','r') as fin:
    dr = csv.DictReader(fin)
    #next(dr)
    to_db = [(i['match_id'], i['season_year'], i['team1'], i['team2'], i['battedfirst'], i['battedsecond'], i['venue_name'], i['city_name'], i['country_name'], i['toss_winner'], i['match_winner'], i['toss_name'], i['win_type'], i['man_of_match'], i['win_margin']) for i in dr]

cur.executemany("INSERT INTO MATCH (match_id,season_year,team1,team2,battedfirst,battedsecond,venue_name,city_name,country_name,toss_winner,match_winner,toss_name,win_type,man_of_match,win_margin) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

con = sqlite3.connect("ipl.db")
cur = con.cursor()
with open('player_match.csv','r') as fin:
    dr = csv.DictReader(fin)
    #next(dr)
    to_db = [(i['playermatch_key'], i['match_id'], i['player_id'], i['batting_hand'], i['bowling_skill'], i['role_desc'], i['team_id']) for i in dr]

cur.executemany("INSERT INTO PLAYER_MATCH (playermatch_key,match_id,player_id,batting_hand,bowling_skill,role_desc,team_id) VALUES (?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()

con = sqlite3.connect("ipl.db")
cur = con.cursor()
with open('ball_by_ball.csv','r') as fin:
    dr = csv.DictReader(fin)
    #next(dr)
    to_db = [(i['match_id'], i['innings_no'], i['over_id'], i['ball_id'], i['striker_batting_position'], i['runs_scored'], i['extra_runs'], i['out_type'], i['striker'], i['non_striker'], i['bowler']) for i in dr]

cur.executemany("INSERT INTO BALL_BY_BALL (match_id,innings_no,over_id,ball_id,striker_batting_position,runs_scored,extra_runs,out_type,striker,non_striker,bowler) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()