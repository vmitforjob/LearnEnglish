import json
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

from code.data.Words import Words
from code.widgets.TestLevel0 import TestLevel0


class TestLevel0_2(TestLevel0):
    combo_answers = [None] * 4

    def fill_combobox_with_answers(self, right_answer_point):
        for item in range(4):
            self.combobox_answers.addItem(self.combo_answers[item])

    def reward(self):
        if self.correct_answer < 3:
            self.words.words[self.current_position].correct_answer += 1


if __name__ == '__main__':
    path_file = '../../source/listsWordsOnJSON/The Big Bang Theory S1 E2'
    with open(path_file+'.json', 'r') as file:
        ws:Words = Words.from_json(json.dumps(json.load(file)))

    ws.words.sort(key=lambda Word: Word.correct_answer)
    only_unknown = Words()
    for w in ws.words:
        if w.correct_answer < 2:
            only_unknown.words.append(w)
    app = QApplication(sys.argv)
    win = TestLevel0_2(only_unknown, path_file)
    win.show()
    sys.exit(app.exec())