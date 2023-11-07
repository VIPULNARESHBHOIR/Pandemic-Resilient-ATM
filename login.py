from db import Update,Read,establish_connection
from AtmGui2 import Ui_MainWindow
from Get_OTP import get_OTP
from Banks import Banks_widget  

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import random
import threading
import Hand_trace as ht
import cv2
import numpy as np
import time
import autopy

cap = cv2.VideoCapture(0)
detector = ht.HandDetector(max_hands=1)

class Ui_Authentication(QMainWindow):
#open the ATM window after Successful Authentication
    def openWindow(self):
        self.OTP=str(self.otp_text.toPlainText())
        if self.OTP=="":
                self.messagebox("Enter the OTP",2)
        elif self.OTP==self.otp:
                self.choices=[]
                establish_connection()
                self.banks = Read("select bank from customer where ph_no={}".format(self.mono))
        
                for bank in self.banks:
                        self.choices.append(bank[0])

                bank_choice_dialog = Banks_widget(self.choices)
                result = bank_choice_dialog.exec_()
                if result == Banks_widget.Accepted:
                        selected_bank = bank_choice_dialog.selected_banks
                        if selected_bank:
                                establish_connection()
                                self.window = QtWidgets.QMainWindow()
                                self.ui=Ui_MainWindow()
                                self.ui.setupUi(self.window,self.mono,selected_bank)
                                self.window.show()
                                self.timer_label.setText("")
                                self.otp=self.change_otp()
                                self.timer.stop()
                                self.timer_thread.cancel()
                                self.otp_text.setText("")
                                self.textEdit_2.setText("")
                                self.otp_text.setEnabled(False)
                                self.textEdit_2.setEnabled(True)
                                self.flag=0
                else:
                        pass
                
        else:
                self.messagebox("Enter Valid OTP",2)
    
    def start_timer(self):
        self.remaining_time = 90
        self.timer.start(1000)  # Update the timer label every 1000 ms (1 second)
        self.timer_thread = threading.Timer(90.0, self.change_otp) 
        self.timer_thread.start()

    def update_timer_label(self):
        self.remaining_time -= 1
        if self.remaining_time >= 0:
                self.timer_label.setText(f"OTP valid till: {self.remaining_time} Sec")
        else:
                self.timer_label.setText("")
                self.otp=self.change_otp()
                self.timer.stop()
                self.timer_thread.cancel()
        
    def change_otp(self):
        otp = ''.join(random.choices('0123456789', k=6))
        return otp

    def setupUi(self, Authentication):

        self.remaining_time = 90  #Initial timer duration (seconds)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer_label)

        self.flag=0
        self.pin=""

        Authentication.setObjectName("Authentication")
        Authentication.resize(1100, 746)
        self.centralwidget = QtWidgets.QWidget(Authentication)
        self.centralwidget.setObjectName("centralwidget")
        
        self.msg = QtWidgets.QMessageBox()

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1101, 811))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.05, y1:0.0280455, x2:1, y2:1, stop:0.38806 rgba(29, 171, 173, 255), stop:1 rgba(0, 0, 58, 255));\n"
"background-color: qlineargradient(spread:pad, x1:0.124378, y1:0.119, x2:1, y2:1, stop:0.18408 rgba(37, 37, 37, 255), stop:0.850746 rgba(74, 74, 74, 255));")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 40, 351, 41))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Serif\";")
        self.label_2.setObjectName("label_2")
        self.send_otp = QtWidgets.QPushButton(self.centralwidget)
        self.send_otp.setGeometry(QtCore.QRect(250, 180, 151, 61))
        self.send_otp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.send_otp.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 89, 255);\n"
