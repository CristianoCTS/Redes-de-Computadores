import http.client
import socket

L = int(input())
    
for i in range(L):
    
    IP = input()
    resp = socket.gethostbyaddr(IP)
    print(resp[0])