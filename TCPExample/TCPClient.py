# import socket
#
# targetHost = '192.168.15.10'
# targetPort = 4370
#
# # AF_INET for IPv4 Config and SOCK_STREAM for TCP Client Config
# #TODO(ornitorrinco) need for deal with blocking sockets
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((targetHost, targetPort))
# print(client)
# response = client.recv(4096)
#
# client.send(bytes('\r\n','utf-8'))
# # client.send(bytes('GET / HTTP/1.1\r\nhttp://192.168.15.10:4370/\r\n\r\n','utf-8'))
#
# print('TCP CLIENT: \n')
# print(response)



import socket

HOST = '192.168.15.10'                 # Symbolic name meaning all available interfaces
PORT = 4370              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)


#
#
# import socket
#
#
# TCP_IP = '192.168.15.10'
# TCP_PORT = 4370
# BUFFER_SIZE = 20  # Normally 1024, but we want fast response
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((TCP_IP, TCP_PORT))
# s.listen(1)
#
# conn, addr = s.accept()
# print('Connection address:', addr)
# while 1:
#     data = conn.recv(BUFFER_SIZE)
#     if not data: break
#     print ("received data:" + str(data))
#     conn.send(data)  # echo
# conn.close()
