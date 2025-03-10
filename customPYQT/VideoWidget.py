# customPYQT/VideoWidget.py
import cv2
from PySide6 import QtWidgets, QtCore, QtGui

class VideoWidget(QtWidgets.QWidget):
    def __init__(self, rtsp_url):
        super().__init__()
        self.rtsp_url = rtsp_url
        self.cap = cv2.VideoCapture(self.rtsp_url)

        self.init_ui()
        self.start_streaming()

    def init_ui(self):
        self.video_label = QtWidgets.QLabel("영상 로딩 중...")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.video_label)

        # 클릭 가능하도록 설정
        self.video_label.setCursor(QtCore.Qt.PointingHandCursor)

    def start_streaming(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = frame.shape
            img = QtGui.QImage(frame.data, w, h, w * 3, QtGui.QImage.Format_RGB888)
            pix = QtGui.QPixmap.fromImage(img)
            self.video_label.setPixmap(pix.scaled(self.video_label.size(), QtCore.Qt.KeepAspectRatio))

    def closeEvent(self, event):
        self.timer.stop()
        self.cap.release()
        event.accept()