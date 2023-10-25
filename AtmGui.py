from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
import pyttsx3
from db import Update,Read,establish_connection
from ENDEC_crypt import decrypt,encrypt

#setting of engine to taking voice 
eng=pyttsx3.init('sapi5')          
voices=eng.getProperty('voices')
eng.setProperty('voices',voices[0].id)
eng.setProperty('rate',170)              #speech rate in words per minute

class Ui_MainWindow(object):
    
    def closeMain(self,win):
        win.hide()

    
    def Speak(self,text):
        self.audio=text
        eng.say(self.audio)
        print("")
        eng.runAndWait() 

    def setupUi(self, MainWindow,mob,Bank_name):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1214, 758)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.win_dow=MainWindow
        self.mob=mob
        self.flag=3     #this flag is use for do nothing
        self.option=0
        self.pass_word=""
        self.Bank_name=Bank_name
        self.PIN=decrypt(self.mob,self.Bank_name) #retriving decrypted pin from database

        self.msg = QtWidgets.QMessageBox()
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-6, -5, 1221, 761))
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.124378, y1:0.119, x2:1, y2:1, stop:0.18408 rgba(0, 73, 113, 255), stop:0.850746 rgba(27, 0, 68, 255));\n"
"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.greenpin = QtWidgets.QPushButton(self.centralwidget)
        self.greenpin.setGeometry(QtCore.QRect(0, 80, 271, 71))
        self.greenpin.setStyleSheet(
"background-color: rgb(0, 0, 59);\n"
"font: 18pt \"Sitka\";\n"
"color:aqua;\n"
"border-radius:10px;\n"
"border-bottom:2px solid aqua;\n"
)
        self.greenpin.setObjectName("greenpin")
        self.withdrawal = QtWidgets.QPushButton(self.centralwidget)
        self.withdrawal.setGeometry(QtCore.QRect(0, 240, 271, 71))
        self.withdrawal.setStyleSheet("background-color: rgb(0, 0, 59);\n"
"font: 18pt \"Sitka\";\n"
"color:aqua;\n"
"border-radius:10px;\n"
"border-bottom:2px solid aqua;")
        self.withdrawal.setObjectName("withdrawal")
        self.changepin = QtWidgets.QPushButton(self.centralwidget)
        self.changepin.setGeometry(QtCore.QRect(940, 80, 271, 71))
        self.changepin.setStyleSheet("background-color: rgb(0, 0, 59);\n"
"font: 18pt \"Sitka\";\n"
"color:aqua;\n"
"border-radius:10px;\n"
"border-bottom:2px solid aqua;")
        self.changepin.setObjectName("changepin")
        self.show_balance = QtWidgets.QPushButton(self.centralwidget)
        self.show_balance.setGeometry(QtCore.QRect(940, 220, 271, 71))
        self.show_balance.setStyleSheet("background-color: rgb(0, 0, 59);\n"
"font: 18pt \"Sitka\";\n"
"color:aqua;\n"
"border-radius:10px;\n"
"border-bottom:2px solid aqua;")
        self.show_balance.setObjectName("deposit")
        self.textbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbox.setGeometry(QtCore.QRect(300, 20, 641, 41))
        self.textbox.setStyleSheet("color: rgb(114, 255, 239);\n"
"background-color:transparent;\n"
"border:none;\n"
"font: 16pt \"OCR A Extended\";")
        self.textbox.setObjectName("textbox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(430, 150, 371, 321))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.two = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.two.setMinimumSize(QtCore.QSize(30, 62))
        self.two.setMaximumSize(QtCore.QSize(148, 28))
        self.two.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 2, 1, 1, 1)
        self.four = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.four.setMinimumSize(QtCore.QSize(30, 62))
        self.four.setMaximumSize(QtCore.QSize(148, 28))
        self.four.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.four.setObjectName("four")
        self.gridLayout.addWidget(self.four, 1, 0, 1, 1)
        self.three = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.three.setMinimumSize(QtCore.QSize(30, 62))
        self.three.setMaximumSize(QtCore.QSize(148, 28))
        self.three.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 2, 2, 1, 1)
        self.five = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.five.setMinimumSize(QtCore.QSize(30, 62))
        self.five.setMaximumSize(QtCore.QSize(148, 28))
        self.five.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.five.setObjectName("five")
        self.gridLayout.addWidget(self.five, 1, 1, 1, 1)
        self.seven = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.seven.setMinimumSize(QtCore.QSize(30, 62))
        self.seven.setMaximumSize(QtCore.QSize(148, 28))
        self.seven.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;\n"
