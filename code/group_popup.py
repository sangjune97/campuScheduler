# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\user\Documents\qt\new\group_popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, parent):
        self.myMainWindow = MainWindow
        self.parent = parent
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(300, 150)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.group_name = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_name.sizePolicy().hasHeightForWidth())
        self.group_name.setSizePolicy(sizePolicy)
        self.group_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.group_name.setObjectName("group_name")
        self.horizontalLayout_2.addWidget(self.group_name)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.group_popup_accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_popup_accept_button.setEnabled(True)
        self.group_popup_accept_button.clicked.connect(self.group_popup_accept_button_clicked)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_popup_accept_button.sizePolicy().hasHeightForWidth())
        self.group_popup_accept_button.setSizePolicy(sizePolicy)
        self.group_popup_accept_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.group_popup_accept_button.setObjectName("group_popup_accept_button")
        self.horizontalLayout_4.addWidget(self.group_popup_accept_button)
        self.group_popup_cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.group_popup_cancel_button.setObjectName("group_popup_cancel_button")
        self.group_popup_cancel_button.clicked.connect(self.group_popup_cancel_button_clicked)
        self.horizontalLayout_4.addWidget(self.group_popup_cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CampuScheduler"))
        self.label_2.setText(_translate("MainWindow", "그룹명 : "))
        self.group_popup_accept_button.setText(_translate("MainWindow", "확인"))
        self.group_popup_cancel_button.setText(_translate("MainWindow", "취소"))

    def createFolder(self,directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
            else:
                QtWidgets.QMessageBox.warning(QtWidgets.QMainWindow(),'CampuScheduler','이미 존재하는 그룹입니다.')
        except OSError:
            QtWidgets.QMessageBox.warning(QtWidgets.QMainWindow(),'CampuScheduler','이미 존재하는 그룹입니다.')
        
    def group_popup_accept_button_clicked(self):
        group_name_text = self.group_name.toPlainText()
        if len(group_name_text)<1 :
            QtWidgets.QMessageBox.warning(QtWidgets.QMainWindow(),'CampuScheduler','그룹명을 입력하세요.')
        path = '../data/'+group_name_text
        self.createFolder(str(path))
        self.parent.group_list_refresh()
        self.myMainWindow.close()
           
    def group_popup_cancel_button_clicked(self):
        self.parent.group_list_refresh()
        self.myMainWindow.close()
        
    
 
"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())"""
