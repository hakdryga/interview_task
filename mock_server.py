import http.server
import re
import socketserver
from simple_logger import logger


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        regex = "/(people|planets|starships)/[0-9]+"
        result = re.fullmatch(regex, self.path)
        json = '{"name":"Anna Drygalska"}'
        if result:
            identifier = int(self.path.split("/")[-1])
            # l = int(last)
            if identifier <= 100:
                self.send_response(200)
            else:
                self.send_response(404)
                json = f'{{"reason":"Object with id {identifier} not found"}}'
        else:
            # print(f"Wrong path {self.path}")
            json = '{"error":"Invalid Path"}'
        self.send_header("Content-type", "application/json")
        self.end_headers()
        logger.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))

        self.wfile.write(bytes(json, "utf8"))
        return


# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
