import socket
import sys
print("Cliente iniciado...")
HOST, PORT = "localhost", 9999
data = " ".join(sys.argv[1:])

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(bytes(data + "\n","utf8"), (HOST, PORT))
received = sock.recv(1024)

print("Enviado: {0}".format(data))
print("Recibido: {0}".format(received))
