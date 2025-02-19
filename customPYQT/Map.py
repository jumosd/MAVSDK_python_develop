from PySide6 import QtWidgets, QtCore
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWebEngineCore import QWebEngineSettings
import folium
import os
import tempfile
from customPYQT.Drone import Drone

class Map(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        # 레이아웃 설정
        layout = QtWidgets.QVBoxLayout(self)

        # QWebEngineView 생성
        self.webview = QWebEngineView(self)
        
        # ✅ QWebEngineView 설정 추가 (외부 리소스 허용)
        settings = self.webview.settings()
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)  # 외부 리소스 허용
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)  # JavaScript 활성화

        layout.addWidget(self.webview)

        # 초기 맵 생성 및 로드
        self.update_map(37.519761357236,126.61111211831)

    def update_map(self, latitude, longitude):
        """드론의 위치를 받아서 맵을 업데이트하는 함수"""
        m = folium.Map(location=[latitude, longitude], zoom_start=15, tiles="OpenStreetMap")  # ✅ tiles 옵션 추가

        # 드론 마커 추가
        folium.Marker(
            [latitude, longitude],
            popup="드론 위치",
            icon=folium.Icon(color="red", icon="cloud")
        ).add_to(m)

        # 지도 저장
        temp_dir = tempfile.gettempdir()
        map_file = os.path.join(temp_dir, "drone_map.html")
        m.save(map_file)

        # QWebEngineView로 지도 로드
        self.webview.setUrl(QtCore.QUrl.fromLocalFile(map_file))