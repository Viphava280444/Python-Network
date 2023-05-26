#Server Side Chat Room
import socket, threading


#Define constants to be used
#HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_IP = "192.168.1.154"
HOST_PORT = 12345
ENCODER = 'utf-8'
BYTESIZE = 1024
TTL = 6 # Number of time to live


# Multicast_Group
# Create a UDP socket
print("Server is running")
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST_IP, HOST_PORT))

# Config TTL
sock.setsockopt(socket.IPPROTO_IP, socket.IP_TTL, TTL)

# Bind the socket to the multicast address and port


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()


#Create two blank lists to store connected client sockets and their names
client_socket_list = []
client_name_list = []

#Send a message to ALL clients connected to the server
def broadcast_message(message):
    for client_socket in client_socket_list:
        client_socket.send(message)

#Recieve an incoming message from a specific client and forward the message to be broadcast
def recieve_message(client_socket):
    while True:
        try:
            #Get the name of the given client
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]
            
            #Recieve message from the client
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            message = f"{name}: {message}".encode(ENCODER)
            broadcast_message(message)
        except:
            #Find the index of the client socket in our list
            index = client_socket_list.index(client_socket)
            name = client_name_list[index]

            #Remove the client socket and name from lists
            client_socket_list.remove(client_socket)
            client_name_list.remove(name)

            #Close the client socket
            client_socket.close()

            #Broadcast that the client has left the chat.
            broadcast_message(f"{name} has left the chat!".encode(ENCODER))
            break

#Connect an incoming client to the server
def connect_client():
    while True:
        # Receive a message from a client with UDP
        message, address = sock.recvfrom(1024)
        message = "a"
        # Send message to client with UDP and TTL configulation
        sock.sendto(message.encode(ENCODER), (address))

        #Accept any incoming client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connected with {client_address}...")

        #Send a NAME flag to prompt the client for their name
        client_socket.send("NAME".encode(ENCODER))
        client_name = client_socket.recv(BYTESIZE).decode(ENCODER)

        #Add new client socket and client name to appropriate lists
        client_socket_list.append(client_socket)
        client_name_list.append(client_name)

        #Update the server, individual client, and ALL clients
        print(f"Name of new client is {client_name}\n") #server
        client_socket.send(f"{client_name}, you have connected to the server!".encode(ENCODER)) #Individual client
        broadcast_message(f"{client_name} has joined the chat!".encode(ENCODER))

        #Now that a new client has connected, start a thread
        recieve_thread = threading.Thread(target=recieve_message, args=(client_socket,))
        recieve_thread.start()


#Start the server
print(f"Server ({HOST_IP}) is listening for incoming connections... with TTL = {TTL}\n")
connect_client()
