import urllib.parse as urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

from lpfClientServer.lpf import largest_prime_factor


class SimpleServer(BaseHTTPRequestHandler):
    def set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.set_response()
        parsed_url = urlparse.urlparse(self.path)

        if 'number' in parse_qs(parsed_url.query):
            parsed_arg = (parse_qs(parsed_url.query)['number'])[0]
            lpf = largest_prime_factor(int(parsed_arg))
            output = str(lpf)
            self.wfile.write(output.encode())
            print('largest prime factor for %s is %s' % (parsed_arg, output))
        else:
            self.send_response(400)
            self.wfile.write('Bad request :('.encode())


if __name__ == '__main__':
    host = ''
    port = 8000
    print('Server is running on 127.0.0.1:' + str(port))
    HTTPServer((host, port), SimpleServer).serve_forever()
