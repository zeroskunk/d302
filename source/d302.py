import sys
from window import Ui_d302reader 
import serial_d302
from PyQt5 import QtWidgets, QtCore, uic


class D302ReaderApp(QtWidgets.QMainWindow, QtCore.QObject, Ui_d302reader):
    def __init__(self, parent=None):

        self.version = '0.0.1'
        
        #super().__init__(parent)
        super(self.__class__, self).__init__()

        #self.ui = uic.loadUi('window.ui', self)
        self.setupUi(self)
        self.render_statusbar()
        #print(GetWindowText(self))
        #print(self.d302reader)
        
        self.d302 = serial_d302.d302()
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
        

    def render_statusbar(self):
        self.text_status = QtWidgets.QLineEdit('')
        self.text_status.setObjectName('statusbar_text')
        self.text_status.setStyleSheet('background: transparent; border: none;')
        self.text_status.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.text_status.setEnabled(False)
        self.statusbar.addWidget(self.text_status, 1)
        
        self.port_status = QtWidgets.QLineEdit()
        self.port_status.setEnabled(False)
        self.port_status.setMaximumSize(QtCore.QSize(60, 16777215))
        self.port_status.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.port_status.setStyleSheet("background: white;")
        self.port_status.setText("")
        #self.port_status.setMaxLength(3)
        self.port_status.setObjectName("statusbar_status")
        self.statusbar.addWidget(self.port_status)
        
        self.setWindowTitle("D302 Reader [Version: "+self.version+']')

    def write_statusbar(self, message, backgroundcolor = 'transparent',  textcolor = 'black'):
        self.text_status.setStyleSheet('background:'+backgroundcolor+';'+'color:'+textcolor+';')
        self.text_status.setText(message)
        return True
    
    def write_statusbar_widget(self, message, backgroundcolor = 'transparent',  textcolor = 'black'):
        self.port_status.setStyleSheet('background:'+backgroundcolor+';'+'color:'+textcolor+';')
        self.port_status.setText(message)
        return True

    def connect_port(self):
        port_checked = self.ports_available[self.combo_port.currentIndex()]
        serial_answer = self.d302.open_port(str(port_checked))
            
        if serial_answer:
            self.port_open_check.setChecked(True)
            self.write_statusbar_widget('open', 'green')
            self.btn_card_read.setEnabled(True)
          
        return True  

    def disconnect_port(self):
        serial_answer = self.d302.close_port()
        
        if serial_answer:
            self.port_open_check.setChecked(False)
            self.write_statusbar_widget('closed')
            self.btn_card_read.setEnabled(False)
        
        return True

    def dialog_popup(self, head, message, answer):
        QtWidgets.QMessageBox.about(self, head, " "+message+" = %s" % (answer))

    def read_card(self):
        serial_answer = self.d302.read_message()
        
        if  serial_answer != '':
            #self.message_box.setText(str(serial_answer))
            #self.statusbar.showMessage(serial_answer)
            self.write_statusbar(serial_answer)
            hex_string = serial_answer[8:-4];
            self.text_card_hex_checksum.setText('R '+serial_answer[-3:-2])
            self.fill_section_card(hex_string)
            self.fill_section_d10(hex_string)
            self.fill_section_w26(hex_string)
            self.btn_card_write.setEnabled(True)
        else:
            self.write_statusbar('NO CARD', 'red')

    def write_card(self):
        hex_string = self.text_card_hex.text()
        serial_answer = self.d302.write_message(hex_string)
        self.text_card_hex_checksum.setText('W '+hex(int(serial_answer[-2:]))[2:].zfill(2))

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
        read_NUM_dec = int(hex_string[6:], 16)
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
            
            #set max value of d10_fields in gui
            if int(d10_clientid) > 255: d10_clientid = 255
            if int(d10_numbers) > 4294967295: d10_numbers = 4294967295
            
            hex_1 = str(hex(int(d10_clientid))[2:]).zfill(2)
            hex_2 = str(hex(int(d10_numbers))[2:]).zfill(8)
            hex_string = hex_1 + hex_2
            
        if '_w26_' in obj.objectName():
            w26_clientid = self.text_w26_clientid.text().zfill(3)
            w26_fc = self.text_w26_fc.text().zfill(3)
            w26_numbers = self.text_w26_numbers.text().zfill(5)
            
            #set max value of w26_fields in gui
            if int(w26_clientid) > 255: w26_clientid = 255
            if int(w26_fc) > 255: w26_fc = 255
            if int(w26_numbers) > 65535 : w26_numbers = 65535
            
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
        
