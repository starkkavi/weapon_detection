from PyQt5.QtWidgets import QApplication
import sys
from login_windows import LoginWindow

app = QApplication(sys.argv)
mainwindows=LoginWindow()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")