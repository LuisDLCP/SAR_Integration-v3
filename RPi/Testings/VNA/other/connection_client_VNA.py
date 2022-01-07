"""
Connection between a client and VNA's program
VNA_IP: local host, 127.0.0.1
VNA_PORT: 5025
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',5025)) # server_ip, server_port
s.sendall(b"disp:spl 3\n") #(b"*disp:col:back 10,10,10\n")#(b"*IDN?\n")
data=s.recv(1024)
print("Received ",repr(data))
