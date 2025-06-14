import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication

from code.data.VList import VList
from code.scripts.ConvertAndSaveWordsToJSON import ConvertAndSaveWordsToJSON
from code.widgets.TestLevel1 import TestLevel1


class ViewList(QWidget):
    isOpenButtons = False
    vList:VList

    def __init__(self, vList:VList):
        super().__init__()
        self.window = uic.loadUi("../uis/view_list.ui", self)

        self.vList = vList
        self.label_name_list.setText(vList.name)
        self.label_counts.setText(f"{vList.numberLearned}/{vList.number}")
        percent_learned = 0
        if not vList.number == 0:
            percent_learned = (vList.numberLearned * 100) / vList.number
        self.label_learned_percent.setText(percent_learned.__int__().__str__()+'%')

        self.widget_buttons.setVisible(self.isOpenButtons)

    def on_but_open_down_buttons_released(self):
        if self.isOpenButtons:
            self.isOpenButtons=False
        else:
            self.isOpenButtons = True
        self.widget_buttons.setVisible(self.isOpenButtons)

    def on_but_learn_released(self):
        words = ConvertAndSaveWordsToJSON().loadWordsFromJSON(self.vList.pathListWords)
        view = TestLevel1(words)
        view.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vList = VList('1. Example List', 420, 45)
    win = ViewList(vList)
    win.show()
    sys.exit(app.exec())