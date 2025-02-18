from PySide6 import QtWidgets, QtGui, QtCore

class Header(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("headerWidget")
        # 로고 (QLabel)
        self.logo = QtWidgets.QLabel("와우미래기술로고")
        logoImage = QtGui.QPixmap("assets/logo/wowlogo.png")
        # QLabel 크기에 맞추되, 이미지가 잘리지 않고 비율 유지 ("contain" 효과)
        scaled_pixmap = logoImage.scaled(
            60,60,
            QtCore.Qt.KeepAspectRatio,
            QtCore.Qt.SmoothTransformation
        )
        self.logo.setPixmap(scaled_pixmap)

        # 버튼 (QPushButton)
        self.button1 = QtWidgets.QPushButton("영상스트리밍")
        self.button1.setStyleSheet("min-width: 80px; min-height: 45px; padding: 10px; font-size: 16px;")
        self.button2 = QtWidgets.QPushButton("웨이포인트")
        self.button2.setStyleSheet("min-width: 80px; min-height: 45px; padding: 10px; font-size: 16px;")
        self.button3 = QtWidgets.QPushButton("비상시경보")
        self.button3.setStyleSheet("min-width: 80px; min-height: 45px; padding: 10px; font-size: 16px;")
        self.button3 = QtWidgets.QPushButton("배터리 정보")
        self.button3.setStyleSheet("min-width: 80px; min-height: 45px; padding: 10px; font-size: 16px;")

        # 로고를 수직 가운데 정렬하기 위한 VBox 레이아웃
        self.logo_layout = QtWidgets.QVBoxLayout()
        self.logo_layout.setContentsMargins(0, 0, 20, 0)
        self.logo_layout.addStretch()  # 위쪽 여백
        self.logo_layout.addWidget(self.logo)
        self.logo_layout.addStretch()  # 아래쪽 여백

        # 버튼들을 가로로 정렬하는 HBox 레이아웃
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addWidget(self.button1)
        self.button_layout.addWidget(self.button2)
        self.button_layout.addWidget(self.button3)

        # 전체 레이아웃 (가로 정렬)
        self.layout = QtWidgets.QHBoxLayout(self)
        self.layout.addLayout(self.logo_layout)  # 로고 추가 (수직 정렬 포함)
        self.layout.addLayout(self.button_layout)  # 버튼 레이아웃 추가
        self.layout.addStretch()  # 로고와 버튼 사이 간격 추가

        # 헤더 스타일 & 크기 조정
        self.setFixedHeight(100)
        self.setStyleSheet("border: 2px solid red;")
        self.setStyleSheet("#headerWidget {border: 2px solid red;}")

# 실행 코드
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Header()
    window.show()
    app.exec()