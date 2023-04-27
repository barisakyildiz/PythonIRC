import socket
import colorama

class Client():
    def __init__(self):
        self.HOST = 'SERVER_IP'
        self.PORT = 6667 #Server port to connect
    
    def connect(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cl:
            cl.connect((self.HOST, self.PORT))
            print("Connected to Relay --> {}:{}".format(self.HOST, self.PORT))
            
            while True:
                message = input("Enter a message: ")
                cl.sendall(message.encode())
                data = cl.recv(1024)
                print("Recieved message from server: {}".format(data.decode()))

def main():
    client_obj = Client()
    client_obj.connect()

if __name__ == '__main__':
    main()