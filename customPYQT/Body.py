from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWebEngineWidgets import QWebEngineView


class Body(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("bodyWidget")
        
        # 레이아웃 생성
        layout = QtWidgets.QVBoxLayout(self)
        
        # QWebEngineView 생성 (웹 페이지를 띄울 수 있음)
        self.webview = QWebEngineView(self)
        layout.addWidget(self.webview)
        
        # 구글 맵 URL (서비스에 따라 URL을 변경하세요)
        map_url = QtCore.QUrl("https://www.google.com/maps")
        self.webview.setUrl(map_url)