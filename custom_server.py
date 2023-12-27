# custom_server.py
import http.server
import socketserver

# Define the port you want to use (e.g., 8000)
PORT = 8000


# Create a custom request handler to serve files
class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Customize the behavior for specific paths
        if self.path == "/":
            # Serve the index.html file
            self.path = "index.html"
        elif self.path == "/main.js":
            # Serve the main.js file
            self.path = "main.js"
        elif self.path == "/WindowManager.js":
            # Serve the WindowManager.js file
            self.path = "WindowManager.js"

        # Call the base class implementation to serve the file
        super().do_GET()


# Set up the server with your custom handler
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving HTTP on port {PORT}...")
    httpd.serve_forever()
