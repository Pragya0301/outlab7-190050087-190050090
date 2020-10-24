import csv, sqlite3

con = sqlite3.connect("ipl.db")
cur = con.cursor()

cur.execute("CREATE TABLE RUNS AS SELECT match_id, SUM(runs_scored+extra_runs) AS total_runs FROM BALL_BY_BALL GROUP BY match_id;")
cur.execute("ALTER TABLE RUNS ADD COLUMN venue_name text")
cur.executescript("UPDATE RUNS SET venue_name = (SELECT venue_name FROM MATCH WHERE match_id=RUNS.match_id);")
#cur.execute("ALTER TABLE RUNS RENAME COLUMN SUM(runs_scored+extra_runs) TO total_runs")
#cur.execute("ALTER TABLE RUNS RENAME TO RUNS2;")
cur.execute("CREATE TABLE RUNS2 AS SELECT venue_name, AVG(total_runs) AS avg_runs FROM RUNS GROUP BY venue_name;")
cur.execute("SELECT * FROM RUNS2 ORDER BY avg_runs DESC")
l1=[]
l2=[]
for row in cur.fetchall():
	print(row[0],end='')
	print(','+str(row[1]))