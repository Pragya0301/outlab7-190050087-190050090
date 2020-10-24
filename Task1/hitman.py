import csv, sqlite3

con = sqlite3.connect("ipl.db")
cur = con.cursor()

cur.execute("CREATE TABLE HITMAN1 AS SELECT striker, runs_scored FROM BALL_BY_BALL;")
cur.execute("ALTER TABLE HITMAN1 ADD COLUMN player_name text")
cur.executescript("UPDATE HITMAN1 SET player_name = (SELECT player_name FROM PLAYER WHERE player_id=HITMAN1.striker);")
cur.execute("CREATE TABLE HITMAN2 AS SELECT striker, sixes FROM HITMAN1 WHERE HITMAN1.runs_scored=6;")
cur.execute("ALTER TABLE HITMAN2 ADD COLUMN player_name text")
cur.executescript("UPDATE HITMAN2 SET player_name = (SELECT player_name FROM PLAYER WHERE player_id=HITMAN2.striker);")

cur.execute("CREATE TABLE HITMAN3 AS SELECT striker,player_name, COUNT(striker) AS num_appear FROM HITMAN1 GROUP BY striker;")

cur.execute("ALTER TABLE HITMAN3 ADD COLUMN num_sixes INT")
cur.executescript("UPDATE HITMAN3 SET num_sixes = (SELECT COUNT(striker) FROM HITMAN2 WHERE striker=HITMAN3.striker);")

cur.execute("ALTER TABLE HITMAN3 ADD COLUMN sixes_rate INT")
cur.executescript("UPDATE HITMAN3 SET sixes_rate = (SELECT 1.0*num_sixes/num_appear FROM HITMAN3 WHERE striker=HITMAN3.striker);")
cur.execute("SELECT * FROM HITMAN3 ORDER BY sixes_rate DESC")

for row in cur.fetchall():
	print(row[0],end='')
	print(','+row[1],end='')
	print(','+row[3],end='')
	print(','+row[2],end='')
	print(','+row[4],end='')