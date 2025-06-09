import re
from typing import List

from code.data.Translation import Translation
from code.data.Words import Words
from code.data.Word import Word


class ConvertFileWordsToWords:
    words: Words = Words()

    def __init__(self, path_file):
        self.words = self.get_words_from_file(path_file)

    def get_words_from_file(self, path_file):
        words: Words = Words()
        with open(path_file, "r") as file:
            for line in file:
                if line.__len__() > 1:
                    parse_word = self.parse_word_by_line_text(line.rstrip())
                    words.words.append(parse_word)
        return words

    def parse_word_by_line_text(self, text: str):
        index = text.find('[')
        word = Word()
        if not index == -1:
            word.name = text[:index].strip()
            index_end = text.find(']')
            word.transcription = text[index:index_end + 1].strip()
            split_text = text[index_end + 1:].strip().split(',')
            for t in split_text:
                word.translations.append(Translation(t))
        else:
            pattern_en = re.compile("[A-Za-z]+")
            pattern_ru = re.compile("[А-Яа-я]+")
            words_en = pattern_en.findall(text)
            words_ru = pattern_ru.findall(text)
            word.name = ' '.join(words_en)
            word.transcription = ''
            split_text = ' '.join(words_ru).split(',')
            for t in split_text:
                word.translations.append(Translation(t))
        return word

    def get_words(self):
        return self.words

if __name__ == "__main__":
    path = '/home/chris/Yandex.Disk/Mind/English/Movies/TheBigBangTheory/Season 1/wordsS1E1.txt'
    _words = ConvertFileWordsToWords(path)
    words:Words = _words.get_words()
    for w in words.words:
        print(w)