import socket
import sys

server_address = ('localhost', 10000)
print("starting up on {} port {}".format(server_address[0], server_address[1]))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)
sock.listen(1) #number denotes how many connect requests before refusing outside connections

while True:
    print("waiting for a connection")
    connection, client_address = sock.accept()
    
    try:
        print("connection from {}".format(client_address))
        
        while True:
            data = connection.recv(50)
            print("reveived {}".format(data))
            if data:
                print("sending data back to the client")
                connection.sendall(data)
            else:
                print("no more data from".format(client_address))
                break
    finally:
        connection.close()
                
            

