import socket
import threading

class Server:
    def __init__(self):
        self.HOST = 'localhost'
        self.PORT = 6667 # Desired port to be used as server
        self.clients = []

    def clientHandler(self, connection, address):
        print("New connection from {}".format(address))
        with connection:
            self.clients.append(connection)
            while True:
                data = connection.recv(1024)
                if not data:
                    print("Connection closed with remote host: {}".format(address))
                    self.clients.remove(connection)
                    break
                print("Recieved message from {}: {}".format(address, data.decode()))
                for client in self.clients:
                    if client != connection:
                        connection.sendall(data)
    

def main():
    server_obj = Server()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc:
        sc.bind((server_obj.HOST, server_obj.PORT))
        sc.listen()
        print("Server started listening on {}:{}".format(server_obj.HOST, server_obj.PORT))
        
        while True:
            connection, address = sc.accept()
            thr = threading.Thread(target=server_obj.clientHandler, args=(connection, address))
            thr.start()

if __name__ == '__main__':
    main()