#!/usr/bin/env python
"""
Simple launcher script to run both frontend and backend servers.
The frontend will be served on port 8000 and backend on port 5000.
"""

import os
import subprocess
import webbrowser
import time

def start_servers():
    """Start Flask backend and HTTP frontend server."""

    print("🚀 Starting Baby Birth Weight Predictor...")
    print()

    # Start Flask backend on port 5000
    print("📦 Starting Flask backend server on http://localhost:5000...")
    flask_process = subprocess.Popen(['python', 'app.py'])

    time.sleep(2)  # Give Flask time to start

    # Start HTTP server on port 8000 in a new process
    print("🌐 Starting frontend server on http://localhost:8000...")
    http_process = subprocess.Popen(['python', '-m', 'http.server', '8000'])

    time.sleep(1)

    print()
    print("✅ Servers started successfully!")
    print()
    print("📍 Frontend: http://localhost:8000")
    print("📍 Backend:  http://localhost:5000")
    print()
    print("Opening frontend in browser...")

    # Open in default browser
    try:
        webbrowser.open('http://localhost:8000/index.html')
    except:
        print("Could not open browser automatically. Please visit http://localhost:8000/index.html")

    print()
    print("Press Ctrl+C to stop both servers...")
    print()

    try:
        # Keep both processes running
        flask_process.wait()
    except KeyboardInterrupt:
        print("\n\n🛑 Stopping servers...")
        flask_process.terminate()
        http_process.terminate()
        print("✅ Servers stopped.")

if __name__ == "__main__":
    start_servers()
