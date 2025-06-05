import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication

from code.data.VList import VList


class ViewList(QWidget):
    def __init__(self, vlist:VList):
        super().__init__()
        self.window = uic.loadUi("../uis/view_list.ui", self)

        self.label_name_list.setText(vlist.name)
        self.label_counts.setText(f"{vlist.numberLearned}/{vlist.number}")
        result = (vlist.numberLearned * 100) / vlist.number
        self.label_learned_percent.setText(result.__int__().__str__()+'%')

        self.widget_buttons.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    vList = VList('1. Example List', 420, 45)
    win = ViewList(vList)
    win.show()
    sys.exit(app.exec())