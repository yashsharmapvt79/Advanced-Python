import socket

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a port
    server_socket.bind(('0.0.0.0', 12345))
    
    # Listen for incoming connections
    server_socket.listen(5)
    print("Server listening on port 12345")
    
    while True:
        # Accept a connection from a client
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")
        
        # Receive data from the client
        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")
        
        # Send a response to the client
        client_socket.sendall(b"Hello from server")
        
        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()
