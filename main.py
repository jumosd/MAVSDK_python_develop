import sys
import random
from PySide6 import QtWidgets, QtCore



class AppWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World")
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.button2 = QtWidgets.QPushButton("이렇게 버튼을 추가하는구나")
        self.button3 =  QtWidgets.QRadioButton("이렇게 버튼을 추가하는구나")
        self.button4 =  QtWidgets.QRadioButton("이렇게 버튼을 추가하는구나")
        self.button5 =  QtWidgets.QRadioButton("이렇게 버튼을 추가하는구나")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.layout.addWidget(self.button4)
        self.layout.addWidget(self.button5)


        self.button.clicked.connect(self.magic)


    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))
    def test(self):
        print("test")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = AppWindow()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
