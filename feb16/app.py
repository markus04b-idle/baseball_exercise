import sqlite3
import pandas as pd
import gradio as gr

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
    WITH top_hitters AS (Select nameFirst,namelast
    from batting Inner JOIN people
    ON batting.playerID = people.playerID
    where teamid = 'PHI' 
    Group by batting.playerID
    order by sum(hr) desc
    limit 10)

    Select Concat(nameFirst,' ',namelast) as player
    from top_hitters
    order by namelast 
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

players = []
for record in records:
    players.append(record[0])

print(players)