"border-radius:10px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 85, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.send_otp.setObjectName("send_otp")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 270, 141, 41))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Serif\";")
        self.label_3.setObjectName("label_3")
        self.otp_text = QtWidgets.QTextEdit(self.centralwidget)
        self.otp_text.setGeometry(QtCore.QRect(130, 310, 371, 71))
        self.otp_text.setStyleSheet("background-color: rgb(99, 99, 99);\n"
"font: 75 28pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"border-radius:10px;\n"
"border-bottom:1px solid white;\n"
"")
        self.otp_text.setObjectName("otp_text")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 90, 541, 71))
        self.textEdit_2.setStyleSheet("background-color: rgb(99, 99, 99);\n"
"font: 75 28pt \"MS Shell Dlg 2\";\n"
"color: white;\n"
"border-radius:10px;\n"
"border-bottom:1px solid white;\n"
"")
        self.textEdit_2.setTabChangesFocus(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.continue_2 = QtWidgets.QPushButton(self.centralwidget)
        self.continue_2.setGeometry(QtCore.QRect(170, 400, 141, 51))
        self.continue_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.continue_2.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 89, 255);\n"
"border-radius:10px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(0, 85, 127);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.continue_2.setObjectName("continue_2")
        self.four = QtWidgets.QPushButton(self.centralwidget)
        self.four.setGeometry(QtCore.QRect(700, 170, 81, 71))
        self.four.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.four.setObjectName("four")
        self.three = QtWidgets.QPushButton(self.centralwidget)
        self.three.setGeometry(QtCore.QRect(900, 90, 81, 71))
        self.three.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.three.setObjectName("three")
        self.two = QtWidgets.QPushButton(self.centralwidget)
        self.two.setGeometry(QtCore.QRect(800, 90, 81, 71))
        self.two.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.two.setObjectName("two")
        self.one = QtWidgets.QPushButton(self.centralwidget)
        self.one.setGeometry(QtCore.QRect(700, 90, 81, 71))
        self.one.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}\n"
