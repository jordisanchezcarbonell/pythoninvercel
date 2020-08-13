from http.server import BaseHTTPRequestHandler
from datetime import datetime

from cowpy import cow


class Contador(object):

    def __init__(self, inicial=0):
        self.numero = inicial

    def siguiente(self):
        self.numero += 1
        return self.numero


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        cuenta = Contador()

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = cow.Cowacter().milk('Hello from Python from a Serverless Function! Now Time is it: ' +
                                      str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+cuenta)

        self.wfile.write(
            bytes("<html><head><title>Title goes here.</title></head>/html>", "utf-8"))

        self.wfile.write(message.encode())
        cuenta.siguiente()
        return
