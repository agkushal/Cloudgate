# server/app.py
from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_NAME = 'database.db'

# Create table
def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    source TEXT,
                    event_type TEXT,
                    message TEXT
                )''')
    conn.commit()
    conn.close()

@app.route('/log', methods=['POST'])
def log_event():
    data = request.json
    source = data.get('source', 'unknown')
    event_type = data.get('event_type', 'info')
    message = data.get('message', '')

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, source, event_type, message) VALUES (?, ?, ?, ?)",
              (datetime.now().isoformat(), source, event_type, message))
    conn.commit()
    conn.close()

    return jsonify({"status": "success"})

@app.route('/logs', methods=['GET'])
def get_logs():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY timestamp DESC LIMIT 100")
    logs = c.fetchall()
    conn.close()
    return jsonify(logs)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)
