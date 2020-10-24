import csv, sqlite3

con = sqlite3.connect("ipl.db")
cur = con.cursor()

cur.execute("CREATE TABLE PLAYER_RUNS AS SELECT striker, SUM(runs_scored) AS runs FROM BALL_BY_BALL GROUP BY striker;")

cur.execute("ALTER TABLE PLAYER_RUNS ADD COLUMN player_name text")
cur.executescript("UPDATE PLAYER_RUNS SET player_name = (SELECT player_name FROM PLAYER WHERE player_id=PLAYER_RUNS.striker);")
cur.execute("SELECT * FROM PLAYER_RUNS ORDER BY runs DESC;")

i=0
for row in cur.fetchall():
	if i==20:
		break
	print(row[0],end='')
	print(','+row[2],end='')
	print(','+str(row[1]))
	i=i+1