from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QFileInfo
from try_mini.prototypes import pdf2, python2
from fpdf import FPDF


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 620)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
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
        self.inputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.inputTextField.setEnabled(True)
        self.inputTextField.setGeometry(QtCore.QRect(480, 60, 211, 131))
        self.inputTextField.setAutoFillBackground(False)
        self.inputTextField.setStyleSheet("")
        self.inputTextField.setObjectName("inputTextField")
        self.outputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTextField.setGeometry(QtCore.QRect(160, 310, 531, 141))
        self.outputTextField.setObjectName("outputTextField")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 350, 49, 16))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.summaryLength = QtWidgets.QComboBox(self.centralwidget)
        self.summaryLength.setGeometry(QtCore.QRect(360, 210, 131, 22))
        self.summaryLength.setStyleSheet("font: 300 8pt \"Poppins\";\n"
                                         "border-radius: 5px;")
        self.summaryLength.setObjectName("summaryLength")
        self.summaryLength.addItem("")
        self.summaryLength.addItem("")
        self.summaryLength.addItem("")
        self.summaryLength.addItem("")
        self.fontType = QtWidgets.QFontComboBox(self.centralwidget)
        self.fontType.setGeometry(QtCore.QRect(240, 470, 131, 22))
        self.fontType.setStyleSheet("\n"
                                    "border-radius: 5px;")
        self.fontType.setObjectName("fontType")
        self.fontSize = QtWidgets.QComboBox(self.centralwidget)
        self.fontSize.setGeometry(QtCore.QRect(480, 470, 131, 22))
        self.fontSize.setStyleSheet("font: 300 8pt \"Poppins\";\n"
                                    "border-radius: 5px;")
        self.fontSize.setObjectName("fontSize")
        self.fontSize.addItem("")
        self.fontSize.addItem("")
        self.fontSize.addItem("")
        self.fontSize.addItem("")
        self.fontSize.addItem("")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(170, 10, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.errorLabel.setFont(font)
        self.errorLabel.setStyleSheet("color: rgb(224, 27, 36);")
        self.errorLabel.setText("")
        self.errorLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.errorLabel.setObjectName("errorLabel")
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

        self.actionOpen.triggered.connect(self.openFile)
        self.open_pdf.clicked.connect(self.openFile)

        self.convertButton.clicked.connect(self.convertText)

        self.exportPDFbutton.clicked.connect(self.pdfExport)

    def convertText(self):
        if self.inputTextField.toPlainText() == '':
            self.errorLabel.setText("Input Text is empty !")
        else:
            txt = self.inputTextField.toPlainText()
            self.ouputText = python2.summaryText(txt)
            self.outputTextField.setText(self.ouputText)

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
                python2.summaryText(text)
                self.outputTextField.setText(python2.summaryText(text))
            elif filename.endswith('.txt'):
                python2.summary(filename)
                self.outputTextField.setText(python2.summary(filename))
            else:
                self.outputTextField.setText("Invalid file type")

            # try:
            #     with open(filename, 'r') as fh:
            #         pdf2.pdf_to_txt(fh)
            # except Exception as e:
            #     # Errata:  Book contains the following line:
            #     # qtw.QMessageBox.critical(f"Could not load file: {e}")
            #     # It should read like this:
            #     QtWidgets.QMessageBox.critical(self, f"Could not load file: {e}")

    def export_to_pdf(self):
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=14)
        # add another cell
        pdf.multi_cell(w=0, txt=self.ouputText, border=0,
                       align='L', max_line_height=pdf.font_size, fill=False)
        # save the pdf with name .pdf
        pdf.output("GFG.pdf")
        # # doc = aw.Document("document.txt")
        # doc = self.ouputText
        # # save TXT as PDF file
        # doc.save("txt-to-pdf.pdf", aw..PDF)

    def pdfExport(self):
        if self.outputTextField.toPlainText() == '' or self.fontSize.currentText() == "Font Size":
            if self.fontSize.currentText() == "Font Size":
                self.errorLabel.setText("Please select Font Size")
            else:
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
        self.label.setText(_translate("MainWindow", "OR"))
        self.exportPDFbutton.setText(_translate("MainWindow", "Export PDF"))
        self.convertButton.setText(_translate("MainWindow", "CONVERT"))
        self.summaryLength.setItemText(0, _translate("MainWindow", "Summarise"))
        self.summaryLength.setItemText(1, _translate("MainWindow", "20%"))
        self.summaryLength.setItemText(2, _translate("MainWindow", "50%"))
        self.summaryLength.setItemText(3, _translate("MainWindow", "70%"))
        self.fontSize.setItemText(0, _translate("MainWindow", "Font Size"))
        self.fontSize.setItemText(1, _translate("MainWindow", "10"))
        self.fontSize.setItemText(2, _translate("MainWindow", "12"))
        self.fontSize.setItemText(3, _translate("MainWindow", "14"))
        self.fontSize.setItemText(4, _translate("MainWindow", "16"))
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
