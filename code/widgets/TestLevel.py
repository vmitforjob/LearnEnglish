import json
import sys
from threading import Timer

import keyboard

from PyQt6 import uic, QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit
from PyQt6.uic.Loader.loader import DynamicUILoader

from code.data.Translation import Translation
from code.data.Word import Word
from code.data.Words import Words
from code.scripts.ConvertAndSaveWordsToJSON import ConvertAndSaveWordsToJSON


class TestLevel(QWidget):
    current_position = 0
    words:Words
    correct_answer = 0
    path_file = '/'

    def __init__(self, words: Words, path_file=''):
        super().__init__()
        self.load_ui()
        self.label_check.setHidden(True)

        self.words = words
        self.change_view_word(self.current_position)
        self.path_file = path_file

    def load_ui(self):
        self.window = uic.loadUi("../uis/test_level.ui", self)

    def show_word(self, word:Word=Word('Example')):
        self.label_word.setText(f'{word.name.__str__()}\n{word.transcription}'
                                f'\n{word.translations[0].translation}')

    def set_setting_view_word(self, position):
        if self.words.words[position].isRight:
            self.set_right_answer()
        elif self.words.words[position].isRight == None:
            self.set_default_answer()
        else:
            self.set_wrong_answer()

    def set_right_answer(self):
        pixmap = QPixmap('../../icons/checked.png')
        self.but_check.setEnabled(False)
        self.label_right.setPixmap(pixmap)
        self.label_right.setHidden(False)

    def set_wrong_answer(self):
        pixmap = QPixmap('../../icons/wrong.png')
        self.label_right.setPixmap(pixmap)
        self.but_check.setEnabled(True)
        self.label_right.setHidden(False)

    def set_default_answer(self):
        pixmap = QPixmap()
        self.but_check.setEnabled(True)
        self.label_right.setHidden(True)
        self.label_right.setPixmap(pixmap)

    def change_view_word(self, position):
        self.show_word(self.words.words[position])
        self.label_count_list.setText(f'{position + 1}/{len(self.words.words)}')
        self.set_setting_view_word(position)

    def on_but_next_released(self):
        self.current_position += 1
        if self.current_position >= len(self.words.words):
            self.current_position = 0
        self.change_view_word(self.current_position)

    def on_but_back_released(self):
        self.current_position -= 1
        if self.current_position < 0:
            self.current_position = len(self.words.words)-1
        self.change_view_word(self.current_position)

    def on_but_check_released(self):
        if self.check_answer(self.words.words[self.current_position].answer):
            self.check_right_answer()
        else:
            self.check_wrong_answer()
        self.show_label_check_per_second()
        self.on_but_next_released()
        ConvertAndSaveWordsToJSON().saveWordsToJSONFile(self.words, self.path_file)

    def show_label_check_per_second(self):
        hide_label_timer = Timer(0.5, self.hide_label_check).start()
        self.label_check.setHidden(False)

    def hide_label_check(self):
        self.label_check.setHidden(True)

    def check_right_answer(self):
        self.correct_answer += 1
        self.reward()
        self.label_correct_answer.setText(self.correct_answer.__str__())
        self.words.words[self.current_position].isRight = True
        pixmap = QPixmap('../../icons/checked.png')
        self.label_check.setPixmap(pixmap)

    def reward(self):
        if self.correct_answer < 1:
            self.words.words[self.current_position].correct_answer += 1

    def check_wrong_answer(self):
        self.words.words[self.current_position].isRight = False
        pixmap = QPixmap('../../icons/wrong.png')
        self.label_check.setPixmap(pixmap)

    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key.Key_Up.value or key == 16777249:
            self.on_but_back_released()
        elif key == Qt.Key.Key_Down.value or key == 16777251:
            self.on_but_next_released()
        elif key == 16777220:
            self.on_but_check_released()
        event.accept()

    def check_answer(self, answer):
        return True

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
    win = TestLevel(only_unknown, path_file)
    win.show()
    sys.exit(app.exec())