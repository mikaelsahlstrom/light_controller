from http.server import BaseHTTPRequestHandler, HTTPServer
from subprocess import call

requests = {
    "/request.html?do=power": ["KEY_POWER"],
    "/request.html?do=light-up": ["KEY_BRIGHTNESSUP"],
    "/request.html?do=light-down": ["KEY_BRIGHTNESSDOWN"],
    "/request.html?do=speed-up": ["KEY_UP"],
    "/request.html?do=speed-down": ["KEY_DOWN"],
    "/request.html?do=red-1": ["KEY_F1"],
    "/request.html?do=red-2": ["KEY_F2"],
    "/request.html?do=yellow-1": ["KEY_F3"],
    "/request.html?do=yellow-2": ["KEY_F4"],
    "/request.html?do=yellow-3": ["KEY_F5"],
    "/request.html?do=green-1": ["KEY_F6"],
    "/request.html?do=green-2": ["KEY_F7"],
    "/request.html?do=green-3": ["KEY_F8"],
    "/request.html?do=green-4": ["KEY_F9"],
    "/request.html?do=green-5": ["KEY_F10"],
    "/request.html?do=blue-1": ["KEY_F11"],
    "/request.html?do=blue-2": ["KEY_F12"],
    "/request.html?do=blue-3": ["KEY_F13"],
    "/request.html?do=blue-4": ["KEY_F14"],
    "/request.html?do=blue-5": ["KEY_F15"],
    "/request.html?do=white-1": ["KEY_F16"],
    "/request.html?do=white-2": ["KEY_F17"],
    "/request.html?do=white-3": ["KEY_F18"],
    "/request.html?do=white-4": ["KEY_F19"],
    "/request.html?do=white-5": ["KEY_F20"],
    "/request.html?do=jump-3": ["KEY_1"],
    "/request.html?do=jump-7": ["KEY_2"],
    "/request.html?do=fade-3": ["KEY_3"]
}

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
        elif self.path in requests:
            call(["irsend", "SEND_ONCE", "SLINGA"] + requests[self.path])
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes("OK", "utf-8"))
            return
        else:
            self.send_response(404)
            self.send_header("Content-type","text/html")
            self.end_headers()
            self.wfile.write(bytes("404", "utf-8"))
            return

def run():
    server_address = ('127.0.0.1', 80)
    httpd = HTTPServer(server_address, LightControlServer)
    httpd.serve_forever()

run()
