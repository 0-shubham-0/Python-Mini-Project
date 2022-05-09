from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QFileInfo
from try_mini import pdf2, python2


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 610)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_pdf = QtWidgets.QPushButton(self.centralwidget)
        self.open_pdf.setGeometry(QtCore.QRect(190, 60, 181, 131))
        self.open_pdf.setStyleSheet("background: rgb(170, 170, 255);\n"
                                    "font: 9pt \"Poppins\";\n"
                                    "color: white;\n"
                                    "border-radius:10px;")
        self.open_pdf.setAutoDefault(False)
        self.open_pdf.setDefault(False)
        self.open_pdf.setObjectName("open_pdf")
        self.orLabel = QtWidgets.QLabel(self.centralwidget)
        self.orLabel.setGeometry(QtCore.QRect(420, 120, 21, 21))
        self.orLabel.setStyleSheet("color: rgb(95,70,200);\n"
                                   "font: 9pt \"Poppins\";")
        self.orLabel.setObjectName("orLabel")
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
        self.inputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.inputTextField.setEnabled(True)
        self.inputTextField.setGeometry(QtCore.QRect(480, 60, 211, 131))
        self.inputTextField.setAutoFillBackground(False)
        self.inputTextField.setStyleSheet("")
        self.inputTextField.setObjectName("inputTextField")
        self.outputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTextField.setGeometry(QtCore.QRect(160, 310, 531, 141))
        self.outputTextField.setObjectName("outputTextField")
        self.summaryLength = QtWidgets.QComboBox(self.centralwidget)
        self.summaryLength.setGeometry(QtCore.QRect(440, 210, 131, 22))
        self.summaryLength.setStyleSheet("font: 300 8pt \"Poppins\";\n"
                                         "border-radius: 5px;")
        self.summaryLength.setObjectName("summaryLength")
        self.summaryLength.addItem("")
        self.summaryLength.addItem("")
        self.summaryLength.addItem("")
        self.fontType = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontType.setGeometry(QtCore.QRect(290, 470, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        self.fontType.setFont(font)
        self.fontType.setStyleSheet("\n"
                                    "border-radius: 5px;")
        self.fontType.setObjectName("fontType")
        self.fontSize = QtWidgets.QComboBox(self.centralwidget)
        self.fontSize.setGeometry(QtCore.QRect(530, 470, 131, 22))
        self.fontSize.setStyleSheet("font: 300 8pt \"Poppins\";\n"
                                    "border-radius: 5px;")
        self.fontSize.setObjectName("fontSize")
        self.fontSize.addItem("")
        self.fontSize.addItem("")
        self.fontSize.addItem("")
        self.fontSize.addItem("")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(170, 10, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(224, 27, 36);")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
        self.lengthLabel = QtWidgets.QLabel(self.centralwidget)
        self.lengthLabel.setGeometry(QtCore.QRect(288, 210, 135, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.lengthLabel.setFont(font)
        self.lengthLabel.setObjectName("lengthLabel")
        self.fontTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.fontTypeLabel.setGeometry(QtCore.QRect(188, 470, 90, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.fontTypeLabel.setFont(font)
        self.fontTypeLabel.setObjectName("fontTypeLabel")
        self.FontSizeLabel = QtWidgets.QLabel(self.centralwidget)
        self.FontSizeLabel.setGeometry(QtCore.QRect(458, 470, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.FontSizeLabel.setFont(font)
        self.FontSizeLabel.setObjectName("FontSizeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 26))
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

        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave_Export.triggered.connect(self.pdfExport)
        self.open_pdf.clicked.connect(self.openFile)

        self.convertButton.clicked.connect(self.convertText)

        self.exportPDFbutton.clicked.connect(self.pdfExport)

    def openFile(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(
            self,
            "Select a text file to open…",
            QtCore.QDir.homePath(),
            'Text Files (*.txt) ;;Pdf Files (*.pdf) ;;All Files (*)',
            'Python Files (*.py)',
            QtWidgets.QFileDialog.DontUseNativeDialog |
            QtWidgets.QFileDialog.DontResolveSymlinks
        )
        if filename:
            print(filename)
            if filename.endswith('.pdf'):
                text = pdf2.pdf_to_txt(filename)
                self.inputTextField.setText(text)
            elif filename.endswith('.txt'):
                scraped_data = open(filename, 'r')
                article = scraped_data.read()
                self.inputTextField.setText(article)
            else:
                self.outputTextField.setText("Invalid file type")

    def convertText(self):
        if self.inputTextField.toPlainText() == '':
            self.errorLabel.setText("Input Text is empty !")
        else:
            txt = self.inputTextField.toPlainText()
            self.ouputText = python2.summaryText(txt, self.summaryLength.currentText())
            self.outputTextField.setText(self.ouputText)


    def pdfExport(self):
        if self.outputTextField.toPlainText() == '':
            self.errorLabel.setText("Summary not generated !")
        else:
            fn, _ = QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All Files()")

            if fn != '':

                if QFileInfo(fn).suffix() == "": fn += '.pdf'

                font = QtGui.QFont()
                font.setPointSize(int(self.fontSize.currentText()))
                font.setFamily(self.fontType.currentText())
                self.outputTextField.setFont(font)

                printer = QPrinter(QPrinter.HighResolution)
                printer.setOutputFormat(QPrinter.PdfFormat)
                printer.setOutputFileName(fn)
                self.outputTextField.document().print_(printer)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_pdf.setText(_translate("MainWindow", "Select PDF"))
        self.orLabel.setText(_translate("MainWindow", "OR"))
        self.exportPDFbutton.setText(_translate("MainWindow", "Export PDF"))
        self.convertButton.setText(_translate("MainWindow", "CONVERT"))
        self.summaryLength.setItemText(0, _translate("MainWindow", "30%"))
        self.summaryLength.setItemText(1, _translate("MainWindow", "50%"))
        self.summaryLength.setItemText(2, _translate("MainWindow", "70%"))
        self.fontSize.setItemText(0, _translate("MainWindow", "10"))
        self.fontSize.setItemText(1, _translate("MainWindow", "12"))
        self.fontSize.setItemText(2, _translate("MainWindow", "14"))
        self.fontSize.setItemText(3, _translate("MainWindow", "16"))
        self.lengthLabel.setText(_translate("MainWindow", "Summary Length"))
        self.fontTypeLabel.setText(_translate("MainWindow", "Font Type"))
        self.FontSizeLabel.setText(_translate("MainWindow", "Font Size"))
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