import json

from code.data.Translation import Translation
from code.data.Word import Word
from code.data.Words import Words


class WordsEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Words):
            return {
                'words': obj.words
            }
        elif isinstance(obj, Word):
            return {
                'name': obj.name,
                'transcription': obj.transcription,
                'translations': obj.translations,
                'skill': obj.skill,
                'correct_answer': obj.correct_answer
            }
        elif isinstance(obj, Translation):
            return {
                'translation': obj.translation
            }
        return super().default(obj)