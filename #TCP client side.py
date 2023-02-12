#TCP client side

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect the socket to a server located at a given IP and Port
client_socket.connect((socket.gethostbyname(socket.gethostname()), 12345))

#Recieve a message from the server...You must specify the max number of bytes to recieve
message = client_socket.recv(10)
print(message.decode("utf-8"))
message = client_socket.recv(10)
print(message.decode("utf-8"))