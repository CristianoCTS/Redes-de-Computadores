import http.client

def HTTPclient(host, port):
    
    L = int(input())
    
    for i in range(L):
        
        content = input()
        conn = http.client.HTTPConnection(host, port)
        conn.request("GET", content)
        resp = conn.getresponse()
        headers = resp.getheaders()
        #print(headers)
        
        if headers[2][0] == "Connection":
            print(f"Content not found")
        elif headers[2][1] == "audio/mpeg":
            print(f"Playing audio: {content}")
        elif headers[2][1] == "text/html":
            print(f"Browsing: {content}")
        elif headers[2][1] == "video/x-msvideo":
            print(f"Playing media: {content}")
        elif headers[2][1] == "application/json":
            print(f"Processing JSON: {content}")
        else:
            print(f"Unknown file/media: {headers[2][1]}-{content}")