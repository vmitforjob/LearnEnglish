import sys

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("../uis/main.ui", self)

    def on_but_create_list_released(self):
        print("Create")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main()
    win.show()
    sys.exit(app.exec())