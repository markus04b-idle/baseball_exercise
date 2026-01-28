import sqlite3
import pandas as pd

conn = sqlite3.connect('baseball.db')
cursor = conn.cursor()

query = """
    SELECT PlayerID, YearID, TeamID, HR
    FROM batting
    WHERE YearID = 1976 and TeamID = 'PHI' and HR != 0
    ORDER BY HR DESC
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records, columns=['PlayerID', 'YearID', 'TeamID', 'HR'])
print(records_df)