import sys

from PyQt6 import uic, QtWidgets
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit

from code.data.Words import Words
from code.scripts.ConvertAndSaveWordsToJSON import ConvertAndSaveWordsToJSON
from code.scripts.ConvertFileWordsToWords import ConvertFileWordsToWords
from code.widgets.ViewWords import ViewWord


class CreateListWords(QWidget):
    words: Words = Words()

    def __init__(self):
        super().__init__()
        self.window = uic.loadUi("../uis/create_list_words.ui", self)

    def on_but_load_list_words_released(self):
        path_file = QtWidgets.QFileDialog.getOpenFileName(self, "Выбрать файл", "/", "*.txt")[0]
        self.line_uri.setText(path_file)
        convert = ConvertFileWordsToWords(path_file)
        self.words = convert.get_words()
        for w in self.words.words:
            self.create_widget(w)

    def on_but_save_released(self):
        if self.valid_list():
            convert = ConvertAndSaveWordsToJSON()
            convert.saveWordsToJSONFile(self.words, self.line_name_list.text())
            print('Сохранено')
        else:
            print('Не правильно!')#TheBigBangtheoryS1E1

    def valid_list(self):
        if not self.words.words:
            return False
        if len(self.line_name_list.text()) < 1:
            return False
        return True

    def on_but_cancel_released(self):
        pass

    def create_widget(self, vList):
        card = ViewWord(vList)
        self.layout_scroll.addWidget(card)

# with open('testWord.json', 'w') as outfile:
#     outfile.write(json.dumps(words, indent=4, cls=WordsEncoder, ensure_ascii=False))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = CreateListWords()
    win.show()
    sys.exit(app.exec())