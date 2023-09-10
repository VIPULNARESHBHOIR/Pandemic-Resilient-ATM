import sys 
import cv2 
import datetime 
from PyQt5.QtCore import pyqtSlot 
from PyQt5.uic import loadUi 
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QDialog,QApplication 

class tehseencode(QDialog): 
	def __init__(self): 
		super(tehseencode, self).__init__() 
		loadUi('Record.ui', self) 
		self.logic=0 
		self.START.clicked.connect(self.STARTClicked) 
		self.TEXT.setText('Kindly Press "Start Recording" button to record video')			
		self.STOP.clicked.connect(self.STOPClicked) 

	@pyqtSlot() 
	def STARTClicked(self):
		self.logic=1 
		cap = cv2.VideoCapture(0) 
		cap.set(cv2.CAP_PROP_FRAME_WIDTH, 121)
		cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 111)
		date = datetime.datetime.now() 
		out = cv2.VideoWriter('C:/Users/bhoir/OneDrive/Desktop/YT_Studio/videos/Video_%s%s%sT%s%s%s.mp4'%(date.year,date.month, date.day, date.hour,date.minute,date.second),-1,20.0,(640,480))
	
		while (cap.isOpened()):
			ret,frame=cap.read()
			if ret == True: 
				self.displayImage (frame, 1) 
				cv2.waitKey() 
				if (self.logic==1): 
					out.write(frame)
					self.TEXT.setText('Video Recording Start')
				if (self.logic ==0): 
					self.TEXT.setText('Video Recording Stop')
					break
			else: 
				print('return not found') 
					
		cap.release() 
		cv2.destroyAllWindows() 

	def STOPClicked(self): 
		self.logic=0 

	def displayImage(self, img,window=1): 
		qformat=QImage.Format_Indexed8 
		
		if len(img.shape) == 3: 
			if (img.shape[2]) == 4: 
				qformat = QImage.Format_RGBA888 
			else: 
				qformat = QImage.Format_RGB888 

		img =QImage(img, img.shape[1], img.shape[0], qformat)
		img =img.rgbSwapped()

		self.imgLabel.setPixmap(QPixmap.fromImage(img)) 
		# print('i am here') 
		# self.imgLabel.setAlignment (QtCore.Qt.AlignHCenter | QtCore.Qt.Align/Center) 

app=QApplication(sys.argv) 
window=tehseencode() 
window.show() 
try: 
	sys.exit(app.exec_())
except:
	print("something")
	