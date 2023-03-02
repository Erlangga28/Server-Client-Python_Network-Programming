import socket
import sys
from datetime import datetime

server_address = ('localhost', 5001)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)

try:
    while True:
        client_socket, client_address = server_socket.accept()
        print(client_socket, client_address)
        
        data = client_socket.recv(1024).decode()
        print(str(data))
        dt = datetime.now()
        ts = datetime.timestamp(dt)
        
        f = open("log.txt","a")
        f.writelines([str(ts),"\n", str(client_socket),"\n", str(data)])
        f.close()
        
        client_socket.close()
        
except KeyboardInterrupt:
    server_socket.close()
    sys.exit(0)