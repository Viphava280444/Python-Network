# UDP Client side

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Send some information via a connectionless protocol
for i in range(3):
    client_socket.sendto("Hello server world!!!".encode("utf-8"), ("1.1.1.1", 12345))
    print("Hello")