"")
        self.one.setObjectName("one")
        self.five = QtWidgets.QPushButton(self.centralwidget)
        self.five.setGeometry(QtCore.QRect(800, 170, 81, 71))
        self.five.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.five.setObjectName("five")
        self.six = QtWidgets.QPushButton(self.centralwidget)
        self.six.setGeometry(QtCore.QRect(900, 170, 81, 71))
        self.six.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.six.setObjectName("six")
        self.seven = QtWidgets.QPushButton(self.centralwidget)
        self.seven.setGeometry(QtCore.QRect(700, 250, 81, 71))
        self.seven.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.seven.setObjectName("seven")
        self.eight = QtWidgets.QPushButton(self.centralwidget)
        self.eight.setGeometry(QtCore.QRect(800, 250, 81, 71))
        self.eight.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.eight.setObjectName("eight")
        self.nine = QtWidgets.QPushButton(self.centralwidget)
        self.nine.setGeometry(QtCore.QRect(900, 250, 81, 71))
        self.nine.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.nine.setObjectName("nine")
        self.zero = QtWidgets.QPushButton(self.centralwidget)
        self.zero.setGeometry(QtCore.QRect(800, 330, 81, 71))
        self.zero.setStyleSheet("QPushButton{\n"
"font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: black;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"font: 75 19pt \"Tw Cen MT\";\n"
"background-color: rgb(203, 203, 203);\n"
"}")
        self.zero.setObjectName("zero")
        self.Del = QtWidgets.QPushButton(self.centralwidget)
        self.Del.setGeometry(QtCore.QRect(900, 330, 81, 71))
        self.Del.setStyleSheet("font: 75 20pt \"Tw Cen MT\";\n"
"background-color: rgb(85, 170, 255);\n"
"color: black;\n"
"border-radius:5px;")
        self.Del.setObjectName("Del")
        self.clr = QtWidgets.QPushButton(self.centralwidget)
        self.clr.setGeometry(QtCore.QRect(700, 330, 81, 71))
        self.clr.setStyleSheet("font: 75 20pt \"Tw Cen MT\";\n"
"background-color: red;\n"
"color: black;\n"
"border-radius:5px;")
        self.clr.setObjectName("clr")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 570, 1101, 201))
        self.label_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1050, 0, 61, 681))
        self.label_5.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(-10, 0, 61, 701))
        self.label_6.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.video_frame = QtWidgets.QLabel(self.centralwidget)
        self.video_frame.setGeometry(QtCore.QRect(440, 559, 240, 180))
        self.video_frame.setStyleSheet("border-radius:8px;\n"
"border:1px solid grey;\n"
"background-color:Transparent;")
        self.video_frame.setText("")
        self.video_frame.setObjectName("video_frame")
        self.gif1 = QtWidgets.QLabel(self.centralwidget)
        self.gif1.setGeometry(QtCore.QRect(50, 560, 200, 180))
        self.gif1.setStyleSheet("border-radius:8px;\n"
"border:1px solid grey;\n"
"background-color:Transparent;")
        self.gif1.setText("")
        self.gif1.setPixmap(QtGui.QPixmap(r"C:\Users\bhoir\OneDrive\Desktop\Finalised_Smart_ATM\gif_img\Click me (2).gif"))
        self.movie1=QtGui.QMovie(r"C:\Users\bhoir\OneDrive\Desktop\Finalised_Smart_ATM\gif_img\Click me (2).gif")
        self.gif1.setMovie(self.movie1)
        self.movie1.start()
        self.gif1.setObjectName("gif1")
        self.gif2 = QtWidgets.QLabel(self.centralwidget)
        self.gif2.setGeometry(QtCore.QRect(850, 560, 200, 180))
        self.gif2.setStyleSheet("border-radius:8px;\n"
"border:1px solid grey;\n"
"background-color:Transparent;")
        self.gif2.setText("")
        self.gif2.setPixmap(QtGui.QPixmap(r"C:\Users\bhoir\OneDrive\Desktop\Finalised_Smart_ATM\gif_img\Click me (1).gif"))
        self.movie=QtGui.QMovie(r"C:\Users\bhoir\OneDrive\Desktop\Finalised_Smart_ATM\gif_img\Click me (1).gif")
        self.gif2.setMovie(self.movie)
        self.movie.start()
        self.gif2.setObjectName("gif2")
        self.gif_text1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_text1.setGeometry(QtCore.QRect(50, 520, 211, 41))
        self.gif_text1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";")
        self.gif_text1.setObjectName("gif_text1")
        self.gif_text2 = QtWidgets.QLabel(self.centralwidget)
        self.gif_text2.setGeometry(QtCore.QRect(850, 520, 211, 41))
        self.gif_text2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Rockwell\";")
        self.gif_text2.setObjectName("gif_text2")
        self.reset = QtWidgets.QPushButton(self.centralwidget)
        self.reset.setGeometry(QtCore.QRect(330, 400, 141, 51))
        self.reset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.reset.setStyleSheet("QPushButton{\n"
"background-color:rgb(75, 75, 227);\n"
"border-radius:10px;\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgb(54, 54, 162);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.reset.setObjectName("reset")
        self.timer_label = QtWidgets.QLabel(self.centralwidget)
        self.timer_label.setGeometry(QtCore.QRect(220, 460, 211, 31))
        self.timer_label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Bahnschrift SemiLight SemiConde\";\n"
"background:transparent;")
        self.timer_label.setText("")
        self.timer_label.setObjectName("timer_label")
        Authentication.setCentralWidget(self.centralwidget)

        self.retranslateUi(Authentication)
        QtCore.QMetaObject.connectSlotsByName(Authentication)

