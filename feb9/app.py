import sqlite3 as sql
import pandas as pd

conn = sql.connect('../baseball.db')
cursor = conn.cursor()
query = """
   Select batting.yearid, name,batting.hr
   from batting inner join teams
   on batting.teamid = teams.teamid and batting.yearid = teams.yearid
   where playerID = 'ruthba01'
"""
cursor.execute(query)
records = cursor.fetchall()
records_df = pd.DataFrame(records)
conn.close()

print(records_df)