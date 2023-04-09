import socket

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f'Server listening on {HOST}:{PORT}')

# Accept incoming connections
client_socket, address = server_socket.accept()

print(f'Connected by {address}')

# Receive the string from the client
data = client_socket.recv(1024).decode()

# Find the vowels in the string
vowels = [char for char in data if char.lower() in 'aeiou']

# Send the vowels to the client
client_socket.send(''.join(vowels).encode())

# Close the socket
client_socket.close()
server_socket.close()

