import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class CreateListWords(QWidget):
    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("../uis/create_list_words.ui", self)

    def on_but_load_list_words_released(self):
        pass

    def on_but_save_released(self):
        pass

    def on_but_cancel_released(self):
        pass



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CreateListWords()
    win.show()
    sys.exit(app.exec())