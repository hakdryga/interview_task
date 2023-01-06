import socketserver
import sys
import getopt
import simple_server

server_ip = ''
server_port = ''

if len(sys.argv) < 5:
    raise Exception('Usage: run_server.py -h [server_ip] -p [server_port] [delay]')

try:
    options, args = getopt.getopt(sys.argv[1:], "h:p:", ["host=", "port="])
except getopt.GetoptError:
    raise Exception('Could not recognise command options')

for name, value in options:
    if name in ['-h', '--host']:
        server_ip = value
    if name in ['-p', '--port']:
        try:
            server_port = int(value)
        except ValueError:
            raise Exception('Server port has to be an integer value')

delay_req = True if 'delay' in args else False

# Create an object of the above class
server_handler = simple_server.MyHttpRequestHandler

socketserver.TCPServer.allow_reuse_address = True
with simple_server.MyTCPServer((server_ip, server_port), server_handler, delay_request=delay_req) as httpd:
    httpd.serve_forever()
