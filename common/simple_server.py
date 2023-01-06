import http.server
import socketserver
import re
import logging
import time
import random


class MyTCPServer(socketserver.TCPServer):

    def __init__(self, server_address, RequestHandlerClass, delay_request=False):
        super(MyTCPServer, self).__init__(server_address, RequestHandlerClass)

        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
        log_file_handler = logging.FileHandler('server_log.txt')
        log_file_handler.setLevel(logging.DEBUG)
        log_file_handler.setFormatter(formatter)
        self.logger.addHandler(log_file_handler)

        self.delay_request = delay_request


class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self) -> None:
        regex = "/(people|planets|starships)/[0-9]+"
        result = re.fullmatch(regex, self.path)
        json = '{"name":"Anna Drygalska"}'
        if result:
            identifier = int(self.path.split("/")[-1])
            if 0 < identifier <= 100:
                self.send_response(200)
            else:
                self.send_response(404)
                json = f'{{"reason":"Object with id {identifier} not found"}}'
        else:
            self.send_response(400)
            json = '{"error":"Invalid Path"}'
        self.send_header("Content-type", "application/json")
        self.end_headers()

        self.wfile.write(bytes(json, "utf8"))

        if self.server.delay_request:
            time.sleep(random.random())

    def log_request(self, code: int | str = ..., size: int | str = ...) -> None:
        self.log_message('Method: %s\nPath: %s\nHeaders:\n%s\nResponse code: %s\n', self.command, self.path, self.headers, code)

    def log_message(self, format: str, *args) -> None:
        self.server.logger.info("%s - - %s\n", self.address_string(), format % args)