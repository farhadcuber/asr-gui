# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(501, 440)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalSlider = QtGui.QSlider(Form)
        self.horizontalSlider.setEnabled(True)
        self.horizontalSlider.setGeometry(QtCore.QRect(90, 90, 391, 29))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.playButton = QtGui.QPushButton(Form)
        self.playButton.setGeometry(QtCore.QRect(10, 90, 30, 30))
        self.playButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setIconSize(QtCore.QSize(25, 25))
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.textEdit = QtGui.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(10, 130, 481, 301))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.openButton = QtGui.QPushButton(Form)
        self.openButton.setGeometry(QtCore.QRect(90, 10, 71, 71))
        self.openButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/open.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.openButton.setIcon(icon1)
        self.openButton.setIconSize(QtCore.QSize(50, 50))
        self.openButton.setObjectName(_fromUtf8("openButton"))
        self.pauseButton = QtGui.QPushButton(Form)
        self.pauseButton.setGeometry(QtCore.QRect(50, 90, 30, 30))
        self.pauseButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icons/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon2)
        self.pauseButton.setIconSize(QtCore.QSize(25, 25))
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.recButton = QtGui.QPushButton(Form)
        self.recButton.setGeometry(QtCore.QRect(10, 10, 71, 71))
        self.recButton.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icons/record-512.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.recButton.setIcon(icon3)
        self.recButton.setIconSize(QtCore.QSize(50, 50))
        self.recButton.setObjectName(_fromUtf8("recButton"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(400, 10, 71, 71))
        self.pushButton.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icons/transcribe.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QtCore.QSize(50, 50))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "SCL Persian Speech Recognizer", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

