import socket

targetHost = 'localhost'
targetPort = 9999

# AF_INET for IPv4 Config and SOCK_STREAM for TCP Client Config
#TODO(ornitorrinco) need for deal with blocking sockets
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((targetHost, targetPort))
print(client)
client.send(bytes('GET / HTTP/1.1\r\nhttps://localhost\r\n\r\n','utf-8'))
response = client.recv(4096)
print('TCP CLIENT: \n')
print(response)
