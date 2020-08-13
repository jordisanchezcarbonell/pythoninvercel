from http.server import BaseHTTPRequestHandler
from datetime import datetime

from cowpy import cow


class handler(BaseHTTPRequestHandler):


NUMBER = 5


def do_GET(self):

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    message = cow.Cowacter().milk('Hello from Python from a Serverless Function! Now Time is it: ' +
                                  str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+' ESTO FUNCIONA : '+str(NUMBER))

    self.wfile.write(
        bytes("<html><head><title>Title goes here.</title></head>/html>", "utf-8"))

    self.wfile.write(message.encode())

    NUMBER += 1

    TEST = cow.Cowacter().milk('Hello from Python from a Serverless Function! Now Time is it: ' +
                               str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+' ESTO FUNCIONA : '+str(NUMBER))

    self.wfile.write(TEST.encode())
    return
