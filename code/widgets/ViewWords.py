import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication

from code.data.Translation import Translation
from code.data.Word import Word


class ViewWord(QWidget):
    def __init__(self, word:Word='Empty'):
        super().__init__()
        self.window = uic.loadUi("../uis/view_word.ui", self)

        self.label_word.setText(word.name)
        self.label_transcription.setText(word.transcription)
        self.label_translate.setText(word.translations[0].translation)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    word = Word(name='word for test',
                transcription='[word for test]',
                translations=[Translation('слово для теста'), Translation('дополнение для примера')])
    win = ViewWord(word)
    win.show()
    sys.exit(app.exec())