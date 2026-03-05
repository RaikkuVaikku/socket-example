import socket
import struct
import threading


def main():
    option = input("Enter 'subscribe' or 'query':\n").strip().lower()

    if option == "subscribe":
        address = input("Enter address:\n").strip()
        port = int(input("Enter port:\n").strip())
        subscribe(address, port)
    elif option == "query":
        address = input("Enter address:\n").strip()
        port = int(input("Enter port:\n").strip())
        query(address, port)
    else:
        print("Invalid option. Please enter 'subscribe' or 'query'.")


# Subscribe to multicast server (UDP)
def subscribe(address, port):
    # Create UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind to port
    sock.bind(("224.1.1.1", port))

    # Join multicast group
    group = socket.inet_aton(address)
    mreq = struct.pack("4sL", group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    print(
        f"Subscribed to multicast group {address} on port {port}. Listening for messages..."
    )

    threading.Thread(target=receive_message, args=(sock,), daemon=True).start()


# receive message function for thread
def receive_message(bound_socket):
    while True:
        data, sender = bound_socket.recvfrom(1024)
        message = data.decode()
        print(f"Received message: {message}")


# Query using TCP
def query(address, port):
    message = input("Enter message to send:\n").strip()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((address, port))
        # Send message
        sock.sendall((message + "\n").encode())
        print(f"Sent message: {message}")
        # Receive response
        response = sock.recv(1024).decode().strip()
        print(f"Received response: {response}")


if __name__ == "__main__":
    while True:
        main()
