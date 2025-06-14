import json
import sys
import keyboard

from PyQt6 import uic, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit

from code.data.Translation import Translation
from code.data.Word import Word
from code.data.Words import Words
from code.scripts.ConvertAndSaveWordsToJSON import ConvertAndSaveWordsToJSON
from code.widgets.TestLevel import TestLevel


class TestLevel1(TestLevel):

    def __init__(self, words: Words, path_file=''):
        super().__init__(words, path_file)

    def load_ui(self):
        self.window = uic.loadUi("../uis/test_level_1.ui", self)

    def show_word(self, word:Word=Word('Example')):
        self.label_word.setText(f'{word.name.__str__()}\n{word.transcription}')

    def set_setting_view_word(self, position):
        super().set_setting_view_word(self.current_position)
        self.line_translate.setText(self.words.words[self.current_position].answer)

    def set_right_answer(self):
        super().set_right_answer()
        self.line_translate.setEnabled(False)

    def on_but_check_released(self):
        self.words.words[self.current_position].answer = self.line_translate.text()
        super().on_but_check_released()

    def reward(self):
        if self.correct_answer < 4:
            self.words.words[self.current_position].correct_answer += 1

    def check_answer(self, answer):
        for t in self.words.words[self.current_position].translations:
            if t.translation.__str__().lower().strip() == str(answer).lower().strip():
                return True
        return False

if __name__ == '__main__':

    path_file = '../../source/listsWordsOnJSON/The Big Bang Theory S1 E2'
    with open(path_file+'.json', 'r') as file:
        ws:Words = Words.from_json(json.dumps(json.load(file)))

    ws.words.sort(key=lambda Word: Word.correct_answer)
    only_unknown = Words()
    for w in ws.words:
        if w.correct_answer < 3:
            only_unknown.words.append(w)
    app = QApplication(sys.argv)
    win = TestLevel1(only_unknown, path_file)
    win.show()
    sys.exit(app.exec())