import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class TestLevel1(QWidget):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("../uis/test_level_1.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TestLevel1()
    win.show()
    sys.exit(app.exec())