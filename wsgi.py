import SimpleHTTPServer
import SocketServer

PORT = 8443

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("https://192.168.99.100", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()