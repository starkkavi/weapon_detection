from PyQt5 import QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QDialog
from PyQt5.uic import loadUi
from detection_windows import DetectionWindow


class SettingWindow(QMainWindow):
    def __init__(self):
        super(SettingWindow, self).__init__()
        loadUi("settings_windows.ui", self)

        self.detection_windows = DetectionWindow()

        self.pushButton.clicked.connect(self.go_to_detection)

    def displayInfo(self):
        self.show()

    def go_to_detection(self):

        if self.detection_windows.isVisible():
            print('Detection Window is already open')
        else:
            self.detection_windows.create_detection_instance()
            self.detection_windows.start_detection()

    def closeEvent(self,event):

        if self.detection_windows.isVisible():
            self.detection_windows.detection,running = False
            self.detection_windows.close()
            event.accept()
