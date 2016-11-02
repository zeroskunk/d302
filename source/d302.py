import sys
import serial_d302 as connect

from PyQt5 import QtWidgets, QtCore, uic


class D302ReaderApp(QtWidgets.QMainWindow, QtCore.QObject):
    def __init__(self, parent=None):
        #super().__init__(parent)
        super(self.__class__, self).__init__()

        self.ui = uic.loadUi('window.ui', self)
        self.d302 = connect.d302()
        self.d10_group.setEnabled(False)
        self.w26_group.setEnabled(False)
        
        self.btn_port_open.clicked.connect(self.connect_port)
        self.btn_port_close.clicked.connect(self.disconnect_port)
        self.btn_card_read.clicked.connect(self.read_card)
        self.btn_card_write.clicked.connect(self.write_card)
        self.btn_radio_d10.clicked.connect(lambda: self.enable_group('d10'))
        self.btn_radio_w26.clicked.connect(lambda: self.enable_group('w26'))
        self.text_d10_clientid.editingFinished.connect(lambda: self.edit_change(self.text_d10_clientid))
        self.text_d10_numbers.editingFinished.connect(lambda: self.edit_change(self.text_d10_numbers))
        self.text_w26_clientid.editingFinished.connect(lambda: self.edit_change(self.text_w26_clientid))
        self.text_w26_fc.editingFinished.connect(lambda: self.edit_change(self.text_w26_fc))
        self.text_w26_numbers.editingFinished.connect(lambda: self.edit_change(self.text_w26_numbers))
        
        self.ports_available = self.d302.serial_ports()
        self.combo_port.addItems(self.ports_available)

    def connect_port(self):
        port_checked = self.ports_available[self.combo_port.currentIndex()]
        serial_answer = self.d302.open_port(str(port_checked))
            
        if serial_answer:
            self.port_open_check.setChecked(True)
            self.port_open_check.setStyleSheet("background: green;")
            self.btn_card_read.setEnabled(True)
          
        return True  

    def disconnect_port(self):
        serial_answer = self.d302.close_port()
        
        if serial_answer:
            self.port_open_check.setChecked(False)
            self.port_open_check.setStyleSheet('')
            self.btn_card_read.setEnabled(False)
        
        return True

    def dialog_popup(self, head, message, answer):
        QtWidgets.QMessageBox.about(self, head, " "+message+" = %s" % (answer))

    def read_card(self):
        serial_answer = self.d302.read_message()
        
        if  serial_answer != '':
            self.message_box.setText(str(serial_answer))
            hex_string = serial_answer[10:-5];
            self.text_card_hex_checksum.setText('R'+serial_answer[-5:-3])
            self.fill_section_card(hex_string)
            self.fill_section_d10(hex_string)
            self.fill_section_w26(hex_string)
            self.btn_card_write.setEnabled(True)
        else:
            self.message_box.setText('NO CARD')

    def write_card(self):
        hex_string = self.text_card_hex.text()
        serial_answer = self.d302.write_message(hex_string)
        self.text_card_hex_checksum.setText('W'+hex(int(serial_answer[-2:]))[2:].zfill(2))

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
            
    def edit_change(self, obj):
        if '_d10_' in obj.objectName():
            d10_clientid = self.text_d10_clientid.text().zfill(3)
            d10_numbers = self.text_d10_numbers.text().zfill(10)
            hex_1 = str(hex(int(d10_clientid))[2:]).zfill(2)
            hex_2 = str(hex(int(d10_numbers))[2:]).zfill(8)
            hex_string = hex_1 + hex_2
            
        if '_w26_' in obj.objectName():
            w26_clientid = self.text_w26_clientid.text().zfill(3)
            w26_fc = self.text_w26_fc.text().zfill(3)
            w26_numbers = self.text_w26_numbers.text().zfill(5)
            hex_1 = str(hex(int(w26_clientid))[2:]).zfill(2)
            hex_2 = str(hex(int(w26_fc))[2:]).zfill(2)
            hex_3 = str(hex(int(w26_numbers))[2:]).zfill(6)
            hex_string = hex_1+hex_2+hex_3
            
        self.fill_section_card(hex_string)
        self.fill_section_d10(hex_string)
        self.fill_section_w26(hex_string)

app = QtWidgets.QApplication(sys.argv)
dialog = D302ReaderApp()
dialog.show()
sys.exit(app.exec_())
        
