import http.server
import socketserver


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/people/':
            self.send_response(200)
        if self.path == '/planets/':
            self.send_response(400)

        self.send_header("Content-type", "application/json")
        self.end_headers()
        json = '{"name":"dryga"}'
        self.wfile.write(bytes(json, "utf8"))
        return
        # return http.server.SimpleHTTPRequestHandler.do_GET(self)


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
