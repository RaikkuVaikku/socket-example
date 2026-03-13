import socket
from hash import Hasher


class Client:
    def __init__(self):
        self.server_ip = input("Enter server IP: ")
        self.server_port = 5000
        self.delimiter = "-"
        self.hasher = Hasher("sha256")

    def start(self):
        product = input("Enter product name: ")

        # Create TCP socket
        with socket.socket('?', '?') as client_socket:
            # Connect to server
            client_socket.connect(('?', '?'))
            # Send product request
            client_socket#.?(product)
            
            # Receive response
            buffer = client_socket#.?(1024)
            data = buffer.decode().strip()

            print("Received:", data)

            # Split message and hash
            message, received_hash = data#.?()

            # Calculate hash locally
            calculated_hash = self.hasher.hash_message(message)

            # Verify integrity


if __name__ == "__main__":
    client = Client()
    client.start()