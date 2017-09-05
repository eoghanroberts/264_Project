import socket
from Packet import packet

def create_bind():
    #will create and bind all sockets needed
    
    #client to channel socket creation and bind
    client_channel = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_channel.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #get an error without this
    client_channel.bind(('localhost', 8000)) #Port will need to be dynamicly set (not static)
    
    return client_channel #will need channel_server, server_channel, channel_client

def client_receive(client_channel, packet):
    MSGLEN = packet[1]
    client_channel.listen(1) #number spesifies how many connections before droping shit   
    chunks = []
    bytes_recd = 0
    while bytes_recd < MSGLEN:
        chunk = client_channel.recv(min(MSGLEN - bytes_recd, 2048))
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return b''.join(chunks)    
    #while True:
        ##accept connections from client
        #print('waiting for connection')
        #(clientsocket, client_address) = client_channel.accept()
        
        #try:
            #print('connection from {}'.format(client_address))
            #while True:
                #data = clientsocket.recv(50) # this will need to be changed to incorperate a packet
                #print(data, "stuff might be working")
                #test = data
                #if data:
                    #print('sending the same data back to client')
                    #clientsocket.sendall(data)
                #else:
                    #print('no more data')
                    #break
        #finally:
            #clientsocket.close()#when it closes is an issue
            #print('the contents of test: {}'.format(test))



client_channel = create_bind()
client_receive(client_channel, packet(1, 1, 8, 'abduetse').setUp())

        
        
