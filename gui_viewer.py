# gui_viewer.py
import tkinter as tk
from tkinter import ttk, scrolledtext
import requests

SERVER_URL = "http://localhost:5000/logs"

def fetch_logs():
    try:
        response = requests.get(SERVER_URL)
        logs = response.json()
        log_area.delete("1.0", tk.END)
        for log in logs:
            log_id, timestamp, source, event_type, message = log
            log_entry = f"[{timestamp}] [{source}] [{event_type.upper()}] {message}\n"
            log_area.insert(tk.END, log_entry)
    except Exception as e:
        log_area.insert(tk.END, f"Error fetching logs: {e}\n")

# GUI Setup
root = tk.Tk()
root.title("Cloud Gate Log Viewer")
root.geometry("800x500")

# Heading
title = ttk.Label(root, text="📡 Cloud Gate Logs", font=("Arial", 18))
title.pack(pady=10)

# Button to refresh logs
refresh_btn = ttk.Button(root, text="🔄 Refresh Logs", command=fetch_logs)
refresh_btn.pack(pady=5)

# Scrollable log area
log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 11))
log_area.pack(expand=True, fill='both', padx=10, pady=10)

# Auto-load logs on startup
fetch_logs()

root.mainloop()
