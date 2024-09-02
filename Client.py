import socket

def start_client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect(('localhost', 12345))
    
    # Send data to the server
    client_socket.sendall(b"Hello from client")
    
    # Receive a response from the server
    response = client_socket.recv(1024)
    print(f"Received from server: {response.decode()}")
    
    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    start_client()
