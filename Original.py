# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI02.ui'
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

class Ui_GuiHand(object):
    def setupUi(self, GuiHand):
        GuiHand.setObjectName(_fromUtf8("GuiHand"))
        GuiHand.resize(713, 573)
        self.buttonBox = QtGui.QDialogButtonBox(GuiHand)
        self.buttonBox.setGeometry(QtCore.QRect(10, 520, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayoutWidget = QtGui.QWidget(GuiHand)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 20, 171, 471))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.graphicsView = QtGui.QGraphicsView(GuiHand)
        self.graphicsView.setGeometry(QtCore.QRect(230, 20, 471, 471))
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.line = QtGui.QFrame(GuiHand)
        self.line.setGeometry(QtCore.QRect(200, 20, 20, 481))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(GuiHand)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), GuiHand.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), GuiHand.reject)
        QtCore.QMetaObject.connectSlotsByName(GuiHand)

    def retranslateUi(self, GuiHand):
        GuiHand.setWindowTitle(_translate("GuiHand", "Dialog", None))

