#!/usr/local/bin/python3

print("Content-Type:text/html\r\n\r\n")

import sys

try:
    import cgi
    import server.securityServer


    inputs = cgi.FieldStorage()
    request = {}

    for key in inputs.keys():
        request[key] = inputs[key].value

    result = server.securityServer.handleRequest(request)
    print(result)

except:
    print(sys.exc_info()[0])