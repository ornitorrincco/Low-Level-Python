import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print('[*] Listening on %s:%d' % (bind_ip, bind_port))

# is the client-handling thread
def handle_client(client_socket):
    print('[*] Received: %s' % request)

# send back a packet
client_socket.send('something')
client_socket.close()

while True:
    client, addr = server.accept()
    print('[*] Accepted Connection from: %s: %d' % (addr[0], addr[1]))

client_handler = threading.Thread(target=handle_client, args=(client,))
client_handler.start()
