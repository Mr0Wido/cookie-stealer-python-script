#!/usr/bin/env python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from datetime import datetime


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print(f"\n{datetime.now().strftime('%Y-%m-%d %I:%M %p')} - {self.client_address[0]}\n{self.headers['user-agent']}\n{'-'*50}")

        # Print all headers.
        for header, value in self.headers.items():
            print(f"{header}: {value}")

        # Print the query string parameters.
        query_components = parse_qs(urlparse(self.path).query)
        for k, v in query_components.items():
            print(f"{k.strip()}: {v}")

        return


    def log_message(self, format, *args):
        return


if __name__ == "__main__":
    try:
        server = HTTPServer(('0.0.0.0', 4444), MyHandler)
        print('Started HTTP Server!')
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutting Down Server')
        server.socket.close()
