#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.
from socket import socket, SOCK_DGRAM, AF_INET
from random import randint
from time import time

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print "Waiting for connections"
while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
     # Set start time as soon as packet is received
    startTime = time()
    # Drop packets randomly 10% of the time
    if randint(0, 9) == 0:
        continue
    # Capitalize the message from the client
    print message, address
    message = message.upper()
    serverSocket.sendto(message, address)
    # Set end time
    endTime = time()
    # Calculated time elapsed in ms
    elapsedTime = (endTime - startTime) * 1000
    print "RTT: " + str(elapsedTime) + " ms"
serverSocket.close()


#Configure the server so that it randomly drops packets.
#Include information about how long each response took. This will be the RTT.