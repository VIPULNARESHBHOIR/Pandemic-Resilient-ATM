import sys
from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton, QVBoxLayout

class Banks_widget(QDialog):
    def __init__(self, choices):
        super().__init__()

        self.choices = choices
        self.selected_banks = None

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bank Choice Widget')
        self.setFixedSize(460, 320)

        self.label = QLabel('Select The Bank:', self)
        self.label.setStyleSheet("font: 75 12pt \"Sitka Text\";")
        self.label.setGeometry(160, 30, 151, 31)

        self.bank_combo = QComboBox(self)
        self.bank_combo.setGeometry(90, 90, 281, 41)
        self.bank_combo.setStyleSheet("font: 75 14pt \"Sitka Text\";")

        for choice in self.choices:
            self.bank_combo.addItem(choice)

        self.ok_button = QPushButton('OK', self)
        self.ok_button.setGeometry(170, 200, 121, 51)
        self.ok_button.setStyleSheet("font: 75 18pt \"Sitka Text\";")

        self.ok_button.clicked.connect(self.on_ok_button_clicked)

    def on_ok_button_clicked(self):
        self.selected_banks = self.bank_combo.currentText()
        self.accept()
