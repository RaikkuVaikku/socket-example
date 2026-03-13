import socket
import random
from hash import Hasher

class Server:
    def __init__(self):
        self.tcp_port = 5000
        self.packetaddress = {"Playstation": "Otakaari 18", "AMD RYZEN 7799": "Jämeräntaival 11", "DRAM": "Servinkuja 3"}
        self.tcp_socket = None
        self.running = False
        self.hasher = Hasher("SHA256")
        self.delimiter = '-'
    def start(self):
        address = input("Enter the IP address of the serve")
        # Create a TCP socket that uses IPv4 addresses
        self.tcp_socket = socket.socket('?', '?')
        #Set the socket option so that it allows reuse of addres and ports
        #self.tcp_socket.setsockopt(level, option, value)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, '?', '?')

        with self.tcp_socket as socket:
            # Bind the socket to a port and address pair
            socket #.?((?, ?))
            # Put the socket into listening mode
            socket#.?()
            print(f"Listening on: {?}")
            #Accept an incoming connection. The function that accepts a connection returns
            # the clients socket object and address pair
            
            #client_socket, ? = socket.?()
            
            with client_socket:
             #print("Connection accepted")
             #Receive data from the connection
             buffer = #?.?(1024)
             data = buffer.decode().strip()
             message = self.packetaddress[data]
             sent_message = simulated_attack(message)
             #Get the hash of the message with the hasher
             messagehash = self.hasher.hash_message(message)
             complete_message = message + self.delimiter + messagehash
             client_socket.sendall(complete_message.encode())
             #Close the connection
             #client_socket.?

    def simulated_attack(self, tampered_message):
        randomval = random.randrange(1, 5)
        randomaddressindex = random.randrange(1, len(self.packetaddress.values()))
        if randomval == 1:
            return self.packetaddress.values()[randomaddressindex]
        else:
            return tampered_message
        

if __name__ == "__main__":
    server = Server()
    server.start()
