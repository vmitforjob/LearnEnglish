import json
from email.policy import default

from code.data.Word import Word
from code.data.Words import Words
from code.data.WordsEncoder import WordsEncoder


class ConvertAndSaveWordsToJSON:
    def saveWordsToJSONFile(self, words:Words, name_file='test'):
        with open(f'../../source/listsWordsOnJSON/{name_file}.json', 'w', encoding='utf-8') as outfile:
            outfile.write(json.dumps(words, indent=4, cls=WordsEncoder, ensure_ascii=False))

    def loadWordsFromJSON(self, path_file):
        with open(f'../../source/listsWordsOnJSON/{path_file}', 'r') as outfile:
            words = Words()
            if outfile.read():
                outfile.seek(0)
                wordsFromFile:Words = words.from_json(json.dumps(json.load(outfile)))
                for w in wordsFromFile.words:
                    words.words.append(w)
        return words