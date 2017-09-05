#import socket
#from struct import *
#from Packet import packet

#test = packet(1, 1, 8, 'abduetse')
#packet = test.setUp()
#print(unpack('H??H{}s'.format(len(test.data)), packet))

#def send():
    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #channel = ('localhost', 8000) #This will need to be dynamicly set (not static)
    ##print("Sending from Client: port = {}".format(channel[1])    
    #sock.connect(host, port) #host and port not yet set
    
    #try:
        #sentdata = 0
        #while sentdata < message_len:
            #sent = self.sock.send(message[sentdata:])
            #if sent == 0:
                #raise RuntimeError("Connection to socket broken")
            
        
    #finally:
        #print("close socket")
        #sock.close()

#send()

import socket
from struct import *
from Packet import packet

#test = packet(1, 1, 8, 'abduetse')
#packet = test.setUp()
def send(packet):
    message = packet[0]
    lenght = packet[1]
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    channel = ('localhost', 8000) #This will need to be dynamicly set (not static)
    #print("Sending from Client: port = {}".format(channel[1]))
    
    


    sock.connect(channel)

    try:
        ##send Data
        ##print("sending {}".format(test.displayPacket()))
        #sock.sendall(message.encode(encoding='utf-8'))

        ##Look for response
        #amount_received = 0
        #amount_expected = len(message)

        #while amount_received < amount_expected:
            #data = sock.recv(518)
            #amount_received += len(data)
            #print("received {}".format(data))
        totalsent = 0
        while totalsent < lenght:
            sent = self.sock.send(message[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent        
    finally:
        print("close socket")
        sock.close()

send(packet(1, 1, 8, 'abduetse').setUp())
    
