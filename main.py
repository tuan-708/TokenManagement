import sys
import threading
from os import startfile
import click.exceptions
from excelFunction import ExcelManager
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QInputDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QGuiApplication
from form import Ui_MainWindow
from tokenFunction import scanTokenController
from createWallet import createMeatmask, createPhantom
from tokenTransaction.BSC import bscTransaction
from tokenTransaction.ETH import ethTransaction
from tokenTransaction.POLYGON import polygonTransaction


class MainWindow(QWidget):
    header = ("Address", "Sym", "Amount", "Contract", "PrivateKey")

    def __init__(self):
        super().__init__()
        self.ListBinance = None
        self.ListToken = None
        self.ItemSelected = None
        self.ListAddressTranfers = None
        self.dataTranfers = None
        self.listProfiles, self.LenDataFrame = None, None
        self.listProfiles, self.LenDataFrame = ExcelManager.getListDataExcel(f"excelManagment/Data.xlsx", "Sheet1")

        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.main_win.setWindowIcon(QtGui.QIcon(f'image\icon.png'))
        self.ListBinance = ExcelManager.readExcel(f"excelManagment/Bsc.xlsx")
        self.dataAccount = ExcelManager.redFileJson(f"mainAccount/account.json")

        # export các list token theo từng mạng
        self.uic.btExport.clicked.connect(self.ExportData)

        # mở file data
        self.uic.bt_OpenData.clicked.connect(self.clickedOpenData)

        # load data khi mở addrestranfers và load account
        if self.uic.rb_Bsc.isChecked():
            self.ListToken = sorted(set(self.ListBinance["Sym"]))
            for i in self.ListToken:
                self.uic.list_Token.addItem(i)
            self.loadAddressTranfers()
            self.loadAccount()

        # bắt event click bsc
        self.uic.rb_Bsc.toggled.connect(lambda: self.clickedRadiobuton(self.uic.rb_Bsc))
        # bắt event click eth
        self.uic.rb_Eth.toggled.connect(lambda: self.clickedRadiobuton(self.uic.rb_Eth))
        # bắt event click sol
        self.uic.rb_Sol.toggled.connect(lambda: self.clickedRadiobuton(self.uic.rb_Sol))
        # bắt event click polygon
        self.uic.rb_Polygon.toggled.connect(lambda: self.clickedRadiobuton(self.uic.rb_Polygon))

        # bắt event click vào token trong list
        self.uic.list_Token.itemClicked.connect(self.clickedToken)
        # bắt event click ExportTranter sang csv
        self.uic.bt_ExportTranfers.clicked.connect(self.clickedExportTranfers)
        # bắt event click button chuyển tiền chuyển các nagative token
        self.uic.btExecute.clicked.connect(self.tokenTransactions)
        # bắt event click vào tạo wallet
        self.uic.btCreateWallet.clicked.connect(self.CreateWallet)
        # bắt event ở file address
        self.uic.btOpenRecipient.clicked.connect(self.OpenRecipient)
        # thay đổi giá gas
        self.uic.cb_Tokens.currentTextChanged.connect(self.on_combobox_changed)
        # Gom token
        self.uic.bt_GomToken.clicked.connect(self.clickGomToken)

    def on_combobox_changed(self):
        if self.uic.cb_Tokens.currentText() == "Bnb":
            self.uic.gasFee.setText(self.dataAccount["feeBcs"])
        if self.uic.cb_Tokens.currentText() == "Eth":
            self.uic.gasFee.setText(self.dataAccount["feeEth"])
        if self.uic.cb_Tokens.currentText() == "Sol":
            self.uic.gasFee.setText(self.dataAccount["feeSol"])
        if self.uic.cb_Tokens.currentText() == "Polygon":
            self.uic.gasFee.setText(self.dataAccount["feePolygon"])

    def show(self):
        self.main_win.show()

    def ExportData(self):
        if self.uic.rb_Bsc.isChecked():
            self.uic.progressBar.setValue(0)
            listProfiles = self.listProfiles.copy()
            thread = threading.Thread(target=scanTokenController.scanTokenController, args=("Bsc", iter(listProfiles), self.LenDataFrame, self.uic.progressBar))
            thread.start()
        if self.uic.rb_Eth.isChecked():
            self.uic.progressBar.setValue(0)
            listProfiles1 = self.listProfiles.copy()
            thread = threading.Thread(target=scanTokenController.scanTokenController, args=("Eth", iter(listProfiles1), self.LenDataFrame, self.uic.progressBar))
            thread.start()
        if self.uic.rb_Sol.isChecked():
            self.uic.progressBar.setValue(0)
            thread = threading.Thread(target=scanTokenController.scanTokenController, args=("Sol", iter(self.listProfiles), self.LenDataFrame, self.uic.progressBar))
            thread.start()
        if self.uic.rb_Polygon.isChecked():
            self.uic.progressBar.setValue(0)
            thread = threading.Thread(target=scanTokenController.scanTokenController, args=("Polygon", iter(self.listProfiles), self.LenDataFrame, self.uic.progressBar))
            thread.start()

    def loadAccount(self):
        self.uic.input_Address.setText(self.dataAccount["Address"])
        self.uic.input_PrivateKey.setText(self.dataAccount["privateKey"])
        self.uic.input_Address1.setText(self.dataAccount["Address1"])
        self.uic.input_PrivateKey1.setText(self.dataAccount["privateKey1"])
        self.uic.gasFee.setText(str(self.dataAccount["feeBcs"]))

    def loadAddressTranfers(self):
        self.uic.list_Address.clear()
        self.dataTranfers = ExcelManager.readCsv(MainWindow.header, f"excelManagment/DataTranfers.csv")
        self.ListAddressTranfers = self.dataTranfers["Address"]
        if len(self.ListAddressTranfers) > 0:
            for j in self.ListAddressTranfers:
                self.uic.list_Address.addItem(j)
            self.uic.lb_AmountAddress.setText(str(len(self.ListAddressTranfers)))
            self.uic.lb_NameToken.setText(self.dataTranfers["Sym"][0])
        else:
            self.uic.lb_AmountAddress.setText(str(0))
            self.uic.lb_NameToken.setText("")

    def clickedRadiobuton(self, item):
        if item.text() == "Bsc":
            if item.isChecked():
                self.ListBinance = ExcelManager.readExcel(f"excelManagment/Bsc.xlsx")
                self.ListToken = sorted(set(self.ListBinance["Sym"]))
                self.uic.list_Token.clear()
                for i in self.ListToken:
                    self.uic.list_Token.addItem(i)
        if item.text() == "Eth":
            if item.isChecked():
                self.ListBinance = ExcelManager.readExcel(f"excelManagment/Eth.xlsx")
                self.ListToken = sorted(set(self.ListBinance["Sym"]))
                self.uic.list_Token.clear()
                for i in self.ListToken:
                    self.uic.list_Token.addItem(i)
        if item.text() == "Sol":
            if item.isChecked():
                self.ListBinance = ExcelManager.readExcel(f"excelManagment/Sol.xlsx")
                self.ListToken = sorted(set(self.ListBinance["Sym"]))
                self.uic.list_Token.clear()
                for i in self.ListToken:
                    self.uic.list_Token.addItem(i)
        if item.text() == "Polygon":
            if item.isChecked():
                self.ListBinance = ExcelManager.readExcel(f"excelManagment/Polygon.xlsx")
                self.ListToken = sorted(set(self.ListBinance["Sym"]))
                self.uic.list_Token.clear()
                for i in self.ListToken:
                    self.uic.list_Token.addItem(i)

    def clickedToken(self, item):
        token = item.text()
        self.ItemSelected = token
        self.uic.lb_TokenHold.setText(token+":")
        count = 0
        amount = 0
        listAmount = self.ListBinance["Amount"]
        listContract = self.ListBinance["Contract"]
        for index, item in enumerate(self.ListBinance["Sym"]):
            if item == token:
                if listAmount[index] > 0.0001:
                    count += 1
                    amount += listAmount[index]
                    contract = listContract[index]
                else:
                    contract = listContract[index]
        self.uic.lb_NumberTokensHold.setText(str(count))
        self.uic.lb_AmountTokenHold.setText(str(amount))
        self.uic.inputTokenContract.setText(contract)

    def clickedExportTranfers(self):
        listTokensExportTranfers = []
        if self.ItemSelected is None:
            self.ShowError("Cần chọn token!", "Thông báo")
        else:
            listAddress = self.ListBinance["Address"]
            listAmount = self.ListBinance["Amount"]
            listContract = self.ListBinance["Contract"]
            listPrivateKey = self.ListBinance["PrivateKey"]

            for index, item in enumerate(self.ListBinance["Sym"]):
                if item == self.ItemSelected:
                    if listAmount[index] > 0.0001:
                        account = (listAddress[index], item, listAmount[index], listContract[index], listPrivateKey[index])
                        listTokensExportTranfers.append(account)

            ExcelManager.writerCsv(MainWindow.header, listTokensExportTranfers, "excelManagment\DataTranfers.csv")
            self.ShowError("Export thành công v_v", "Thông báo")
            self.loadAddressTranfers()

    def tokenTransactions(self):
        try:
            float(self.uic.AmountTranfers.text())
            if self.uic.cb_Function.currentText() == "Chuyển Token":
                if self.uic.cb_Tokens.currentText() == "Bnb":
                    thread = threading.Thread(target=bscTransaction.bnbTransaction, args=(self.uic.input_Address1.text(), self.uic.input_PrivateKey1.text(),
                                                  self.uic.AmountTranfers.text(), self.uic.gasFee.text(),
                                                  self.dataTranfers, self.uic.progressBar,))
                    thread.start()
                if self.uic.cb_Tokens.currentText() == "Eth":
                    thread = threading.Thread(target=ethTransaction.ethTransaction, args=(self.uic.input_Address1.text(), self.uic.input_PrivateKey1.text(),
                                                  self.uic.AmountTranfers.text(), self.uic.gasFee.text(),
                                                  self.dataTranfers, self.uic.progressBar,))
                    thread.start()
                if self.uic.cb_Tokens.currentText() == "Polygon":
                    thread = threading.Thread(target=polygonTransaction.polygonTransaction, args=(self.uic.input_Address1.text(), self.uic.input_PrivateKey1.text(),
                                                self.uic.AmountTranfers.text(), self.uic.gasFee.text(), self.dataTranfers, self.uic.progressBar,))
                    thread.start()
        except Exception:
            self.ShowError("Nhập số lượng chuyển!!!", "Thông báo")

    def clickGomToken(self):
        if len(self.dataTranfers) == 0:
            self.ShowError("Không có token trong file", "Thông báo")
        thread = threading.Thread(target=bscTransaction.GomtokenTransaction, args=(self.dataTranfers,))
        thread.start()

    def OpenRecipient(self):
        try:
            startfile(f"excelManagment\DataTranfers.csv")
        except Exception:
            self.ShowError("Lỗi mở file", "Thông báo")

    def CreateWallet(self):
        if self.uic.cbCreateWallet.currentText() == "Metamask":
            inputDialog = QInputDialog(self.main_win)
            inputDialog.setInputMode(QInputDialog.TextInput)
            inputDialog.setLabelText("Nhập số lượng ví cần tạo: ")
            inputDialog.resize(200, 300)
            inputDialog.setWindowTitle("Nhập")
            oke = inputDialog.exec_()
            value = inputDialog.textValue()
            self.uic.progressBar.setValue(0)
            thread = threading.Thread(target=createMeatmask.walletMetamask, args=(value, self.uic.progressBar,))
            thread.start()
        else:
            self.uic.progressBar.setValue(0)
            thread = threading.Thread(target=createPhantom.walletPhantom, args=(self.uic.progressBar,))
            thread.start()

    def clickedOpenData(self):
        try:
            startfile(f"excelManagment\Data.xlsx")
        except Exception:
            self.ShowError("Lỗi mở file", "Thông báo")

    def ShowError(self, text, windowTitle):
        msg = QMessageBox(self.main_win)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle(windowTitle)
        msg.contextMenuPolicy()
        msg.exec_()


def app_aboutToQuit():
    answer = QMessageBox.question(main_win, 'Thoát', 'Bạn có muốn lưu Account không?', QMessageBox.No | QMessageBox.Yes)
    if answer == QtWidgets.QMessageBox.Yes:
        address = main_win.uic.input_Address.text().strip()
        privateKey = main_win.uic.input_PrivateKey.text().strip()
        address1 = main_win.uic.input_Address1.text().strip()
        privateKey1 = main_win.uic.input_PrivateKey1.text().strip()
        account = {'Address': address, 'privateKey': privateKey,
                   'Address1': address1, 'privateKey1': privateKey1,
                   'feeBcs': "10", 'feeEth': "10", 'feeSol': "3", 'feePolygon': "50"}
        ExcelManager.saveFileJson(f"mainAccount/account.json", account)
    else:
        account = {'Address': None, 'privateKey': None,
                   'Address1': None, 'privateKey1': None,
                   'feeBcs': "10", 'feeEth': "10", 'feeSol': "3", 'feePolygon': "50"}
        ExcelManager.saveFileJson(f"mainAccount/account.json", account)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(app_aboutToQuit)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
