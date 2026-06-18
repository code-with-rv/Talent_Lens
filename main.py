import http.server
import socketserver
import webbrowser
import threading
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def open_browser():
    print(f"Opening browser at http://localhost:{PORT}...")
    webbrowser.open(f"http://localhost:{PORT}")

def run_server():
    # Allow port reuse to avoid 'Address already in use' errors
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("\n" + "=" * 50)
            print(f"  TalentLens Local Dev Server started!")
            print(f"  Serving files from: {DIRECTORY}")
            print(f"  URL: http://localhost:{PORT}")
            print("=" * 50 + "\n")
            print("Press Ctrl+C in your terminal to stop the server.")
            
            # Start timer to open browser once server is initialized
            threading.Timer(0.8, open_browser).start()
            
            httpd.serve_forever()
    except Exception as e:
        print(f"Error starting server: {e}", file=sys.stderr)
        print("Make sure port 8000 is not already in use by another program.", file=sys.stderr)

if __name__ == "__main__":
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nTalentLens server stopped successfully. Goodbye!")
