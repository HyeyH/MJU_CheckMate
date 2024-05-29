# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from gui.file_manager import FileManager as FD

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("#menu_widget {\n"
"    background-color:  #313a46;\n"
"}\n"
"#menu_widget QPushButton, QLabel{\n"
"    height: 50px;\n"
"    border: none;\n"
"}\n"
"#menu_widget QPushButton:hover{\n"
"    background-color: rgba(86,101,115,0.5);\n"
"}\n"
"#menu_widget QLabel{\n"
"    color: #fff;\n"
"}\n"
"#menu_widget QPushButton{\n"
"    color:  #737373;\n"
"}\n"
"#menu_widget QPushButton:hover{\n"
"    color:  #fff;\n"
"}\n"
"#MainWindow{\n"
"    background-color:#fff;\n"
"}\n"
"#data_page QPushButton:hover{\n"
"    color: #fff;\n"
"}\n"
"#train_page QPushButton:hover{\n"
"    color: #fff;\n"
"}\n"
"#detect_page QPushButton:hover{\n"
"    color: #fff;\n"
"}\n"
"#data_page data_button{\n"
"    color: #fff;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.menu_widget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.menu_widget.setObjectName("menu_widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.menu_widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logo = QtWidgets.QLabel(self.menu_widget)
        self.logo.setMinimumSize(QtCore.QSize(50, 50))
        self.logo.setMaximumSize(QtCore.QSize(50, 50))
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/icons/icons/icons8-출석-표-64.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        self.horizontalLayout.addWidget(self.logo)
        self.title = QtWidgets.QLabel(self.menu_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.horizontalLayout.addWidget(self.title)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_button = QtWidgets.QPushButton(self.menu_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.home_button.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-집-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_button.setIcon(icon1)
        self.home_button.setIconSize(QtCore.QSize(25, 25))
        self.home_button.setCheckable(True)
        self.home_button.setAutoExclusive(True)
        self.home_button.setObjectName("home_button")
        self.verticalLayout.addWidget(self.home_button)
        self.data_button = QtWidgets.QPushButton(self.menu_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.data_button.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-영상-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.data_button.setIcon(icon2)
        self.data_button.setIconSize(QtCore.QSize(25, 25))
        self.data_button.setCheckable(True)
        self.data_button.setAutoExclusive(True)
        self.data_button.setObjectName("data_button")
        self.verticalLayout.addWidget(self.data_button)
        self.learn_button = QtWidgets.QPushButton(self.menu_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.learn_button.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-책-공개-시험-48 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.learn_button.setIcon(icon3)
        self.learn_button.setIconSize(QtCore.QSize(25, 25))
        self.learn_button.setCheckable(True)
        self.learn_button.setAutoExclusive(True)
        self.learn_button.setObjectName("learn_button")
        self.verticalLayout.addWidget(self.learn_button)
        self.detect_button = QtWidgets.QPushButton(self.menu_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.detect_button.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-검사-48 (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.detect_button.setIcon(icon4)
        self.detect_button.setIconSize(QtCore.QSize(25, 25))
        self.detect_button.setCheckable(True)
        self.detect_button.setAutoExclusive(True)
        self.detect_button.setObjectName("detect_button")
        self.verticalLayout.addWidget(self.detect_button)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 248, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.helper_button = QtWidgets.QPushButton(self.menu_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(13)
        self.helper_button.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/icons8-search-more-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helper_button.setIcon(icon5)
        self.helper_button.setIconSize(QtCore.QSize(25, 25))
        self.helper_button.setCheckable(True)
        self.helper_button.setAutoExclusive(True)
        self.helper_button.setObjectName("helper_button")
        self.verticalLayout_2.addWidget(self.helper_button)
        self.gridLayout.addWidget(self.menu_widget, 0, 0, 1, 1)
        self.content_widget = QtWidgets.QWidget(self.centralwidget)
        self.content_widget.setObjectName("content_widget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.content_widget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.content_widget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.main_page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.main_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.main_page)
        self.data_page = QtWidgets.QWidget()
        self.data_page.setObjectName("data_page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.data_page)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.data_add_button = QtWidgets.QPushButton(self.data_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.data_add_button.setFont(font)
        self.data_add_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.data_add_button.setObjectName("data_add_button")
        self.horizontalLayout_3.addWidget(self.data_add_button)
        self.data_label_button = QtWidgets.QPushButton(self.data_page)
        # 이 부분은 충돌 오류 날 때마다 추가 부탁드립니다
        self.file_manager = FD()
        self.gridLayout_3.addWidget(self.file_manager, 2, 0, 1, 1)
        #
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.data_label_button.setFont(font)
        self.data_label_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.data_label_button.setObjectName("data_label_button")
        self.horizontalLayout_3.addWidget(self.data_label_button)
        self.dataset_create_button = QtWidgets.QPushButton(self.data_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dataset_create_button.setFont(font)
        self.dataset_create_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.dataset_create_button.setObjectName("dataset_create_button")
        self.horizontalLayout_3.addWidget(self.dataset_create_button)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        self.data_label = QtWidgets.QLabel(self.data_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.data_label.setFont(font)
        self.data_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.data_label.setAlignment(QtCore.Qt.AlignCenter)
        self.data_label.setObjectName("data_label")
        self.gridLayout_3.addWidget(self.data_label, 0, 0, 1, 1)
        self.data_info_label = QtWidgets.QLabel(self.data_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.data_info_label.setFont(font)
        self.data_info_label.setObjectName("data_info_label")
        self.gridLayout_3.addWidget(self.data_info_label, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.data_page)
        self.train_page = QtWidgets.QWidget()
        self.train_page.setObjectName("train_page")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.train_page)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.train_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        #3줄 추가
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.train_page)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout_6.addWidget(self.textBrowser_2, 1, 0, 1, 1)
#        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
#        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
#        self.lineEdit_2 = QtWidgets.QLineEdit(self.train_page)
#        font = QtGui.QFont()
#        font.setPointSize(9)
#        self.lineEdit_2.setFont(font)
#        self.lineEdit_2.setStyleSheet("border: 2px solid#a6aaaf;\n"
#"border-radius: 5px;\n"
#"padding: 1px 5px;\n"
#"\n"
#"")
#        self.lineEdit_2.setObjectName("lineEdit_2")
#        self.horizontalLayout_4.addWidget(self.lineEdit_2)
#        self.train_data_upload_button = QtWidgets.QPushButton(self.train_page)
#        font = QtGui.QFont()
#        font.setFamily("맑은 고딕")
#        font.setPointSize(10)
#        font.setBold(True)
#        font.setWeight(75)
#        self.train_data_upload_button.setFont(font)
#        self.train_data_upload_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
#"border-radius: 5px;\n"
#"padding: 1px 5px;\n"
#"background-color: #a6aaaf;\n"
#"")
#        self.train_data_upload_button.setObjectName("train_data_upload_button")
#        self.horizontalLayout_4.addWidget(self.train_data_upload_button)
#        self.gridLayout_6.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)
#        spacerItem1 = QtWidgets.QSpacerItem(20, 434, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
#        self.gridLayout_6.addItem(spacerItem1, 2, 0, 1, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.yolo_button = QtWidgets.QPushButton(self.train_page)
        self.yolo_button.setMinimumSize(QtCore.QSize(0, 0))
        self.yolo_button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.yolo_button.setFont(font)
        self.yolo_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.yolo_button.setObjectName("yolo_button")
        self.gridLayout_5.addWidget(self.yolo_button, 0, 0, 1, 1)
        self.efficientAD_button = QtWidgets.QPushButton(self.train_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.efficientAD_button.setFont(font)
        self.efficientAD_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.efficientAD_button.setObjectName("efficientAD_button")
        self.gridLayout_5.addWidget(self.efficientAD_button, 0, 1, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_5, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.train_page)
        self.detect_page = QtWidgets.QWidget()
        self.detect_page.setObjectName("detect_page")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.detect_page)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_3 = QtWidgets.QLabel(self.detect_page)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_10.addWidget(self.label_3, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem2, 1, 0, 1, 1)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.anomaly_detect_widget = QtWidgets.QWidget(self.detect_page)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.anomaly_detect_widget.setFont(font)
        self.anomaly_detect_widget.setStyleSheet("#anomaly_detect_widget{\n"
"    border: 2px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"}")
        self.anomaly_detect_widget.setObjectName("anomaly_detect_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.anomaly_detect_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.anomaly_detect_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.anomaly_detect_widget)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.refresh_button = QtWidgets.QPushButton(self.anomaly_detect_widget)
        self.refresh_button.setIconSize(QtCore.QSize(40, 40))  # 버튼 크기 설정
        icon = QtGui.QIcon("gui/icons/refresh-icon-14.png")  # 이미지 파일 경로 설정
        self.refresh_button.setIcon(icon)  # 버튼에 이미지 설정
        self.refresh_button.setFixedSize(QtCore.QSize(40, 40))  # 버튼 크기 고정
        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
            }
            QPushButton:hover {
                background-color: #a6aaaf;
            }
        """)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.horizontalLayout_4.addWidget(self.refresh_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4, 0)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.detect_image_button = QtWidgets.QPushButton(self.anomaly_detect_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.detect_image_button.setFont(font)
        self.detect_image_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.detect_image_button.setObjectName("detect_image_button")
        self.horizontalLayout_2.addWidget(self.detect_image_button)
        self.detect_video_button = QtWidgets.QPushButton(self.anomaly_detect_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.detect_video_button.setFont(font)
        self.detect_video_button.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.detect_video_button.setObjectName("detect_video_button")
        self.horizontalLayout_2.addWidget(self.detect_video_button)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.gridLayout_9.addWidget(self.anomaly_detect_widget, 0, 0, 1, 1)
        self.anomaly_widget = QtWidgets.QWidget(self.detect_page)
        self.anomaly_widget.setStyleSheet("#anomaly_widget{\n"
"    border: 2px solid#a6aaaf;\n"
"    border-radius: 5px;\n"
"}")
        self.anomaly_widget.setObjectName("anomaly_widget")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.anomaly_widget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_5 = QtWidgets.QLabel(self.anomaly_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_8.addWidget(self.label_5, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.anomaly_widget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 4px solid#a6aaaf;\n"
"border-radius: 5px;\n"
"padding: 1px 5px;\n"
"background-color: #a6aaaf;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_8.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout_9.addWidget(self.anomaly_widget, 1, 0, 1, 1)
        self.gridLayout_10.addLayout(self.gridLayout_9, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem3, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.detect_page)
        self.helper_page = QtWidgets.QWidget()
        self.helper_page.setObjectName("helper_page")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.helper_page)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.textBrowser = QtWidgets.QTextBrowser(self.helper_page)
        font = QtGui.QFont()
        font.setFamily("Pretendard Variable SemiBold")
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_7.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.helper_page)
        self.gridLayout_4.addWidget(self.stackedWidget, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.content_widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "체크메이트"))
        self.home_button.setText(_translate("MainWindow", "홈"))
        self.data_button.setText(_translate("MainWindow", "데이터"))
        self.learn_button.setText(_translate("MainWindow", "학습"))
        self.detect_button.setText(_translate("MainWindow", "검출"))
        self.helper_button.setText(_translate("MainWindow", "도움말"))
        self.label.setText(_translate("MainWindow", "체크메이트"))
        self.data_add_button.setText(_translate("MainWindow", "데이터 추가"))
        self.data_label_button.setText(_translate("MainWindow", "데이터 라벨링"))
        self.dataset_create_button.setText(_translate("MainWindow", "데이터셋 생성"))
        self.data_label.setText(_translate("MainWindow", "데이터"))
        self.data_info_label.setText(_translate("MainWindow", "모델 학습을 위한 데이터를 관리하는 메뉴입니다.\n"))
        self.label_2.setText(_translate("MainWindow", "학습"))
#        self.train_data_upload_button.setText(_translate("MainWindow", "불러오기"))
        self.yolo_button.setText(_translate("MainWindow", "YOLO 학습"))
        self.efficientAD_button.setText(_translate("MainWindow", "EfficientAD 학습"))
        self.label_3.setText(_translate("MainWindow", "불량 검출"))
        self.detect_image_button.setText(_translate("MainWindow", "이미지"))
        self.detect_video_button.setText(_translate("MainWindow", "영상"))
        self.label_4.setText(_translate("MainWindow", "YOLO 검출")) #추가
        self.label_5.setText(_translate("MainWindow", "EFFICIENT 검출")) #추가
        self.pushButton.setText(_translate("MainWindow", "이상 탐지")) #추가
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Pretendard Variable SemiBold\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Gulim\';\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Gulim\';\">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</span></p></body></html>"))
import gui.resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
