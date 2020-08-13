from http.server import BaseHTTPRequestHandler
from datetime import datetime

from cowpy import cow


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function! Now Time is it: ' +
                                      str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

        self.wfile.write(message.encode())

        return
