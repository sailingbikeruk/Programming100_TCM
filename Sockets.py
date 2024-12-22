# Sockets - used tp connect two nodes together

import socket
HOST = '127.0.0.1' 
PORT = 7777
HOSTPORT = ('127.0.0.1',7777) # this sets a tuple with the values

# AF_INET = IPv4
# SOCK_STREAM is a port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# This AF_INET to the value of HOST and SOCK_STREAM to ther value of PORT

s.connect((HOST,PORT)) # this creates a tuple from the two variables and passes it to s.connect
s.connect(HOSTPORT) # this uses the predefined tuple (line 6) and passes it to s.connect