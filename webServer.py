#!/usr/bin/python

# Used to serve a simple HTTP server for Kali Linux unattended installs
# Place the unattended file inside the DIR with this script
# Call the file through your HTTP string

import SimpleHTTPServer
import SocketServer
import os

os.chdir('/bin/pythontools/www')
PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print 'Serving HTTP on port ", PORT,". Terminate with [crtl] + [c].

httpd.serve_forever()
