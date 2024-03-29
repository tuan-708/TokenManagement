# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1236, 657)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GBox = QtWidgets.QGroupBox(self.centralwidget)
        self.GBox.setGeometry(QtCore.QRect(10, 10, 1211, 611))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.GBox.setFont(font)
        self.GBox.setObjectName("GBox")
        self.lbMang = QtWidgets.QLabel(self.GBox)
        self.lbMang.setGeometry(QtCore.QRect(20, 30, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lbMang.setFont(font)
        self.lbMang.setObjectName("lbMang")
        self.rb_Bsc = QtWidgets.QRadioButton(self.GBox)
        self.rb_Bsc.setGeometry(QtCore.QRect(90, 30, 110, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rb_Bsc.setFont(font)
        self.rb_Bsc.setChecked(True)
        self.rb_Bsc.setObjectName("rb_Bsc")
        self.rb_Eth = QtWidgets.QRadioButton(self.GBox)
        self.rb_Eth.setGeometry(QtCore.QRect(160, 30, 110, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rb_Eth.setFont(font)
        self.rb_Eth.setObjectName("rb_Eth")
        self.rb_Sol = QtWidgets.QRadioButton(self.GBox)
        self.rb_Sol.setGeometry(QtCore.QRect(230, 30, 110, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rb_Sol.setFont(font)
        self.rb_Sol.setObjectName("rb_Sol")
        self.rb_Polygon = QtWidgets.QRadioButton(self.GBox)
        self.rb_Polygon.setGeometry(QtCore.QRect(300, 30, 110, 24))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.rb_Polygon.setFont(font)
        self.rb_Polygon.setObjectName("rb_Polygon")
        self.line1 = QtWidgets.QFrame(self.GBox)
        self.line1.setGeometry(QtCore.QRect(20, 70, 831, 16))
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line1.setObjectName("line1")
        self.lb_1 = QtWidgets.QLabel(self.GBox)
        self.lb_1.setGeometry(QtCore.QRect(20, 100, 101, 20))
        self.lb_1.setObjectName("lb_1")
        self.bt_GomToken = QtWidgets.QPushButton(self.GBox)
        self.bt_GomToken.setGeometry(QtCore.QRect(120, 100, 93, 29))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.bt_GomToken.setFont(font)
        self.bt_GomToken.setObjectName("bt_GomToken")
        self.label_3 = QtWidgets.QLabel(self.GBox)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 81, 20))
        self.label_3.setObjectName("label_3")
        self.input_Address = QtWidgets.QLineEdit(self.GBox)
        self.input_Address.setGeometry(QtCore.QRect(120, 150, 221, 21))
        self.input_Address.setObjectName("input_Address")
        self.label_4 = QtWidgets.QLabel(self.GBox)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 101, 20))
        self.label_4.setObjectName("label_4")
        self.input_PrivateKey = QtWidgets.QLineEdit(self.GBox)
        self.input_PrivateKey.setGeometry(QtCore.QRect(120, 180, 221, 21))
        self.input_PrivateKey.setObjectName("input_PrivateKey")
        self.lb_2 = QtWidgets.QLabel(self.GBox)
        self.lb_2.setGeometry(QtCore.QRect(350, 90, 63, 20))
        self.lb_2.setObjectName("lb_2")
        self.list_Token = QtWidgets.QListWidget(self.GBox)
        self.list_Token.setGeometry(QtCore.QRect(390, 80, 191, 161))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.list_Token.setFont(font)
        self.list_Token.setObjectName("list_Token")
        self.lb_TokenHold = QtWidgets.QLabel(self.GBox)
        self.lb_TokenHold.setGeometry(QtCore.QRect(620, 90, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_TokenHold.setFont(font)
        self.lb_TokenHold.setObjectName("lb_TokenHold")
        self.lb_NumberTokensHold = QtWidgets.QLabel(self.GBox)
        self.lb_NumberTokensHold.setGeometry(QtCore.QRect(720, 90, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_NumberTokensHold.setFont(font)
        self.lb_NumberTokensHold.setObjectName("lb_NumberTokensHold")
        self.lb_AmountToken = QtWidgets.QLabel(self.GBox)
        self.lb_AmountToken.setGeometry(QtCore.QRect(620, 130, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_AmountToken.setFont(font)
        self.lb_AmountToken.setObjectName("lb_AmountToken")
        self.lb_AmountTokenHold = QtWidgets.QLabel(self.GBox)
        self.lb_AmountTokenHold.setGeometry(QtCore.QRect(720, 130, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_AmountTokenHold.setFont(font)
        self.lb_AmountTokenHold.setObjectName("lb_AmountTokenHold")
        self.line2 = QtWidgets.QFrame(self.GBox)
        self.line2.setGeometry(QtCore.QRect(20, 240, 831, 20))
        self.line2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line2.setObjectName("line2")
        self.lb_3 = QtWidgets.QLabel(self.GBox)
        self.lb_3.setGeometry(QtCore.QRect(20, 270, 101, 20))
        self.lb_3.setObjectName("lb_3")
        self.cb_Function = QtWidgets.QComboBox(self.GBox)
        self.cb_Function.setGeometry(QtCore.QRect(130, 270, 151, 26))
        self.cb_Function.setObjectName("cb_Function")
        self.cb_Function.addItem("")
        self.cb_Function.addItem("")
        self.cb_Tokens = QtWidgets.QComboBox(self.GBox)
        self.cb_Tokens.setGeometry(QtCore.QRect(300, 270, 80, 26))
        self.cb_Tokens.setObjectName("cb_Tokens")
        self.cb_Tokens.addItem("")
        self.cb_Tokens.addItem("")
        self.cb_Tokens.addItem("")
        self.cb_Tokens.addItem("")
        self.lb_ListAddress = QtWidgets.QLabel(self.GBox)
        self.lb_ListAddress.setGeometry(QtCore.QRect(390, 280, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_ListAddress.setFont(font)
        self.lb_ListAddress.setObjectName("lb_ListAddress")
        self.list_Address = QtWidgets.QListWidget(self.GBox)
        self.list_Address.setGeometry(QtCore.QRect(550, 260, 301, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.list_Address.setFont(font)
        self.list_Address.setObjectName("list_Address")
        self.lb_Address = QtWidgets.QLabel(self.GBox)
        self.lb_Address.setGeometry(QtCore.QRect(20, 310, 81, 20))
        self.lb_Address.setObjectName("lb_Address")
        self.input_Address1 = QtWidgets.QLineEdit(self.GBox)
        self.input_Address1.setGeometry(QtCore.QRect(130, 310, 221, 21))
        self.input_Address1.setObjectName("input_Address1")
        self.label_13 = QtWidgets.QLabel(self.GBox)
        self.label_13.setGeometry(QtCore.QRect(20, 350, 101, 20))
        self.label_13.setObjectName("label_13")
        self.input_PrivateKey1 = QtWidgets.QLineEdit(self.GBox)
        self.input_PrivateKey1.setGeometry(QtCore.QRect(130, 350, 221, 21))
        self.input_PrivateKey1.setObjectName("input_PrivateKey1")
        self.lb_Amount = QtWidgets.QLabel(self.GBox)
        self.lb_Amount.setGeometry(QtCore.QRect(390, 350, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_Amount.setFont(font)
        self.lb_Amount.setObjectName("lb_Amount")
        self.lb_AmountAddress = QtWidgets.QLabel(self.GBox)
        self.lb_AmountAddress.setGeometry(QtCore.QRect(480, 350, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.lb_AmountAddress.setFont(font)
        self.lb_AmountAddress.setObjectName("lb_AmountAddress")
        self.label_16 = QtWidgets.QLabel(self.GBox)
        self.label_16.setGeometry(QtCore.QRect(20, 390, 101, 20))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.GBox)
        self.label_17.setGeometry(QtCore.QRect(260, 390, 63, 20))
        self.label_17.setObjectName("label_17")
        self.gasFee = QtWidgets.QLineEdit(self.GBox)
        self.gasFee.setGeometry(QtCore.QRect(340, 390, 91, 21))
        self.gasFee.setObjectName("gasFee")
        self.line4 = QtWidgets.QFrame(self.GBox)
        self.line4.setGeometry(QtCore.QRect(863, 20, 20, 561))
        self.line4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line4.setObjectName("line4")
        self.btExecute = QtWidgets.QPushButton(self.GBox)
        self.btExecute.setGeometry(QtCore.QRect(20, 430, 93, 29))
        self.btExecute.setObjectName("btExecute")
        self.btOpenRecipient = QtWidgets.QPushButton(self.GBox)
        self.btOpenRecipient.setGeometry(QtCore.QRect(130, 430, 141, 29))
        self.btOpenRecipient.setObjectName("btOpenRecipient")
        self.bt_OpenData = QtWidgets.QPushButton(self.GBox)
        self.bt_OpenData.setGeometry(QtCore.QRect(730, 20, 121, 29))
        self.bt_OpenData.setObjectName("bt_OpenData")
        self.line3 = QtWidgets.QFrame(self.GBox)
        self.line3.setGeometry(QtCore.QRect(20, 490, 831, 16))
        self.line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line3.setObjectName("line3")
        self.label_18 = QtWidgets.QLabel(self.GBox)
        self.label_18.setGeometry(QtCore.QRect(20, 520, 101, 20))
        self.label_18.setObjectName("label_18")
        self.btReset = QtWidgets.QPushButton(self.GBox)
        self.btReset.setGeometry(QtCore.QRect(130, 520, 93, 29))
        self.btReset.setObjectName("btReset")
        self.cbReset = QtWidgets.QComboBox(self.GBox)
        self.cbReset.setGeometry(QtCore.QRect(240, 520, 111, 26))
        self.cbReset.setObjectName("cbReset")
        self.cbReset.addItem("")
        self.cbReset.addItem("")
        self.cbReset.addItem("")
        self.cbReset.addItem("")
        self.cbReset.addItem("")
        self.lbStatusProcess = QtWidgets.QLabel(self.GBox)
        self.lbStatusProcess.setGeometry(QtCore.QRect(20, 560, 81, 20))
        self.lbStatusProcess.setObjectName("lbStatusProcess")
        self.progressBar = QtWidgets.QProgressBar(self.GBox)
        self.progressBar.setGeometry(QtCore.QRect(130, 563, 671, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.lb_AvatarBio = QtWidgets.QLabel(self.GBox)
        self.lb_AvatarBio.setGeometry(QtCore.QRect(880, 30, 331, 561))
        self.lb_AvatarBio.setStyleSheet("image: url(./image/bio.jpg);")
        self.lb_AvatarBio.setObjectName("lb_AvatarBio")
        self.btExport = QtWidgets.QPushButton(self.GBox)
        self.btExport.setGeometry(QtCore.QRect(620, 20, 93, 29))
        self.btExport.setObjectName("btExport")
        self.bt_ExportTranfers = QtWidgets.QPushButton(self.GBox)
        self.bt_ExportTranfers.setGeometry(QtCore.QRect(230, 100, 93, 29))
        self.bt_ExportTranfers.setObjectName("bt_ExportTranfers")
        self.AmountTranfers = QtWidgets.QLineEdit(self.GBox)
        self.AmountTranfers.setGeometry(QtCore.QRect(130, 390, 91, 21))
        self.AmountTranfers.setObjectName("AmountTranfers")
        self.inputTokenContract = QtWidgets.QLineEdit(self.GBox)
        self.inputTokenContract.setGeometry(QtCore.QRect(700, 170, 161, 21))
        self.inputTokenContract.setObjectName("inputTokenContract")
        self.label = QtWidgets.QLabel(self.GBox)
        self.label.setGeometry(QtCore.QRect(620, 170, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.GBox)
        self.label_2.setGeometry(QtCore.QRect(390, 310, 63, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lb_NameToken = QtWidgets.QLabel(self.GBox)
        self.lb_NameToken.setGeometry(QtCore.QRect(440, 310, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.lb_NameToken.setFont(font)
        self.lb_NameToken.setText("")
        self.lb_NameToken.setObjectName("lb_NameToken")
        self.label_5 = QtWidgets.QLabel(self.GBox)
        self.label_5.setGeometry(QtCore.QRect(550, 520, 63, 20))
        self.label_5.setObjectName("label_5")
        self.cbCreateWallet = QtWidgets.QComboBox(self.GBox)
        self.cbCreateWallet.setGeometry(QtCore.QRect(740, 520, 111, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cbCreateWallet.setFont(font)
        self.cbCreateWallet.setObjectName("cbCreateWallet")
        self.cbCreateWallet.addItem("")
        self.cbCreateWallet.addItem("")
        self.btCreateWallet = QtWidgets.QPushButton(self.GBox)
        self.btCreateWallet.setGeometry(QtCore.QRect(620, 520, 93, 29))
        self.btCreateWallet.setObjectName("btCreateWallet")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1236, 26))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuSetting.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Token App 1.0"))
        self.GBox.setTitle(_translate("MainWindow", "Chương trình"))
        self.lbMang.setText(_translate("MainWindow", "Mạng:"))
        self.rb_Bsc.setText(_translate("MainWindow", "Bsc"))
        self.rb_Eth.setText(_translate("MainWindow", "Eth"))
        self.rb_Sol.setText(_translate("MainWindow", "Sol"))
        self.rb_Polygon.setText(_translate("MainWindow", "Polygon"))
        self.lb_1.setText(_translate("MainWindow", "Chức năng:"))
        self.bt_GomToken.setText(_translate("MainWindow", "Gom Token"))
        self.label_3.setText(_translate("MainWindow", "Address:"))
        self.label_4.setText(_translate("MainWindow", "Private Key:"))
        self.lb_2.setText(_translate("MainWindow", "List:"))
        self.lb_TokenHold.setText(_translate("MainWindow", "Số Token:"))
        self.lb_NumberTokensHold.setText(_translate("MainWindow", "0"))
        self.lb_AmountToken.setText(_translate("MainWindow", "Số lượng:"))
        self.lb_AmountTokenHold.setText(_translate("MainWindow", "0"))
        self.lb_3.setText(_translate("MainWindow", "Chức năng:"))
        self.cb_Function.setItemText(0, _translate("MainWindow", "Chuyển Token"))
        self.cb_Function.setItemText(1, _translate("MainWindow", "Tạo giao dịch"))
        self.cb_Tokens.setItemText(0, _translate("MainWindow", "Bnb"))
        self.cb_Tokens.setItemText(1, _translate("MainWindow", "Eth"))
        self.cb_Tokens.setItemText(2, _translate("MainWindow", "Sol"))
        self.cb_Tokens.setItemText(3, _translate("MainWindow", "Polygon"))
        self.lb_ListAddress.setText(_translate("MainWindow", "List Address:"))
        self.lb_Address.setText(_translate("MainWindow", "Address:"))
        self.label_13.setText(_translate("MainWindow", "Private Key:"))
        self.lb_Amount.setText(_translate("MainWindow", "Số lượng:"))
        self.lb_AmountAddress.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "SL Chuyển:"))
        self.label_17.setText(_translate("MainWindow", "Gas fee:"))
        self.btExecute.setText(_translate("MainWindow", "Thực thi"))
        self.btOpenRecipient.setText(_translate("MainWindow", "Mở file Recipient"))
        self.bt_OpenData.setText(_translate("MainWindow", "Mở file Data"))
        self.label_18.setText(_translate("MainWindow", "Chức năng:"))
        self.btReset.setText(_translate("MainWindow", "Reset"))
        self.cbReset.setItemText(0, _translate("MainWindow", "All File"))
        self.cbReset.setItemText(1, _translate("MainWindow", "File Bsc"))
        self.cbReset.setItemText(2, _translate("MainWindow", "File Eth"))
        self.cbReset.setItemText(3, _translate("MainWindow", "File Sol"))
        self.cbReset.setItemText(4, _translate("MainWindow", "File Polygon"))
        self.lbStatusProcess.setText(_translate("MainWindow", "Running:"))
        self.lb_AvatarBio.setText(_translate("MainWindow", "Avatar"))
        self.btExport.setText(_translate("MainWindow", "Export"))
        self.bt_ExportTranfers.setText(_translate("MainWindow", "Export"))
        self.label.setText(_translate("MainWindow", "Contract:"))
        self.label_2.setText(_translate("MainWindow", "Toke:"))
        self.label_5.setText(_translate("MainWindow", "Tạo ví:"))
        self.cbCreateWallet.setItemText(0, _translate("MainWindow", "Metamask"))
        self.cbCreateWallet.setItemText(1, _translate("MainWindow", "PhanTom"))
        self.btCreateWallet.setText(_translate("MainWindow", "Thực thi"))
        self.menuSetting.setTitle(_translate("MainWindow", "Setting"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
