"""Word Finder: finds random words from a dictionary."""


from random import Random
import random


class WordFinder:
    """finds random words from a file located in this directory"""
    def __init__(self):
        "Look for a words.txt file and read number of words. Print result."
        self.count = self.read_and_count() 
        self.d = self.build_dict_out_of_words()
    from random import randrange
     
    def read_and_count(self):
        count = 0
        words = open("words.txt", "r")
        for line in words:
            count += 1
        words.seek(0)
        words.close()
        return count

    def build_dict_out_of_words(self):
        l = []
        words = open("words.txt", "r")
        for line in words:
            l.append(line.strip())
        words.seek(0)
        words.close()
        d={}
        keys = range(self.count)
        for i in keys:
            d[i] = l[i]
        return d

    def random(self):
        ran = random.randrange(self.count)
        return self.d[ran]

class SpecialWordFinder(WordFinder):
    def __init__(self):
        super().__init__()

    def build_dict_out_of_words(self):
        l = []
        words = open("words.txt", "r")
        for line in words:
            if line.strip() and not line.startswith("#"):
                l.append(line.strip())
        words.seek(0)
        words.close()
        d={}
        keys = range(self.count)
        for i in keys:
                d[i] = l[i]
        return d

