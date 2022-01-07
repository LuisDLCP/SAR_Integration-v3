"""
Connection between a client and VNA's program
VNA_IP: local host, 127.0.0.1
VNA_PORT: 5025
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1',5025)) # server_ip, server_port
s.sendall(b"CALC2:TRAC1:DATA:SDAT?\n")
data=s.recv(1024)
print("Received ",repr(data))
