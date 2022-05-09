# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proto2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_pdf = QtWidgets.QPushButton(self.centralwidget)
        self.open_pdf.setGeometry(QtCore.QRect(190, 60, 181, 131))
        self.open_pdf.setStyleSheet("background: rgb(170, 170, 255);\n"
"font: 9pt \"Poppins\";\n"
"color: white;\n"
"border-radius:10px;")
        self.open_pdf.setObjectName("open_pdf")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 120, 31, 21))
        self.label.setStyleSheet("color: rgb(95,70,200);\n"
"font: 9pt \"Poppins\";")
        self.label.setObjectName("label")
        self.exportPDFbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exportPDFbutton.setGeometry(QtCore.QRect(370, 510, 111, 31))
        self.exportPDFbutton.setStyleSheet("background-color: rgb(170, 170, 255);\n"
"font: 9pt \"Poppins\";\n"
"color: white;\n"
"border-radius:10px;")
        self.exportPDFbutton.setObjectName("exportPDFbutton")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(300, 250, 251, 41))
        self.convertButton.setStyleSheet("background-color: rgb(95,70,200);\n"
"font: 9pt \"Poppins\";\n"
"color: white;\n"
"border-radius:10px;")
        self.convertButton.setObjectName("convertButton")
        self.outputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTextField.setEnabled(True)
        self.outputTextField.setGeometry(QtCore.QRect(480, 60, 211, 131))
        self.outputTextField.setAutoFillBackground(False)
        self.outputTextField.setStyleSheet("\n"
"border-radius: 100px;")
        self.outputTextField.setObjectName("outputTextField")
        self.inputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.inputTextField.setGeometry(QtCore.QRect(160, 310, 531, 141))
        self.inputTextField.setObjectName("inputTextField")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 350, 49, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(170, 320, 49, 16))
        self.label_3.setStyleSheet("font: 300 8pt \"Poppins\";\n"
"")
        self.label_3.setObjectName("label_3")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(660, 70, 20, 111))
        self.verticalScrollBar.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background:rgb(225, 235, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(170, 176, 255);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(170, 176, 255);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(170, 176, 255);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(490, 70, 161, 16))
        self.label_5.setStyleSheet("font: 300 8pt \"Poppins\";")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(360, 210, 131, 22))
        self.comboBox.setStyleSheet("font: 300 8pt \"Poppins\";\n"
"border-radius: 5px;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.fontComboBox = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontComboBox.setGeometry(QtCore.QRect(180, 470, 131, 22))
        self.fontComboBox.setStyleSheet("\n"
"border-radius: 5px;")
        self.fontComboBox.setObjectName("fontComboBox")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(360, 470, 131, 21))
        self.lineEdit.setStyleSheet("font: 300 8pt \"Poppins\";\n"
"border-radius: 5px;\n"
"colour: grey;")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(660, 320, 20, 121))
        self.verticalScrollBar_2.setStyleSheet("/* VERTICAL SCROLLBAR */\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background:rgb(225, 235, 255);\n"
"    width: 14px;\n"
"    margin: 15px 0 15px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"\n"
"/*  HANDLE BAR VERTICAL */\n"
"QScrollBar::handle:vertical {    \n"
"    background-color: rgb(170, 176, 255);\n"
"    min-height: 30px;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"\n"
"/* BTN TOP - SCROLLBAR */\n"
"QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(170, 176, 255);\n"
"    height: 15px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"\n"
"/* BTN BOTTOM - SCROLLBAR */\n"
"QScrollBar::add-line:vertical {\n"
"    border: none;\n"
"    background-color: rgb(170, 176, 255);\n"
"    height: 15px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"/* RESET ARROW */\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background: none;\n"
"}\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(530, 470, 131, 22))
        self.comboBox_2.setStyleSheet("font: 300 8pt \"Poppins\";\n"
"border-radius: 5px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave_Export = QtWidgets.QAction(MainWindow)
        self.actionSave_Export.setObjectName("actionSave_Export")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_Export)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_pdf.setText(_translate("MainWindow", "Select PDF"))
        self.label.setText(_translate("MainWindow", "OR"))
        self.exportPDFbutton.setText(_translate("MainWindow", "Export PDF"))
        self.convertButton.setText(_translate("MainWindow", "CONVERT"))
        self.label_3.setText(_translate("MainWindow", "Result"))
        self.label_5.setText(_translate("MainWindow", "Paste text"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Summarise"))
        self.comboBox.setItemText(1, _translate("MainWindow", "20%"))
        self.comboBox.setItemText(2, _translate("MainWindow", "50%"))
        self.comboBox.setItemText(3, _translate("MainWindow", "70%"))
        self.lineEdit.setText(_translate("MainWindow", "Rename PDF"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Font Size"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "2"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "3"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "4"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "5"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "6"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "7"))
        self.comboBox_2.setItemText(8, _translate("MainWindow", "8"))
        self.comboBox_2.setItemText(9, _translate("MainWindow", "9"))
        self.comboBox_2.setItemText(10, _translate("MainWindow", "10"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "open a pdf file or text file"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave_Export.setText(_translate("MainWindow", "Save/Export"))
        self.actionSave_Export.setStatusTip(_translate("MainWindow", "save the file"))
        self.actionSave_Export.setShortcut(_translate("MainWindow", "Ctrl+S"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
