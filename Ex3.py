# import socket module
import socket
# http://localhost:55555/HelloWorld.html
from socket import *
import sys  # In order to terminate the program

SERVER_ADDRESS = ('', 55555)
serverSocket = socket(AF_INET, SOCK_STREAM) # here we crate a tcp socket,
# Prepare a sever socket
# Fill in start
serverSocket.bind(SERVER_ADDRESS) # connect the server to the server addres
serverSocket.listen(1) # listen
# Fill in end
while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() # accept client
    try:
        message = connectionSocket.recv(1024) # the client request
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP header line into socket
        # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
        # connectionSocket.send("HTTP/1.1 200 OK\n".encode('utf-8'))
        connectionSocket.send(fr'''HTTP/1.1 200 OK
        Content-Type: text/plain
        {outputdata}

        '''.encode())
        print(f'client has conect{addr}')
        # Fill in end
        # Send the content of the requested file to the client

        # for i in range(0, len(outputdata)):
        #     connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        break
    except IOError as e:
        # Send response message for file not found
        # Fill in start
        # connectionSocket.send("HTTP/1.1 404 Not Found\n".encode('utf-8'))
        print("the client search something that not exists")
        connectionSocket.send(fr'''HTTP/1.1 404 Not Found
        Content-Type: text/plain

        NOT FOUND
        '''.encode())
        # Fill in end
        # Close client socket
        # Fill in start
        connectionSocket.close() #close the connection between the client and the server.
        break
        # Fill in end
serverSocket.close() #close the server
sys.exit()  # Terminate the program after sending the corresponding data
