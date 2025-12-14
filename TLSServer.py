import socket
import ssl

def start_server():
    server_address = '0.0.0.0'
    server_port = 8443

    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(r"C:\Users\Daazl\Documents\TLSserver\server.crt",
                            keyfile=r"C:\Users\Daazl\Documents\TLSserver\server.key")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((server_address, server_port))
        sock.listen(5)
        print("[+] TLS Server listening...")

        while True:
            conn, addr = sock.accept()
            try:
                tls_conn = context.wrap_socket(conn, server_side=True)
                print(f"[+] Connection from {addr}")
                while True:
                    data = tls_conn.recv(1024)
                    if not data:
                        break
                    print(f"Received from client: {data.decode()}")
                    tls_conn.sendall(b"Message received!")
            except Exception as e:
                print(f"Connection error: {e}")
            finally:
                conn.close()

if __name__ == "__main__":
    start_server()