"\n"
"")
        self.seven.setObjectName("seven")
        self.gridLayout.addWidget(self.seven, 0, 0, 1, 1)
        self.one = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.one.setMinimumSize(QtCore.QSize(30, 62))
        self.one.setMaximumSize(QtCore.QSize(148, 28))
        self.one.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 2, 0, 1, 1)
        self.six = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.six.setMinimumSize(QtCore.QSize(30, 62))
        self.six.setMaximumSize(QtCore.QSize(148, 28))
        self.six.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.six.setObjectName("six")
        self.gridLayout.addWidget(self.six, 1, 2, 1, 1)
        self.eight = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.eight.setMinimumSize(QtCore.QSize(30, 62))
        self.eight.setMaximumSize(QtCore.QSize(148, 28))
        self.eight.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.eight.setObjectName("eight")
        self.gridLayout.addWidget(self.eight, 0, 1, 1, 1)
        self.nine = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.nine.setMinimumSize(QtCore.QSize(30, 62))
        self.nine.setMaximumSize(QtCore.QSize(148, 28))
        self.nine.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.nine.setObjectName("nine")
        self.gridLayout.addWidget(self.nine, 0, 2, 1, 1)
        self.zero = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.zero.setMinimumSize(QtCore.QSize(30, 62))
        self.zero.setMaximumSize(QtCore.QSize(148, 28))
        self.zero.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 3, 1, 1, 1)
        self.clr = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.clr.setMinimumSize(QtCore.QSize(30, 62))
        self.clr.setMaximumSize(QtCore.QSize(148, 28))
        self.clr.setStyleSheet("background-color: rgb(41, 73, 255);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.clr.setObjectName("clr")
        self.gridLayout.addWidget(self.clr, 3, 0, 1, 1)
        self.Del = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.Del.setMinimumSize(QtCore.QSize(30, 62))
        self.Del.setMaximumSize(QtCore.QSize(148, 28))
        self.Del.setStyleSheet("background-color: rgb(3, 9, 26);\n"
"font: 28pt \"MV Boli\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius:30px;")
        self.Del.setObjectName("del")
        self.gridLayout.addWidget(self.Del, 3, 2, 1, 1)
        self.proceed = QtWidgets.QPushButton(self.centralwidget)
        self.proceed.setGeometry(QtCore.QRect(490, 490, 251, 61))
        self.proceed.setStyleSheet("\n"
"font: 28pt ;\n"
"border-radius:10px;\n"
"background-color: rgb(65, 255, 112);")
        self.proceed.setObjectName("proceed")
        self.video = QtWidgets.QLabel(self.centralwidget)
        self.video.setGeometry(QtCore.QRect(960, 530, 241, 211))
        self.video.setStyleSheet("border:2px solid grey;")
        self.video.setText("")
        self.video.setObjectName("video")

        self.card = QtWidgets.QPushButton(self.centralwidget,clicked=lambda:self.closeMain(MainWindow))
        self.card.setText("CLOSE")
        self.card.setGeometry(QtCore.QRect(30, 640, 351, 81))

        self.card.setStyleSheet("\n"
"font: 28pt ;\n"
"border-radius:10px;\n"
"background-color:red;\n"
"color:white;\n"
"border:1px solid grey;")
        self.card.setObjectName("card")
        self.inputbox = QtWidgets.QTextBrowser(self.centralwidget)
        self.inputbox.setGeometry(QtCore.QRect(340, 70, 520, 80))
        self.inputbox.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.124378, y1:0.119, x2:1, y2:1, stop:0.18408 rgba(0, 0, 0, 147), stop:0.850746 rgba(3, 0, 7, 255));\n"
