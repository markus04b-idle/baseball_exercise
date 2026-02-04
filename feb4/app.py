import sqlite3
import pandas as pd

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """ 
    SELECT yearID,sum(HR) as totalHR
    from Batting
    where teamID = 'PHI'
    Group by yearID 
    order by yearID desc
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns=['yearID', 'totalHR'])

print(records_df)