import sqlite3
import pandas as pd
import gradio as gr

conn = sqlite3.connect('../baseball.db')
cursor = conn.cursor()
query = """
WITH top_hitters AS (Select nameFirst,namelast,batting.playerid
from batting Inner JOIN people
ON batting.playerID = people.playerID
where teamid = 'PHI' 
Group by batting.playerID
order by sum(hr) desc
limit 10)

Select Concat(nameFirst,' ',namelast) as player,playerid
from top_hitters
order by namelast 
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

def f(playerID):
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
    SELECT CAST(yearID AS TEXT),HR
    from batting
    where teamid = 'PHI' and playerID = ?
    """
    cursor.execute(query, [playerID])
    records = cursor.fetchall()
    conn.close()
    df = pd.DataFrame(records, columns = ['year', 'home runs'])
    return df

with gr.Blocks() as iface:
    player_dd = gr.Dropdown(records,interactive = True)
    plot = gr.LinePlot(x = "year", y = "home runs")
    player_dd.change(fn = f, inputs = [player_dd], outputs = [plot])

iface.launch()