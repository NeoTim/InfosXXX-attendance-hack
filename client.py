#!/usr/bin/env python

import socket
import sys

host = sys.argv[1]  # server address
port = int(sys.argv[2])  # server port

i = 0
filer = open("data.txt")
lines = 0

while(1):

    # create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    record = filer.readline()
    if record == "":
        break
    lines += 1
    print 'real:', record,

    # connect to server
    s.connect((host, port))
    s.send(record)  # send test string
    data = s.recv(80)  # read up to 80 bytes

    print 'recv:', data,
    if not data: # if end of data, leave loop
        break
    print 'received', len(data), 'bytes\n'
    s.close()

# close the connection
print '\nFinished Total Records :: ', lines
