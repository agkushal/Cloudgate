# Cloudgate 

It is a simple client–server log monitoring system that collects, stores, and displays system events in real time. It was built as a learning project to understand backend development, APIs, databases, and basic GUI integration.

- REST API to receive log events
- SQLite database for log storage
- Timestamped and categorized logs
- Desktop GUI to view logs in real time
- Manual log refresh support

Technologies Used
- Python
- Flask (backend API)
- SQLite (database)
- Tkinter (GUI)
- Requests (HTTP communication)

Project Structure
- app.py        → Flask server and API endpoints
- SQLite database storing logs
- send_event.py → Client script to send logs
- gui_viewer.py → Tkinter-based log viewer

How It Works
1. The Flask server runs locally and exposes endpoints to receive and fetch logs.
2. Client scripts send log events using HTTP POST requests.
3. Logs are saved in an SQLite database with timestamps.
4. The GUI fetches and displays logs from the server.

How to Run
1. Start the server:
   python app.py

2. Send a test log:
   python send_event.py

3. Open the log viewer:
   python gui_viewer.py

Purpose
This project was created to practice backend development, API design, database handling, and GUI integration in Python.

Notes
- Runs locally on localhost
- Designed for learning and demonstration purposes
- Not intended for production use
