import sys
from PySide6 import QtWidgets, QtCore
from customPYQT.Header import Header
from customPYQT.Map import Map
from customPYQT.VideoWidget import VideoWidget

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("드론 제어 프로그램")
        self.resize(1200, 800)

        # 메인 레이아웃 설정
        main_layout = QtWidgets.QVBoxLayout(self)

        # 헤더 추가
        self.header = Header()
        main_layout.addWidget(self.header)

        # 지도와 비디오를 교체하는 StackedWidget 설정
        self.content_widget = QtWidgets.QStackedWidget()
        main_layout.addWidget(self.content_widget)

        # 맵 추가
        self.map_widget = Map()
        self.content_widget.addWidget(self.map_widget)

        # 메인 비디오 위젯 추가
        self.video_widget = VideoWidget("rtsp://192.168.144.25:8554/main.264")
        self.content_widget.addWidget(self.video_widget)

        # 초기화면은 지도 표시
        self.content_widget.setCurrentWidget(self.map_widget)

        # 작은 영상 위젯 (좌측 하단 고정)
        self.thumbnail_video = VideoWidget("rtsp://192.168.144.25:8554/main.264")
        self.thumbnail_video.setFixedSize(320, 240)
        self.thumbnail_video.setParent(self)
        self.thumbnail_video.move(20, self.height() - self.thumbnail_video.height() - 20)
        self.thumbnail_video.show()

        # 클릭 이벤트 연결
        self.thumbnail_video.video_label.mousePressEvent = self.switch_to_video
        self.video_widget.video_label.mousePressEvent = self.switch_to_map

        # 상태변수 초기화
        self.is_video_maximized = False

    # 화면 크기 조정 시 썸네일 위치 업데이트
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.thumbnail_video.move(20, self.height() - self.thumbnail_video.height() - 20)

    # 영상으로 전환
    def switch_to_video(self, event):
        if not self.is_video_maximized:
            self.content_widget.setCurrentWidget(self.video_widget)
            self.thumbnail_video.hide()
            self.is_video_maximized = True

    # 다시 맵으로 전환
    def switch_to_map(self, event):
        if self.is_video_maximized:
            self.content_widget.setCurrentWidget(self.map_widget)
            self.thumbnail_video.show()
            self.is_video_maximized = False

    # 창 크기 조정 시 썸네일 위치 유지
    def resizeEvent(self, event):
        super().resizeEvent(event)
        margin = 20
        self.thumbnail_video.move(
            20, 
            self.height() - self.thumbnail_video.height() - 20
        )

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())