"""
An old adage of English spelling claims "i" before "e" except after "c". Print all the English words for which this
adage does not hold true. That is, all words containing "cie" or "Xei" where X is not a "c". Don't print proper nouns.
"""


import nltk
import re
from nltk.corpus import words


nltk.download()


def adage_exception(word):
    return re.match(..., word)


if __name__ == "__main__":
    for word in sorted(words.words()):
        if word.lower() == word and adage_exception(word):
            print(word)
