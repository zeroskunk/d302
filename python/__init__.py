import sys
import serial_d302 as connect
from PyQt5 import QtWidgets, uic

class D302ReaderApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = uic.loadUi('window.ui', self)
        self.d302 = connect.d302()
        self.d10_group.setEnabled(False)
        self.w26_group.setEnabled(False)
        
        self.btn_port_open.clicked.connect(self.connect_port)
        self.btn_port_close.clicked.connect(self.disconnect_port)
        self.btn_card_read.clicked.connect(self.read_card)
        self.btn_radio_d10.clicked.connect(lambda: self.enable_group('d10'))
        self.btn_radio_w26.clicked.connect(lambda: self.enable_group('w26'))
        
    def connect_port(self):
        if self.text_port.text():
            serial_answer = self.d302.open_port(self.text_port.text())
        else:
            serial_answer = self.d302.open_port()
            
        if serial_answer:
            self.port_open_check.setChecked(True)
            self.port_open_check.setStyleSheet("background: green;")
            self.btn_card_read.setEnabled(True)
            
        return self.dialog_popup('PORT', 'port open',  serial_answer)
        
        
    def disconnect_port(self):
        serial_answer = self.d302.close_port()
        return self.dialog_popup('PORT', 'port close',  serial_answer)
        
    def dialog_popup(self, head, message, answer):
        QtWidgets.QMessageBox.about(self, head, " "+message+" = %s" % (answer))
        
    def read_card(self):
        serial_answer = self.d302.read_message()
        self.message_box.setText(serial_answer)
        hex_string = serial_answer[8:-4];
        
        self.fill_section_card(hex_string)
        self.fill_section_d10(hex_string)
        self.fill_section_w26(hex_string)
        
    def fill_section_card(self, hex_string):
        self.text_card_hex.setText(hex_string)
        i = 9
        while i >= 0:
            string = 'self.text_card_hex_'+str(i)+'.setText("'+hex_string[i]+'")'
            exec(string)
            i= i-1
    
    def fill_section_d10(self, hex_string):
        read_CID_dec = int(hex_string[:2], 16)
        read_FC_NUM_dec = int(hex_string[2:], 16)
        self.text_d10_clientid.setText(str(read_CID_dec))
        self.text_d10_numbers.setText(str(read_FC_NUM_dec))
        
    def fill_section_w26(self, hex_string):
        read_CID_dec = int(hex_string[:2], 16)
        read_FC_dec = int(hex_string[2:4], 16)
        read_NUM_dec = int(hex_string[4:], 16)
        self.text_w26_clientid.setText(str(read_CID_dec))
        self.text_w26_fc.setText(str(read_FC_dec))
        self.text_w26_numbers.setText(str(read_NUM_dec))
        
    def enable_group(self, group_name):
        if group_name == 'd10':
            self.d10_group.setEnabled(True)
            self.w26_group.setEnabled(False)
        elif group_name == 'w26':
            self.d10_group.setEnabled(False)
            self.w26_group.setEnabled(True)
            
        
        
    
        
app = QtWidgets.QApplication(sys.argv)
dialog = D302ReaderApp()
dialog.show()
sys.exit(app.exec_())
        
