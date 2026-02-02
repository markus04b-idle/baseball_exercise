import sqlite3
import gradio as gr

def fetch_phillies():
    conn = sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT PlayerID
        FROM batting
        WHERE YearID = 1976 and TeamID = 'PHI'
    """
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    players = []
    for record in records:
        players.append(record[0])
    return players

def f(player):
    conn =sqlite3.connect('../baseball.db')
    cursor = conn.cursor()
    query = """
        SELECT HR
        from batting
        WHERE playerID = ? and yearID = 1976 and TeamID = 'PHI'
    """
    cursor.execute(query,[player])
    records = cursor.fetchall()
    return records[0][0]

with gr.Blocks() as iface:
    playerID = gr.Dropdown(choices = fetch_phillies(), interactive = True, label = "Select a Phillies Player from 1976")
    hr_output = gr.Number(label = "Number of Home Runs in 1976")
    playerID.change(fn = f, inputs = [playerID], outputs = [hr_output])

iface.launch()


