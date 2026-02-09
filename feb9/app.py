import sqlite3 as sql
import pandas as pd

conn = sql.connect('../baseball.db')
cursor = conn.cursor()
query = """
   select teamid, sum(hr) as seasonHR
   from batting
   where year_id = 2025
   group by teamid
   Having seasonHR >= 200
"""
cursor.execute(query)
records = cursor.fetchall()
records_df = pd.DataFrame(records, columns=['team', 'home_runs'])
conn.close()

print(records_df)