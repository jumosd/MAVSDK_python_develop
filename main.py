import sys
from PySide6 import QtCore, QtWidgets
from customPYQT.Header import Header
from customPYQT.Body import Body

# PySide6 실행 코드
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # 메인 윈도우
    main_window = QtWidgets.QWidget()
    main_layout = QtWidgets.QVBoxLayout(main_window)

    # 헤더 추가
    header = Header()
    body = Body()
    main_layout.addWidget(header)
    main_layout.addWidget(body)
    # 메인 윈도우 실행
    main_window.resize(800, 600)
    main_window.show()

    sys.exit(app.exec())