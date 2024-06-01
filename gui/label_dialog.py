# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'label_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_label_dialog(object):
    def setupUi(self, label_dialog):
        script_path = os.path.abspath(__file__)
        script_dir = os.path.dirname(script_path)
        os.chdir(script_dir)
        label_dialog.setObjectName("label_dialog")
        label_dialog.resize(550, 400)
        label_dialog.setStyleSheet("QDialog{\n"
"    background-color: #fff;\n"
"}\n"
"QPushButton {\n"
"    background-color: #DBE2EF;\n"
"    color: #112D4E;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    width: 120px;\n"
"    height: 50px;\n"
"}\n"
"QPushButton:hover{\n"
"    color:  #fff;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(label_dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_label = QtWidgets.QLabel(label_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_label.sizePolicy().hasHeightForWidth())
        self.label_label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label_label.setFont(font)
        self.label_label.setAlignment(QtCore.Qt.AlignCenter)
        self.label_label.setObjectName("label_label")
        self.verticalLayout.addWidget(self.label_label, 0, QtCore.Qt.AlignHCenter)
        self.item_combo = QtWidgets.QComboBox(label_dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_combo.sizePolicy().hasHeightForWidth())
        self.item_combo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setKerning(False)
        self.item_combo.setFont(font)
        self.item_combo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_combo.setObjectName("item_combo")
        self.verticalLayout.addWidget(self.item_combo, 0, QtCore.Qt.AlignHCenter)
        self.label_button = QtWidgets.QPushButton(label_dialog)
        self.label_button.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Noto Sans KR")
        font.setPointSize(12)
        self.label_button.setFont(font)
        self.label_button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_button.setStyleSheet("")
        self.label_button.setObjectName("label_button")
        self.verticalLayout.addWidget(self.label_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(label_dialog)
        QtCore.QMetaObject.connectSlotsByName(label_dialog)

    def retranslateUi(self, label_dialog):
        _translate = QtCore.QCoreApplication.translate
        label_dialog.setWindowTitle(_translate("label_dialog", "Dialog"))
        self.label_label.setText(_translate("label_dialog", "라벨링할 데이터 물품을 선택해 주세요"))
        self.label_button.setText(_translate("label_dialog", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    label_dialog = QtWidgets.QDialog()
    ui = Ui_label_dialog()
    ui.setupUi(label_dialog)
    label_dialog.show()
    sys.exit(app.exec_())
