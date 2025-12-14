import socket
import ssl

server_address = '192.168.1.243'
server_port = 8443

context = ssl._create_unverified_context()

with socket.create_connection((server_address, server_port)) as sock:
    with context.wrap_socket(sock, server_hostname=None) as tls_sock:
        while True:
            message = input("Type a message to send (or 'exit' to quit): ")
            if message.lower() in ['exit', 'quit']:
                print("Closing connection.")
                break
            tls_sock.sendall(message.encode())
            data = tls_sock.recv(1024)
            print(f"Received from server: {data.decode()}")


