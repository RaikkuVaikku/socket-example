import socket
import threading
import time
import random

class Server:
    def __init__(self):
        self.tcp_port = 5000
        self.multicast_port = 5000
        self.multicast_address = "224.1.1.1"
        self.multicast_message = ""
        self.stocks = {"Nvidia": 300, "OpenAI": 180, "AMD": 500}
        self.tcp_socket = None
        self.multicast_socket = None
        self.running = False

    def start(self):
        # Initialize TCP server socket
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.tcp_socket.bind(("", self.tcp_port))
        self.tcp_socket.listen()

        # Initialize multicast socket (UDP)
        self.multicast_socket = socket.socket(
            socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP
        )

        self.running = True

        # Start multicast sender thread
        threading.Thread(target=self.start_multicast_sender, daemon=True).start()
        print("CURL!")

        # Start TCP listener (main thread)
        self.start_tcp_listener()

    def stop(self):
        self.running = False
        if self.tcp_socket:
            self.tcp_socket.close()
        if self.multicast_socket:
            self.multicast_socket.close()

    def start_tcp_listener(self):
        print(f"TCP server listening on port {self.tcp_port}...")

        while self.running:
            client_socket, addr = self.tcp_socket.accept()
            print(f"Client connected from {addr}")
            handler = TCPClientHandler(client_socket, self.stocks)
            handler.start()

    def start_multicast_sender(self):
        print("Starting multicast sender...")

        while self.running:
            if len(self.multicast_message) == 0:
                for x, y in self.stocks.items():
                    self.multicast_message += str(x) + ": " + str(y) + ", "
            message_bytes = self.multicast_message.encode()
            print(message_bytes)
            # Send multicast packet
            self.multicast_socket.sendto(
                message_bytes, (self.multicast_address, self.multicast_port)
            )
            print("Sent a multicast message")
            self.randomize_prices()
            time.sleep(10)

    def randomize_prices(self):
        for i in self.stocks:
            self.stocks[i] = random.randrange(5000)
        self.multicast_message = ""


class TCPClientHandler(threading.Thread):
    def __init__(self, client_socket, stocks):
        super().__init__()
        self.client_socket = client_socket
        self.stocks = stocks

    def run(self):
        try:
            buffer = self.client_socket.recv(1024)
            if not buffer:
                return

            input_line = buffer.decode().strip()
            print("Received:", input_line)

            if input_line in self.stocks.keys():
                message = input_line + ": " + str(self.stocks[input_line])
                self.client_socket.sendall(message.encode())
            else:
                self.client_socket.sendall(b"No such stock")
        except OSError as e:
            print("Connection closed:", str(e))

        finally:
            self.client_socket.close()


if __name__ == "__main__":
    server = Server()
    server.start()
