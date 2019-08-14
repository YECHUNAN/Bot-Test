from http.server import HTTPServer, BaseHTTPRequestHandler

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'hello get')
    
    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'hello post')

httpd = HTTPServer(('localhost', 8000), MyHandler)

httpd.serve_forever()