from http.server import BaseHTTPRequestHandler, HTTPServer

class LightControlServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/index.html" or \
                self.path == "/":
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()

            with open("html/index.html", "r") as f:
                self.wfile.write(bytes(f.read(), "utf8"))
            return
        elif self.path == "/bootstrap/css/bootstrap.min.css" or \
                self.path == "/bootstrap/css/bootstrap-theme.min.css":
            self.send_response(200)
            self.send_header("Content-type", "text/css")
            self.end_headers()
            with open("html%s" % self.path, "r") as f:
                self.wfile.write(bytes(f.read(), "utf8"))
            return
        elif self.path == "/jquery.min.js" or \
                self.path == "/bootstrap/js/bootstrap.min.js":
            self.send_response(200)
            self.send_header("Content-type", "text/javascript")
            self.end_headers()
            with open("html%s" % self.path, "r") as f:
                self.wfile.write(bytes(f.read(), "utf8"))
            return
        elif self.path == "/bootstrap/fonts/glyphicons-halflings-regular.woff2":
            self.send_response(200)
            self.send_header("Content-type", "application/x-font-woff")
            self.end_headers()

            with open("html%s" % self.path, "rb") as f:
                self.wfile.write(f.read())
            return
        else:
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes("404", "utf-8"))

def run():
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, LightControlServer)
    httpd.serve_forever()

run()
