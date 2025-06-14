import sys
from tkinter.font import names

from PyQt6 import uic
from PyQt6.QtCore import Qt, pyqtSlot
from PyQt6.QtWidgets import QMainWindow, QApplication

from code.data.VList import VList
from code.data.VLists import VLists
from code.data.Word import Word
from code.scripts.SaveVListToJSON import SaveVListToJSON
from code.widgets.CreateListWords import CreateListWords
from code.widgets.ViewList import ViewList


class Main(QMainWindow):
    vLists:VLists

    def __init__(self, vLists:VLists = VLists()):
        super().__init__()
        self.window = uic.loadUi("../uis/main.ui", self)
        self.vLists = vLists
        for l in self.vLists.vLists:
            self.create_widget(l)

    def on_but_create_list_released(self):
        view = CreateListWords()
        view.show()
        self.make_connection(view)

    def create_widget(self, vList):
        card = ViewList(vList)
        self.layout_scroll.addWidget(card)

    @pyqtSlot(VList)
    def get_slider_value(self, vList: VList):
        self.vLists.vLists.append(vList)
        self.create_widget(vList)

    def make_connection(self, slider_object):
        slider_object.changed_value.connect(self.get_slider_value)

if __name__ == '__main__':

    # list1 = VList(name='List test1', number=12, numberLearned=2)
    # list2 = VList(name='List test2', number=12, numberLearned=2)
    # list3 = VList(name='List test3', number=12, numberLearned=2)

    vLists = SaveVListToJSON().loadVListsFromJSON()
    print(vLists)

    app = QApplication(sys.argv)
    win = Main(vLists)
    win.show()
    sys.exit(app.exec())