# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_d302reader(object):
    def setupUi(self, d302reader):
        d302reader.setObjectName("d302reader")
        d302reader.resize(437, 525)
        self.centralwidget = QtWidgets.QWidget(d302reader)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 383, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.combo_port = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo_port.setObjectName("combo_port")
        self.horizontalLayout.addWidget(self.combo_port)
        self.port_open_check = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.port_open_check.setEnabled(False)
        self.port_open_check.setMaximumSize(QtCore.QSize(15, 16777215))
        self.port_open_check.setStyleSheet("")
        self.port_open_check.setText("")
        self.port_open_check.setChecked(False)
        self.port_open_check.setObjectName("port_open_check")
        self.horizontalLayout.addWidget(self.port_open_check)
        self.btn_port_open = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_port_open.setObjectName("btn_port_open")
        self.portButtonGroup = QtWidgets.QButtonGroup(d302reader)
        self.portButtonGroup.setObjectName("portButtonGroup")
        self.portButtonGroup.addButton(self.btn_port_open)
        self.horizontalLayout.addWidget(self.btn_port_open)
        self.btn_port_close = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_port_close.setObjectName("btn_port_close")
        self.portButtonGroup.addButton(self.btn_port_close)
        self.horizontalLayout.addWidget(self.btn_port_close)
        self.btn_card_read = QtWidgets.QPushButton(self.centralwidget)
        self.btn_card_read.setEnabled(False)
        self.btn_card_read.setGeometry(QtCore.QRect(40, 415, 85, 27))
        self.btn_card_read.setObjectName("btn_card_read")
        self.btn_card_write = QtWidgets.QPushButton(self.centralwidget)
        self.btn_card_write.setEnabled(False)
        self.btn_card_write.setGeometry(QtCore.QRect(130, 415, 85, 27))
        self.btn_card_write.setObjectName("btn_card_write")
        self.card_lock = QtWidgets.QCheckBox(self.centralwidget)
        self.card_lock.setGeometry(QtCore.QRect(300, 415, 101, 20))
        self.card_lock.setObjectName("card_lock")
        self.text_card_hex = QtWidgets.QLineEdit(self.centralwidget)
        self.text_card_hex.setEnabled(True)
        self.text_card_hex.setGeometry(QtCore.QRect(40, 370, 201, 26))
        self.text_card_hex.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_card_hex.setStyleSheet("background: white;")
        self.text_card_hex.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.text_card_hex.setReadOnly(False)
        self.text_card_hex.setPlaceholderText("")
        self.text_card_hex.setObjectName("text_card_hex")
        self.message_box = QtWidgets.QTextEdit(self.centralwidget)
        self.message_box.setEnabled(False)
        self.message_box.setGeometry(QtCore.QRect(40, 450, 361, 41))
        self.message_box.setStyleSheet("background: transparent; color:red;")
        self.message_box.setObjectName("message_box")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setEnabled(False)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 330, 361, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.text_card_hex_0 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_0.setEnabled(False)
        self.text_card_hex_0.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_0.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_0.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_0.setReadOnly(True)
        self.text_card_hex_0.setPlaceholderText("")
        self.text_card_hex_0.setObjectName("text_card_hex_0")
        self.horizontalLayout_9.addWidget(self.text_card_hex_0)
        self.text_card_hex_1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_1.setEnabled(False)
        self.text_card_hex_1.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_1.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_1.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_1.setReadOnly(True)
        self.text_card_hex_1.setPlaceholderText("")
        self.text_card_hex_1.setObjectName("text_card_hex_1")
        self.horizontalLayout_9.addWidget(self.text_card_hex_1)
        self.text_card_hex_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_2.setEnabled(False)
        self.text_card_hex_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_2.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_2.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_2.setReadOnly(True)
        self.text_card_hex_2.setPlaceholderText("")
        self.text_card_hex_2.setObjectName("text_card_hex_2")
        self.horizontalLayout_9.addWidget(self.text_card_hex_2)
        self.text_card_hex_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_3.setEnabled(False)
        self.text_card_hex_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_3.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_3.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_3.setReadOnly(True)
        self.text_card_hex_3.setPlaceholderText("")
        self.text_card_hex_3.setObjectName("text_card_hex_3")
        self.horizontalLayout_9.addWidget(self.text_card_hex_3)
        self.text_card_hex_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_4.setEnabled(False)
        self.text_card_hex_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_4.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_4.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_4.setReadOnly(True)
        self.text_card_hex_4.setPlaceholderText("")
        self.text_card_hex_4.setObjectName("text_card_hex_4")
        self.horizontalLayout_9.addWidget(self.text_card_hex_4)
        self.text_card_hex_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_5.setEnabled(False)
        self.text_card_hex_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_5.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_5.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_5.setReadOnly(True)
        self.text_card_hex_5.setPlaceholderText("")
        self.text_card_hex_5.setObjectName("text_card_hex_5")
        self.horizontalLayout_9.addWidget(self.text_card_hex_5)
        self.text_card_hex_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_6.setEnabled(False)
        self.text_card_hex_6.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_6.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_6.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_6.setReadOnly(True)
        self.text_card_hex_6.setPlaceholderText("")
        self.text_card_hex_6.setObjectName("text_card_hex_6")
        self.horizontalLayout_9.addWidget(self.text_card_hex_6)
        self.text_card_hex_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_7.setEnabled(False)
        self.text_card_hex_7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_7.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_7.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_7.setReadOnly(True)
        self.text_card_hex_7.setPlaceholderText("")
        self.text_card_hex_7.setObjectName("text_card_hex_7")
        self.horizontalLayout_9.addWidget(self.text_card_hex_7)
        self.text_card_hex_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_8.setEnabled(False)
        self.text_card_hex_8.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_8.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_8.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_8.setReadOnly(True)
        self.text_card_hex_8.setPlaceholderText("")
        self.text_card_hex_8.setObjectName("text_card_hex_8")
        self.horizontalLayout_9.addWidget(self.text_card_hex_8)
        self.text_card_hex_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.text_card_hex_9.setEnabled(False)
        self.text_card_hex_9.setMaximumSize(QtCore.QSize(30, 16777215))
        self.text_card_hex_9.setStyleSheet("background: white; color: blue;")
        self.text_card_hex_9.setAlignment(QtCore.Qt.AlignCenter)
        self.text_card_hex_9.setReadOnly(True)
        self.text_card_hex_9.setPlaceholderText("")
        self.text_card_hex_9.setObjectName("text_card_hex_9")
        self.horizontalLayout_9.addWidget(self.text_card_hex_9)
        self.text_card_hex_checksum = QtWidgets.QLineEdit(self.centralwidget)
        self.text_card_hex_checksum.setEnabled(False)
        self.text_card_hex_checksum.setGeometry(QtCore.QRect(250, 370, 41, 26))
        self.text_card_hex_checksum.setStyleSheet("background: white;")
        self.text_card_hex_checksum.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.text_card_hex_checksum.setReadOnly(True)
        self.text_card_hex_checksum.setPlaceholderText("")
        self.text_card_hex_checksum.setObjectName("text_card_hex_checksum")
        self.d10_group = QtWidgets.QGroupBox(self.centralwidget)
        self.d10_group.setEnabled(True)
        self.d10_group.setGeometry(QtCore.QRect(130, 90, 271, 81))
        self.d10_group.setAutoFillBackground(False)
        self.d10_group.setStyleSheet("background: #D8DCFF;")
        self.d10_group.setTitle("")
        self.d10_group.setFlat(False)
        self.d10_group.setCheckable(False)
        self.d10_group.setObjectName("d10_group")
        self.layoutWidget = QtWidgets.QWidget(self.d10_group)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 271, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setMaximumSize(QtCore.QSize(62, 16777215))
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setStyleSheet("")
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setStyleSheet("")
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.text_d10_clientid = QtWidgets.QLineEdit(self.layoutWidget)
        self.text_d10_clientid.setEnabled(True)
        self.text_d10_clientid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.text_d10_clientid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_d10_clientid.setStyleSheet("background: white;")
        self.text_d10_clientid.setText("")
        self.text_d10_clientid.setMaxLength(3)
        self.text_d10_clientid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_d10_clientid.setObjectName("text_d10_clientid")
        self.horizontalLayout_3.addWidget(self.text_d10_clientid)
        self.text_d10_numbers = QtWidgets.QLineEdit(self.layoutWidget)
        self.text_d10_numbers.setEnabled(True)
        self.text_d10_numbers.setMaximumSize(QtCore.QSize(200, 16777215))
        self.text_d10_numbers.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_d10_numbers.setStyleSheet("background: white;")
        self.text_d10_numbers.setText("")
        self.text_d10_numbers.setMaxLength(10)
        self.text_d10_numbers.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_d10_numbers.setObjectName("text_d10_numbers")
        self.horizontalLayout_3.addWidget(self.text_d10_numbers)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setMaximumSize(QtCore.QSize(67, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #E83151;")
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("color: #E83151; ")
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setWordWrap(False)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.w26_group = QtWidgets.QGroupBox(self.centralwidget)
        self.w26_group.setEnabled(True)
        self.w26_group.setGeometry(QtCore.QRect(130, 210, 271, 81))
        self.w26_group.setStyleSheet("background: #D8DCFF;")
        self.w26_group.setTitle("")
        self.w26_group.setObjectName("w26_group")
        self.layoutWidget1 = QtWidgets.QWidget(self.w26_group)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 0, 271, 81))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(5, 0, 5, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setMaximumSize(QtCore.QSize(62, 16777215))
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setMaximumSize(QtCore.QSize(62, 16777215))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setAutoFillBackground(False)
        self.label_11.setStyleSheet("")
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_6.addWidget(self.label_11)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.text_w26_clientid = QtWidgets.QLineEdit(self.layoutWidget1)
        self.text_w26_clientid.setEnabled(True)
        self.text_w26_clientid.setMaximumSize(QtCore.QSize(60, 16777215))
        self.text_w26_clientid.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_w26_clientid.setStyleSheet("background: white;")
        self.text_w26_clientid.setText("")
        self.text_w26_clientid.setMaxLength(3)
        self.text_w26_clientid.setCursorPosition(3)
        self.text_w26_clientid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_w26_clientid.setObjectName("text_w26_clientid")
        self.horizontalLayout_7.addWidget(self.text_w26_clientid)
        self.text_w26_fc = QtWidgets.QLineEdit(self.layoutWidget1)
        self.text_w26_fc.setEnabled(True)
        self.text_w26_fc.setMaximumSize(QtCore.QSize(60, 16777215))
        self.text_w26_fc.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_w26_fc.setStyleSheet("background: white;")
        self.text_w26_fc.setText("")
        self.text_w26_fc.setMaxLength(3)
        self.text_w26_fc.setCursorPosition(3)
        self.text_w26_fc.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_w26_fc.setObjectName("text_w26_fc")
        self.horizontalLayout_7.addWidget(self.text_w26_fc)
        self.text_w26_numbers = QtWidgets.QLineEdit(self.layoutWidget1)
        self.text_w26_numbers.setEnabled(True)
        self.text_w26_numbers.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.text_w26_numbers.setStyleSheet("background: white;")
        self.text_w26_numbers.setText("")
        self.text_w26_numbers.setMaxLength(5)
        self.text_w26_numbers.setCursorPosition(5)
        self.text_w26_numbers.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.text_w26_numbers.setObjectName("text_w26_numbers")
        self.horizontalLayout_7.addWidget(self.text_w26_numbers)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: #E83151;")
        self.label_9.setWordWrap(False)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setMaximumSize(QtCore.QSize(55, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_10.setStyleSheet("color: #E83151;")
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setWordWrap(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_12.setStyleSheet("color: #E83151; ")
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setWordWrap(False)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.btn_radio_w26 = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_radio_w26.setGeometry(QtCore.QRect(40, 190, 96, 20))
        self.btn_radio_w26.setObjectName("btn_radio_w26")
        self.radioButtonGroup = QtWidgets.QButtonGroup(d302reader)
        self.radioButtonGroup.setObjectName("radioButtonGroup")
        self.radioButtonGroup.addButton(self.btn_radio_w26)
        self.btn_radio_d10 = QtWidgets.QRadioButton(self.centralwidget)
        self.btn_radio_d10.setGeometry(QtCore.QRect(40, 70, 91, 20))
        self.btn_radio_d10.setObjectName("btn_radio_d10")
        self.radioButtonGroup.addButton(self.btn_radio_d10)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 200, 360, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(40, 395, 360, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(40, 80, 360, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(40, 310, 360, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        d302reader.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(d302reader)
        self.statusbar.setObjectName("statusbar")
        d302reader.setStatusBar(self.statusbar)

        self.retranslateUi(d302reader)
        QtCore.QMetaObject.connectSlotsByName(d302reader)
        d302reader.setTabOrder(self.btn_port_open, self.btn_port_close)
        d302reader.setTabOrder(self.btn_port_close, self.text_w26_clientid)
        d302reader.setTabOrder(self.text_w26_clientid, self.text_w26_fc)
        d302reader.setTabOrder(self.text_w26_fc, self.text_w26_numbers)
        d302reader.setTabOrder(self.text_w26_numbers, self.btn_card_read)
        d302reader.setTabOrder(self.btn_card_read, self.btn_card_write)
        d302reader.setTabOrder(self.btn_card_write, self.text_card_hex)
        d302reader.setTabOrder(self.text_card_hex, self.card_lock)
        d302reader.setTabOrder(self.card_lock, self.text_card_hex_0)
        d302reader.setTabOrder(self.text_card_hex_0, self.text_card_hex_1)
        d302reader.setTabOrder(self.text_card_hex_1, self.text_card_hex_2)
        d302reader.setTabOrder(self.text_card_hex_2, self.text_card_hex_3)
        d302reader.setTabOrder(self.text_card_hex_3, self.text_card_hex_4)
        d302reader.setTabOrder(self.text_card_hex_4, self.text_card_hex_5)
        d302reader.setTabOrder(self.text_card_hex_5, self.text_card_hex_6)
        d302reader.setTabOrder(self.text_card_hex_6, self.text_card_hex_8)
        d302reader.setTabOrder(self.text_card_hex_8, self.text_card_hex_9)
        d302reader.setTabOrder(self.text_card_hex_9, self.port_open_check)
        d302reader.setTabOrder(self.port_open_check, self.message_box)

    def retranslateUi(self, d302reader):
        _translate = QtCore.QCoreApplication.translate
        d302reader.setWindowTitle(_translate("d302reader", "D302 Reader"))
        self.btn_port_open.setText(_translate("d302reader", "open Port"))
        self.btn_port_close.setText(_translate("d302reader", "close Port"))
        self.btn_card_read.setText(_translate("d302reader", "readCard"))
        self.btn_card_write.setText(_translate("d302reader", "writeCard"))
        self.card_lock.setText(_translate("d302reader", "Lock Card"))
        self.label_2.setText(_translate("d302reader", "Client ID"))
        self.label_4.setText(_translate("d302reader", "Number"))
        self.text_d10_clientid.setInputMask(_translate("d302reader", "000"))
        self.text_d10_numbers.setInputMask(_translate("d302reader", "0000000000"))
        self.label_3.setText(_translate("d302reader", "1-255"))
        self.label_5.setText(_translate("d302reader", "0-4294967295"))
        self.label_6.setText(_translate("d302reader", "Client ID"))
        self.label_7.setText(_translate("d302reader", "FC"))
        self.label_11.setText(_translate("d302reader", "Number"))
        self.text_w26_clientid.setInputMask(_translate("d302reader", "000"))
        self.text_w26_fc.setInputMask(_translate("d302reader", "000"))
        self.text_w26_numbers.setInputMask(_translate("d302reader", "00000"))
        self.label_9.setText(_translate("d302reader", "1-255"))
        self.label_10.setText(_translate("d302reader", "1-255"))
        self.label_12.setText(_translate("d302reader", "1-65535"))
        self.btn_radio_w26.setText(_translate("d302reader", "W26 "))
        self.btn_radio_d10.setText(_translate("d302reader", "D10"))
