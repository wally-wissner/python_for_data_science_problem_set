import nltk
import re
from nltk.corpus import words


nltk.download()


def adage_exception(word):
    return re.match("(cie)|([^c]ei)", word)


if __name__ == "__main__":
    for word in sorted(words.words()):
        if word.lower() == word and adage_exception(word):
            print(word)
