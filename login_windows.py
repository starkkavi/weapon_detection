from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5 import QtWidgets
import sqlite3
from setting_window import SettingWindow

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow , self).__init__()
        loadUi("Login.ui",self)
        
        self.pushButton.clicked.connect(self.go_to_register)
        self.loginbutton.clicked.connect(self.open_setting)
        
        self.show()
    def go_to_register(self):
        print("go to register page")
        
    def open_setting(self):
        self.settings_window = SettingWindow()
        self.settings_window.displayInfo()
        self.close()
     