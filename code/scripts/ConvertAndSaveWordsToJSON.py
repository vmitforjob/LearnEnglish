import json

from code.data.Words import Words
from code.data.WordsEncoder import WordsEncoder


class ConvertAndSaveWordsToJSON:
    def saveWordsToJSONFile(self, words:Words, name_file='test'):
        with open(f'../../source/{name_file}.json', 'w') as outfile:
            outfile.write(json.dumps(words.words, indent=4, cls=WordsEncoder, ensure_ascii=False))