# Action to be perform for each button
        self.continue_2.clicked.connect(self.openWindow)
        self.send_otp.clicked.connect(self.Send_OTP)
        self.zero.clicked.connect(self.Zero)
        self.one.clicked.connect(self.One)
        self.two.clicked.connect(self.Two)
        self.three.clicked.connect(self.Three)
        self.four.clicked.connect(self.Four)
        self.five.clicked.connect(self.Five)
        self.six.clicked.connect(self.Six)
        self.seven.clicked.connect(self.Seven)
        self.eight.clicked.connect(self.Eight)
        self.nine.clicked.connect(self.Nine)
        self.clr.clicked.connect(self.CLR)
        self.Del.clicked.connect(self.DEL)
        self.reset.clicked.connect(self.Reset)

# Call the Worker1 Class object to start the camera and related functions
        self.Worker1 = Worker1()
        self.Worker1.start()
        self.Worker1.ImageUpdate.connect(self.ImageUpdateSlot)
   
    def ImageUpdateSlot(self, Image):
        self.video_frame.setPixmap(QPixmap.fromImage(Image))

#function for each action to be perform after clicking button
    def Zero(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"0")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"0")
    def One(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"1")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"1")
    def Two(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"2")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"2")
    def Three(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"3")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"3")
    def Four(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"4")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"4")
    def Five(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"5")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"5")
    def Six(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"6")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"6")
    def Seven(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"7")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"7")
    def Eight(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"8")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"8")
    def Nine(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()+"9")
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()+"9")
        
    def CLR(self):
        if self.flag==0:
                self.textEdit_2.setText("")
        if self.flag==1:
                self.otp_text.setText("")
    def DEL(self):
        if self.flag==0:
                self.textEdit_2.setText(self.textEdit_2.toPlainText()[:-1])
        if self.flag==1:
                self.otp_text.setText(self.otp_text.toPlainText()[:-1])

    #Send the OTP
    def Send_OTP(self):
        self.mono=str(self.textEdit_2.toPlainText())
        if len(self.mono)!=10 or self.mono=="":
                self.messagebox("Enter valid 10-DIGIT Mobile No.",2)
        else:   
                establish_connection()
                # Account exists for the NUMBER or not(retriving data as pin no or anything)
                try:
                        self.pin=Read("select pin from customer where ph_no='{}'".format(self.mono))[0][0]
                except:
                        self.messagebox("Account not EXISTS!!",2)
                print(self.pin)
                if self.pin != None:
                        self.otp=self.change_otp()
                        get_OTP(self.mono,self.otp)
                        self.start_timer()
                        self.flag=1
                        self.otp_text.setEnabled(True)
                        self.textEdit_2.setDisabled(True)
                else:
                        self.messagebox("Account not EXISTS!!",2)

    # reset otp and phone number
    def Reset(self):
        self.flag=0
        self.otp_text.setText("")
        self.textEdit_2.setText("")
        self.otp_text.setEnabled(False)
        self.textEdit_2.setDisabled(False)
        try:
                self.timer_label.setText("")
                self.otp=self.change_otp()
                self.timer.stop()
                self.timer_thread.cancel()
        except:
                pass

    #type 1= information message / type 2 = warning message
    def messagebox(self,message,type):     
        self.message=message
        self.type=type
                
        if self.type==1:
                self.msg.setIcon(self.msg.Information)

                # setting message for Message Box
                self.msg.setText(self.message)

                # setting Message box window title
                self.msg.setWindowTitle("Transaction Successful !!!")

                # declaring buttons on Message Box
                self.msg.setStandardButtons(self.msg.Ok | self.msg.Cancel)

        if self.type==2:
                self.msg.setIcon(self.msg.Warning)

                # setting message for Message Box
                self.msg.setText(self.message)

                # setting Message box window title
                self.msg.setWindowTitle("!!! Warning !!!")

                # declaring buttons on Message Box
                self.msg.setStandardButtons(self.msg.Ok | self.msg.Cancel)

        # start the app
        retval = self.msg.exec_()

    def retranslateUi(self, Authentication):
        _translate = QtCore.QCoreApplication.translate
        Authentication.setWindowTitle(_translate("Authentication", "MainWindow"))
        self.label_2.setText(_translate("Authentication", "Enter your mobile number"))
        self.send_otp.setText(_translate("Authentication", "SEND OTP"))
        self.label_3.setText(_translate("Authentication", "Enter OTP"))
        self.otp_text.setHtml(_translate("Authentication", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_2.setHtml(_translate("Authentication", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:28pt; font-weight:72; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.continue_2.setText(_translate("Authentication", "Continue"))
        self.four.setText(_translate("Authentication", "4"))
        self.three.setText(_translate("Authentication", "3"))
        self.two.setText(_translate("Authentication", "2"))
        self.one.setText(_translate("Authentication", "1"))
        self.five.setText(_translate("Authentication", "5"))
        self.six.setText(_translate("Authentication", "6"))
        self.seven.setText(_translate("Authentication", "7"))
        self.eight.setText(_translate("Authentication", "8"))
        self.nine.setText(_translate("Authentication", "9"))
        self.zero.setText(_translate("Authentication", "0"))
        self.Del.setText(_translate("Authentication", "DEL"))
        self.clr.setText(_translate("Authentication", "CLR"))
        self.gif_text1.setText(_translate("Authentication", "Move the Arrow by"))
        self.gif_text2.setText(_translate("Authentication", "Click the Button by"))
        self.reset.setText(_translate("Authentication", "Reset"))


class Worker1(QThread):
    global plocX,clocX,clocY,plocY,smoothening
    ImageUpdate = pyqtSignal(QImage)
    def run(self):
        self.ThreadActive = True
        width_camera, height_camera = 640, 480
        width_screen, height_screen = autopy.screen.size()  # Screen size
        frame_reduction = 100  # Frame reduction
        smoothening = 5

        previous_time = 0
        previous_location_x, previous_location_y = 0, 0
        current_location_x, current_location_y = 0, 0

        cap.set(3, width_camera)
        cap.set(4, height_camera)

        while self.ThreadActive:
            success, image = cap.read()
            if success:
                # Finding the hand landmarks
                image = detector.find_hands(image)
                landmark_list, bounding_box = detector.find_hand_position(image)

                # Get the tip of the index and middle finger
                if len(landmark_list) != 0:
                        x1, y1 = landmark_list[8][1:]
                        x2, y2 = landmark_list[12][1:]

                # Check up fingers
                fingers = detector.fingers_up()

                if len(fingers) != 0:
                        # Only index finger in moving position
                        if fingers[1] == 1 and fingers[2] == 0:
                                # Converting coordinates for perfect movement of hands
                                x3 = np.interp(x1, (0, width_camera), (0, width_screen))
                                y3 = np.interp(y1, (0, height_camera), (0, height_screen))

                                # Setting to mouse cursor properly over the screen (smoothening)
                                current_location_x = previous_location_x + (x3 - previous_location_x) / smoothening
                                current_location_y = previous_location_y + (y3 - previous_location_y) / smoothening
                                # Movement of mouse over the screen
                                autopy.mouse.move(width_screen - current_location_x, current_location_y)
                                cv2.circle(image, (x1, y1), 15, (255, 0, 255), cv2.FILLED)

                                previous_location_x, previous_location_y = current_location_x, current_location_y

                        # When index and middle finger are up then click
                        if fingers[1] == 1 and fingers[2] == 1:
                                # Find distance between fingers
                                distance, image, line_info = detector.find_distance(8, 12, image)

                                if distance < 20:
                                        cv2.circle(image, (line_info[4], line_info[5]), 15, (0, 255, 0), cv2.FILLED)
                                        autopy.mouse.click()
                                        time.sleep(0.2)


                Image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                FlippedImage = cv2.flip(Image, 1)
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0], QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(250, 250, Qt.KeepAspectRatio)
                self.ImageUpdate.emit(Pic)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Authentication = QtWidgets.QMainWindow()
    ui = Ui_Authentication()
    ui.setupUi(Authentication)
    Authentication.show()
    sys.exit(app.exec_())
