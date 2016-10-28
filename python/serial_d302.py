import serial
import time
import binascii

class d302():
    def __init__(self, parent=None):
        self.ser = serial.Serial()
        self.cardlock = False
        
    def calc_checksum(self, read_line):
        n = 2
        checksum = 0
        hex_list =  [read_line[i:i+n] for i in range(0, len(read_line), n)]
        for x in hex_list: 
            checksum ^= int(x,16)
        return checksum
        
    def int_list(self, read_line):
        hex_list =  [read_line[i:i+2] for i in range(0, len(read_line), 2)]
        hex_list_int = []
        for i in hex_list: hex_list_int.append(int(i,16))
        return hex_list_int
    
    def hex_list(self, read_line):
        read_line = str(binascii.hexlify(read_line), 'ascii')
        hex_list =  [read_line[i:i+2] for i in range(0, len(read_line), 2)]
        return hex_list
        
        
    def open_port(self, port='/dev/ttyUSB0'):
        try:
            self.ser.baudrate = 4800
            self.ser.xonxoff = 0
            self.ser.rtscts = False
            self.ser.bytesize = serial.EIGHTBITS
            self.ser.timeout = 3
            self.ser.write_timeout = 2
            self.ser.dsrdtr = True
            self.ser.rtscts = True
            self.ser.port = port
            self.ser.open()
            self.initial_message()
    
            return True
        except:
            return False
        
    def close_port(self):
        if self.ser.isOpen():
            self.ser.close()
            return True
        else:
            return False
            
    def initial_message(self):
        if self.ser.isOpen() == False:
            return False
        
        initString = bytearray([0x02, 0x01, 0x00, 0x00, 0x03, 0x03])
        self.ser.write(initString)
        answerString = self.ser.read(6)
        answerString = binascii.hexlify(answerString)
        print (answerString)
        return str(answerString, 'ascii')
        
    def read_message(self):
        self.initial_message()
        
        if self.ser.isOpen() == False:
            return False
        
        time.sleep(1)
        writeString = bytearray([0x02, 0x01, 0xa4, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xac, 0x03])
        self.ser.write(writeString)
        answerString = self.ser.read(11)
        answerString = binascii.hexlify(answerString)
        return str(answerString, 'ascii')
        
    def write_message(self, hex, lock=False):
        self.initial_message()
        
        if lock: 
            lockbit = 'ff' 
        else: 
            lockbit = '00'
            
        time.sleep(1)
        writeSeq = '0201a50b0000000000'
        lockSeq = lockbit
        checksumInt = self.calc_checksum(writeSeq+hex)
        intList = self.int_list(writeSeq+lockSeq+hex)
        writeString = bytearray(intList)+bytearray([checksumInt, 0x03])
        self.ser.write(writeString)
        time.sleep(1)
        return self.ser.read(self.ser.inWaiting()).encode('hex')
        
        
        
