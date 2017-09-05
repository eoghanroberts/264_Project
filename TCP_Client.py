import socket
import Packet
import pickle

def send():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    channel = ('localhost', 8000) #This will need to be dynamicly set (not static)
    #print("Sending from Client: port = {}".format(channel[1]))
    test = Packet.packet(1, 1, 8, 'abduetse')
    packet = test.setUp()
    packet.displayPacket()
    
    
    sock.connect(channel)
    
    try:
        #send Data
        print("sending {}".format(test.displayPacket()))
        sock.sendall(message.encode(encoding='utf-8'))
    
        #Look for response
        amount_received = 0
        amount_expected = len(message)
    
        while amount_received < amount_expected:
            data = sock.recv(518)
            amount_received += len(data)
            print("received {}".format(data))
    finally:
        print("close socket")
        sock.close()

send()
    