import socket

targetHost = 'www.google.com'
targetPort = 80

# AF_INET for IPv4 Config and SOCK_STREAM for TCP Client Config
#TODO(ornitorrinco) need for deal with blocking sockets
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((targetHost, targetPort))
client.send(bytes('GET / HTTP/1.1\r\nHOST: google.com\r\n\r\n','utf-8'))
response = client.recv(4096)
print('TCP CLIENT: \n\n')
print(response)

targetHost = '127.0.0.1'
targetPort = 80
# UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind((targetHost, targetPort))
client.sendto(bytes('Something to Test', 'utf-8'),(targetHost, targetPort))

data, addr = client.recvfrom(4096)
print('UDP CLIENT: \n\n')
print(data)
