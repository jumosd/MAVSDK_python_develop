# customPYQT/VideoStream.py

import sys
import cv2

from PySide6 import QtWidgets, QtCore, QtGui

class VideoStream(QtWidgets.QWidget):
    def __init__(self, rtsp_url):
        super().__init__()
        self.rtsp_url = rtsp_url
        self.cap = cv2.VideoCapture(rtsp_url)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("영상 스트리밍")
        self.video_label = QtWidgets.QLabel()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.video_label)

        # 타이머로 영상 업데이트 (약 30 FPS)
        self.timer = QtCore.QTimer()
        self.timer_interval = 30  # 약 30fps
        self.timer_event()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)  # 약 30 FPS

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            height, width, channel = frame.shape
            image = QtGui.QImage(frame.data, width, height, width*3, QtGui.QImage.Format_RGB888)
            pixmap = QtGui.QPixmap.fromImage(image)
            self.video_label.setPixmap(pixmap.scaled(self.video_label.size(), QtCore.Qt.KeepAspectRatio))

    def closeEvent(self, event):
        self.timer.stop()
        self.cap.release()
        super().closeEvent(event)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    rtsp_url = "rtsp://192.168.144.25:8554/main.264"
    window = VideoStream(rtsp_url)
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())