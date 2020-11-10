#!/usr/bin/python

import socket
import sys

if len(sys.argv) !=2:
    print "Usage: smtpverifier.py <username>"
    sys.exit(0)

#Create a Socket and connect to the Server

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect (('!!!IP ADRESS HERE!!!',25))

# Receive the banner

banner = s.recv(1024)
print banner

#Verify a user
s.send('VRFY ' + sys.argv[1] + '\r\n')
result = s.recv(1024)
print result

#Close socket
s.close()
