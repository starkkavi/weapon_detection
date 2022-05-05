from PyQt5.QtCore import QThread, Qt, pyqtSignal
from PyQt5.QtGui import QImage
import cv2


class Detection(QThread):
    def __init__(self):
        super(Detection, self).__init__()

    changePixmap = pyqtSignal(QImage)

    def run(self):
        self.running = True

        cap = cv2.VideoCapture(1)

        while self.running:
            ret, frame = cap.read()

            if ret:
                hight , width , channels = frame.shape
                rgbImage = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                bytesPerLine = channels * width
                convertToQtFormat = QImage(rgbImage.data,width, hight, bytesPerLine,QImage.Format_RGBA8888)
                p = convertToQtFormat.scaled(854,480,Qt.KeepAspectRatio)
                self.changePixmap.emit(p)