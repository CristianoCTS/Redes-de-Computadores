import http.client

def HTTPclient(host, port):
    
    L = int(input())
    
    for i in range(L):
        
        content = input()
        conn = http.client.HTTPConnection(host, port)
        conn.request("GET", content)
        resp = conn.getresponse()
        print(resp.read().decode())
        