"font: 30pt \"MV Boli\";\n"
"color: rgb(85, 255, 38);\n"
"border:none;\n"
"border-radius:10px;\n"
"border-bottom:2px solid grey;\n"
"border-left:2px solid grey;")
        self.inputbox.setObjectName("inputbox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

#===========intance to connect function to coresponding buttons===========
        
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

        self.changepin.clicked.connect(self.Changepin)
        self.withdrawal.clicked.connect(self.Withdrawal) 
        self.show_balance.clicked.connect(self.Balence)
        self.proceed.clicked.connect(self.Proceed)

#================== Methods for each button ==========================
    
    def quit(self):
        self.exit()

    def Zero(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"0")
        if self.option==1:
                self.pass_word+="0"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def One(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"1")
        if self.option==1:
                self.pass_word+="1"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Two(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"2")
        if self.option==1:
                self.pass_word+="2"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Three(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"3")
        if self.option==1:
                self.pass_word+="3"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Four(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"4")
        if self.option==1:
                self.pass_word+="4"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Five(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"5")
        if self.option==1:
                self.pass_word+="5"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Six(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"6")
        if self.option==1:
                self.pass_word+="6"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Seven(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"7")
        if self.option==1:
                self.pass_word+="7"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Eight(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"8")
        if self.option==1:
                self.pass_word+="8"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    def Nine(self):
        if self.option==0:
                self.inputbox.setText(self.inputbox.toPlainText()+"9")
        if self.option==1:
                self.pass_word+="9"
                self.inputbox.setText(self.inputbox.toPlainText()+"*")
    
    def CLR(self):
        if self.option==1:
                self.pass_word=""
        self.inputbox.setText("")
    def DEL(self):
        self.inputbox.setText(self.inputbox.toPlainText()[:-1])
        if self.option==1:
                self.pass_word=self.pass_word[:-1]

    def Changepin(self):
        self.textbox.setText("\t\tEnter your PIN")
        self.flag=4

    def Balence(self):
        establish_connection()
        self.BALANCE = Read("select balance from customer where ph_no='{}' and bank='{}'".format(self.mob,self.Bank_name))[0][0]
        self.messagebox("YOUR BALANCE:{}".format(self.BALANCE),1)

    def Withdrawal(self):
        self.flag=0
        self.option=0
        self.textbox.setText("\t\tEnter The Amount")
        self.Speak("Enter The Amount")

    def Proceed(self):
        if self.flag==0:                                #for withdrawal
                if self.inputbox.toPlainText()!="":
                        self.amount=int(self.inputbox.toPlainText())
                        print(self.mob)
                        establish_connection()
                        self.BALANCE = Read("select balance from customer where ph_no='{}' and bank='{}'".format(self.mob,self.Bank_name))[0][0]
                        print(self.BALANCE)
                        if self.BALANCE==None:
                                print("TRY AGAIN!!")

                        elif self.amount>int(self.BALANCE):
                                self.Speak("No enough balance in account")
                                self.messagebox("You don't have enough balance in account\nYOUR BALANCE:%s"%(self.BALANCE),2)
                                self.flag=0
                                
                        else:
                                self.textbox.setText("\t\tEnter Your PIN")
                                self.inputbox.setText("")
                                self.flag=1
                                self.option=1
                                self.Speak("Enter Your PIN")
                                
        if self.flag==1:                                #for pin
                if self.inputbox.toPlainText()!="":
                        self.pin=self.pass_word
                        print(self.pin)
                        self.flag=2
                
        if self.flag==2: 
                #for cross verify the pin
                if str(self.pin)==str(self.PIN):
                        establish_connection()
                        Update("update customer set balance=balance-{} where ph_no='{}' and bank='{}'".format (self.amount,self.mob,self.Bank_name))
                        self.Speak("Transaction Successful !")
                        self.messagebox("Withdrawal Amount:%s\nTake the Money from Money Box"%(self.amount),1)
                        #self.inputbox.setText("")
                        #self.flag=3
                        #self.textbox.setText("")
                        self.closeMain(self.win_dow)

                else:
                        self.Speak("Incorrect PIN")
                        self.messagebox("Incorrect PIN",2)
                        self.inputbox.setText("")
                        self.flag=1
                        self.pass_word=""
                        print(self.pass_word)

        if self.flag==4:
                if self.inputbox.toPlainText()!="":
                        self.pin=int(self.inputbox.toPlainText())
                        self.PIN=decrypt(self.mob,self.Bank_name)
                        if str(self.PIN)==str(self.pin):
                                self.flag=5
                                self.inputbox.setText("")
                                self.textbox.setText("\t\tEnter the new PIN")
                        else:
                                self.messagebox("Incorrect PIN",2)
                        
        if self.flag==5:
                
                self.pin=str(self.inputbox.toPlainText())
                if self.pin !="":
                        check=encrypt(self.mob,self.Bank_name,self.pin)
                        if check:
                                self.messagebox("PIN has been changed Successfully !",1)
                        #establish_connection()
                        #Update("update customer set pin={} where ph_no='{}' and bank='{}'".format (self.pin,self.mob,self.Bank_name))
                        self.flag=3
                        self.inputbox.setText("")
                else:
                        self.messagebox("ENTER NEW PIN",1)
        
        
    def messagebox(self,message,type):              #type 1= information message / type 2 = warning message
        self.message=message
        self.type=type
                
        if self.type==1:
                self.msg.setIcon(self.msg.Information)

                # setting message for Message Box
                self.msg.setText(self.message)

                # setting Message box window title
                self.msg.setWindowTitle("Information")

                # declaring buttons on Message Box
                self.msg.setStandardButtons(self.msg.Ok | self.msg.Cancel)

        if self.type==2:
                self.msg.setIcon(self.msg.Warning)

                # setting message for Message Box
                self.msg.setText(self.message)

                # setting Message box window title
                self.msg.setWindowTitle("Warning !!!")

                # declaring buttons on Message Box
                self.msg.setStandardButtons(self.msg.Ok | self.msg.Cancel)


        # start the message_app
        retval = self.msg.exec_()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.greenpin.setText(_translate("MainWindow", "Green Pin"))
        self.withdrawal.setText(_translate("MainWindow", "Cash Withdrawl"))
        self.changepin.setText(_translate("MainWindow", "Change Pin"))
        self.show_balance.setText(_translate("MainWindow", "Balance"))
        self.textbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'OCR A Extended\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.two.setText(_translate("MainWindow", "2"))
        self.four.setText(_translate("MainWindow", "4"))
        self.three.setText(_translate("MainWindow", "3"))
        self.five.setText(_translate("MainWindow", "5"))
        self.seven.setText(_translate("MainWindow", "7"))
        self.one.setText(_translate("MainWindow", "1"))
        self.six.setText(_translate("MainWindow", "6"))
        self.eight.setText(_translate("MainWindow", "8"))
        self.nine.setText(_translate("MainWindow", "9"))
        self.zero.setText(_translate("MainWindow", "0"))
        self.clr.setText(_translate("MainWindow", "CLR"))
        self.Del.setText(_translate("MainWindow", "DEL"))
        self.proceed.setText(_translate("MainWindow", "Proceed"))
        self.card.setText(_translate("MainWindow", "CLOSE"))
        self.inputbox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MV Boli\'; font-size:28pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
