import socket
import threading

# Connection Details
host = '127.0.0.1'
port = 7000

# Setting Up the Server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen()

# Lists to Store Clients and Their Nicknames
clients = []
nicknames = []

# Function to Broadcast Messages to All Clients Except the Current One
def broadcast(message, current_client):
    for client in clients:
        if client == current_client:
            continue
        client.send(message)

# Function to Handle Messages from Clients
def handle_client(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message, client)
        except:
            # Removing and Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'), client)
            nicknames.remove(nickname)
            break

# Function for Receiving and Listening
def receive():
    while True:
        # Accepting Connections
        client_socket, address = server_socket.accept()
        print("Connected with {}".format(str(address)))

        # Requesting and Storing Nicknames
        client_socket.send('NICK'.encode('ascii'))
        nickname = client_socket.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client_socket)

        # Printing and Broadcasting Nicknames
        print("Nickname: {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'), client_socket)
        client_socket.send('Connected to the server!'.encode('ascii'))

        # Starting Thread to Handle Client
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

# Starting the Receiving Function
receive()
