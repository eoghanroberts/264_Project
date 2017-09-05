from struct import * 
class packet:
    def __init__(self, packet_type, seqno, dataLen, data):
        self.magicno = int('0x497E', 16) #is static
        self.packet_type = packet_type
        self.seqno = seqno
        self.dataLen = dataLen
        self.data = bytes(data, 'utf-8')
        
    #DISPLAY FUNCTIONS
    def displayPacket(self):
        print("Packet: ")
        print("Data: {}, Size {}".format(self.data, self.dataLen))
        print("DataType: {}".format(self.packet_type))
    
    def setPacketType(self):
        if self.packet_type == 0:
            self.packet_type = 'dataPacket'
        elif self.packet_type == 1:
            self.packet_type = 'acknowledgementPacket'
        else:
            print("Error setting Packet Type, wrong values used")
    
    def setSeqno(self):
        if self.seqno == 0 or self.seqno == 1:
            pass
        else:
            print("Error setting seqno, wrong values used")
            
    def setData(self):
        if self.dataLen == len(self.data) and self.dataLen <= 512:
            pass
        else:
            print("Error, data not complient with spesificatons")
            
    def struct_create(self):
        #magicno = unasigned short 
        #packet_type = Bool
        #seqno = Bool
        #dataLen = unasigned short
        #data = unasigned long long
        output_packet = pack('H??H{}s'.format(self.dataLen), 
                             self.magicno, 
                             self.packet_type, 
                             self.seqno, 
                             self.dataLen,
                             self.data)
        #gota convert the data into bits
        lenght = len(output_packet)
        #lenght = 0
        #lenght += len
        #lenght +=
        #lenght +=
        #lenght +=
        #lenght +=
        #lenght +=
        #print(output_packet)
        return output_packet, lenght
    

    def setUp(self):
        self.setPacketType()
        self.setData()
        packet_parts = self.struct_create()
        packet = packet_parts[0]
        lenght = packet_parts[1]
        #print(packet)
        #print(lenght)
        #len_message = self.message_length()
       
        return packet, lenght


#shows how a packet can be created and unpacked 
#test = packet(1, 1, 8, 'abduetse')
#packet = test.setUp()
#print(unpack('H??H{}s'.format(len(test.data)), packet))
