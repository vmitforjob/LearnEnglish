import json
import sys
from random import random, randint

from PyQt6 import uic
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import QWidget, QApplication, QComboBox

from code.data.Word import Word
from code.data.Words import Words
from code.scripts.ConvertAndSaveWordsToJSON import ConvertAndSaveWordsToJSON
from code.widgets.TestLevel import TestLevel


class TestLevel0(TestLevel):
    combo_answers = [None] * 4

    def __init__(self, words: Words, path_file=''):
        super().__init__(words, path_file)

    def load_ui(self):
        self.window = uic.loadUi("../uis/test_level_0.ui", self)

    def show_word(self, word:Word=Word('Example')):
        self.label_word.setText(f'{word.name.__str__()}\n{word.transcription}')

    def set_setting_view_word(self, position):
        super().set_setting_view_word(position)
        self.fill_random_wrong_answers()
        if self.words.words[position].isRight == True:
            for item, a in enumerate(self.combo_answers):
                if self.words.words[position].answer == a:
                    self.combobox_answers.setCurrentIndex(item)

    def fill_random_wrong_answers(self):
        self.combobox_answers.clear()
        self.combo_answers.clear()
        self.combo_answers = [None] * 4
        right_answer_random_point = randint(0, 3)
        self.combo_answers[right_answer_random_point] = self.words.words[self.current_position].translations[0].translation

        for i in range(len(self.combo_answers)):
            if self.combo_answers[i] == None:
                self.combo_answers[i] = self.words.words[
                    randint(0, len(self.words.words)-1)].translations[0].translation
        self.fill_combobox_with_answers(right_answer_random_point)

    def fill_combobox_with_answers(self, right_answer_point):
        for item in range(4):
            self.combobox_answers.addItem(self.combo_answers[item])
            if right_answer_point == item:
                self.combobox_answers.setItemIcon(item, QIcon('../../icons/checked.png'))
            else:
                self.combobox_answers.setItemIcon(item, QIcon('../../icons/wrong.png'))

    def on_but_check_released(self):
        self.words.words[self.current_position].answer = (self.combobox_answers.
                                                          itemText(self.combobox_answers.currentIndex()))
        super().on_but_check_released()

    def on_combobox_answers_activated(self, index):
        if type(index) == int:
            self.words.words[self.current_position].answer = self.combobox_answers.itemText(index)
            self.check_answer(self.words.words[self.current_position].answer)
            self.on_but_check_released()

    def reward(self):
        if self.correct_answer < 2:
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
        if w.correct_answer < 2:
            only_unknown.words.append(w)
    app = QApplication(sys.argv)
    win = TestLevel0(only_unknown, path_file)
    win.show()
    sys.exit(app.exec())