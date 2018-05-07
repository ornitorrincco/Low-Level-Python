import socketserver
print("Servidor iniciado...")
class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{0} Ha escrito:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)
if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = socketserver.UDPServer((HOST, PORT), MyUDPHandler)
    server.serve_forever()
