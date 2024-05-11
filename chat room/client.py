import socket
import threading

# Prompting the user to choose a nickname
nickname = input("Enter your nickname: ")

# Connecting to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 7000))

# Function to receive messages from the server and send the nickname
def receive_messages():
    while True:
        try:
            # Receiving messages from the server
            # If 'NICK', send the chosen nickname
            message = client_socket.recv(1024).decode('ascii')
            if message == 'NICK':
                client_socket.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Closing the connection in case of an error
            print("An error occurred!")
            client_socket.close()
            break

# Function to send messages to the server
def send_messages():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client_socket.send(message.encode('ascii'))

# Starting threads for receiving and sending messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
