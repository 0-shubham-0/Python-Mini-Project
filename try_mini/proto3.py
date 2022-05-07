# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'proto1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from try_mini import pdf2, python1, python2
import aspose as aw
from fpdf import FPDF


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.open_pdf = QtWidgets.QPushButton(self.centralwidget)
        self.open_pdf.setGeometry(QtCore.QRect(130, 140, 75, 24))
        self.open_pdf.setObjectName("open_pdf")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 150, 49, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 50, 141, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 270, 49, 16))
        self.label_3.setObjectName("label_3")
        self.exportPDFbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exportPDFbutton.setGeometry(QtCore.QRect(580, 400, 101, 41))
        self.exportPDFbutton.setObjectName("exportPDFbutton")
        self.convertButton = QtWidgets.QPushButton(self.centralwidget)
        self.convertButton.setGeometry(QtCore.QRect(330, 210, 89, 25))
        self.convertButton.setObjectName("convertButton")
        self.outputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.outputTextField.setGeometry(QtCore.QRect(60, 320, 351, 211))
        self.outputTextField.setObjectName("outputTextField")
        self.outputTextField.setPlaceholderText("Output will be displayed here ...")
        self.outputTextField.setReadOnly(True)
        self.inputTextField = QtWidgets.QTextEdit(self.centralwidget)
        self.inputTextField.setGeometry(QtCore.QRect(470, 50, 321, 241))
        self.inputTextField.setObjectName("inputTextField")
        self.inputTextField.setPlaceholderText("Enter your text here ...")
        self.inputTextField.setAcceptRichText(False)
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

        self.exportPDFbutton.clicked.connect(self.export_to_pdf)

    # def storeSummary(self):
    #     self.outputTextField = python2.su

    def convertText(self):
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_pdf.setText(_translate("MainWindow", "Open pdf"))
        self.label.setText(_translate("MainWindow", "OR"))
        self.label_2.setText(_translate("MainWindow", "Input Pdf or Paste text"))
        self.label_3.setText(_translate("MainWindow", "Output"))
        self.exportPDFbutton.setText(_translate("MainWindow", "Export as pdf"))
        self.convertButton.setText(_translate("MainWindow", "Convert"))
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
