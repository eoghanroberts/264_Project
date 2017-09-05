import socket

def create_bind():
    #will create and bind all sockets needed
    
    #client to channel socket creation and bind
    client_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_channel.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #get an error without this
    client_channel.bind(('localhost', 8000)) #Port will need to be dynamicly set (not static)
    
    return client_channel #will need channel_server, server_channel, channel_client

def client_receive(client_channel):
    client_channel.listen(1) #number spesifies how many connections before droping shit   
    
    while True:
        #accept connections from client
        print('waiting for connection')
        (clientsocket, client_address) = client_channel.accept()
        
        try:
            print('connection from {}'.format(client_address))
            while True:
                data = clientsocket.recv(518) # this will need to be changed to incorperate a packet
                print(data)
                if data:
                    print('sending the same data back to client')
                    clientsocket.sendall(data)
                else:
                    print('no more data')
                    break
        finally:
            clientsocket.close()#when it closes is an issue
            print('the contents of test: {}'.format(data))



client_channel = create_bind()
client_receive(client_channel)

        
        