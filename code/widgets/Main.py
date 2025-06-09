import sys
from tkinter.font import names

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication

from code.data.VList import VList
from code.data.Word import Word
from code.widgets.ViewList import ViewList


class Main(QMainWindow):
    def __init__(self, lists:list):
        super().__init__()
        self.window = uic.loadUi("../uis/main.ui", self)

        for l in lists:
            self.create_widget(l)

    def on_but_create_list_released(self):
        print("Create")

    def create_widget(self, vList):
        card = ViewList(vList)
        self.layout_scroll.addWidget(card)

if __name__ == '__main__':

    list1 = VList(name='List test1', number=12, numberLearned=2)
    list2 = VList(name='List test2', number=12, numberLearned=2)
    list3 = VList(name='List test3', number=12, numberLearned=2)
    list4 = VList(name='List test4', number=12, numberLearned=2)
    list5 = VList(name='List test5', number=12, numberLearned=2)
    list6 = VList(name='List test6', number=12, numberLearned=2)

    app = QApplication(sys.argv)
    win = Main([list1, list2])
    win.show()
    sys.exit(app.exec())