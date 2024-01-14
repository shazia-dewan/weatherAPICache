from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from weatherAPI import weather  # Import the weather dictionary from weatherAPI

class WeatherHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code
        self.send_response(200)

        # Set the content type header
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        # Convert the weather dictionary to JSON and encode it
        weather_json = json.dumps(weather).encode('utf-8')

        # Send the response
        self.wfile.write(weather_json)

def run_server(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, WeatherHandler)

    print(f"Server is running on http://localhost:{port}")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer shutting down.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()

