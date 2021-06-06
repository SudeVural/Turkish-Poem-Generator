
import random

def tokenize():
    """Tokenizes and cleans the poems."""
    poems = open("cleaned_poems.txt", "r", encoding='utf-8').read()
    words = poems.split()
    unwanted_tokens = ['i', 'e', 'a', 'ö', 'ı', 'u', 'ü', 'b', 'c', 'ç,', '’', 'guk', 'lir', 'd', 'f', 'g', 'ğ',
                       'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z', 'ir', "'",
                       "'üç", 'kiki', 'muc’ın', 'x', 'iiçimde', 'ssağ', 'vvar', 'hhissim', 'gu', 'lee', 'na',
                       'gabriel', "straits'in", "'sabahattin", 'kkabul', "böylece'", 'se', 'nin', '””hayatın',
                       "yi", 'lık', "ming", "'rivayetdi"]
    filtered_tokens = []
    for w in words:
        if w not in unwanted_tokens:
            filtered_tokens.append(w)
    return filtered_tokens

def firstverse(num): #Doesn't work perfectly.
    """Tokenizes, creates a dictionary and generates the first line of the poem with given length."""
    def create_dict():
        """Creates a dictionary with key value pairs"""
        tokens = tokenize()
        dic = {}
        for words in range(0, len(tokens) - 2):
            couple = "{0} {1}".format(tokens[words], tokens[words + 1])
            value = tokens[words + 2]
            dic.setdefault(couple, []).append(value)
        return dic

    def create_line(num, dic, seedword):
        """Generates a poem line"""
        keys = list(dic.keys())
        filtered_words = keys[random.randint(0, len(keys) - 1)]
        poemline = filtered_words.split(" ")
        while len(poemline) < num:
            new_key = "{0} {1}".format(poemline[-2], poemline[-1])
            if new_key in dic:
                temp = seedword
                poemline.append(temp)
            else:
                temp = keys[random.randint(0, len(keys) - 1)]
                temp = temp.split(" ")
                poemline = poemline + temp
        poemline = poemline[0:num]
        return poemline

    def printoutline(num):
        """Prints out a poem line with given length."""
        dict = create_dict()
        line = create_line(num, dict, seedword=input(("Enter a seed word: ")))
        joined = " ".join(line)
        poem = joined.capitalize()
        return poem
    finalline = printoutline(num)
    banned_end_words = ["ve", "ile", "bir", "o", "ne", "daha", "en", "ay", "çok", "her"]
    if finalline[-1] in banned_end_words:
        finalline.replace(finalline[-1], '')
    print(finalline)

def singleverse(num):
    """Creates a dictionary and generates a poem line with given length."""
    def create_dict():
        """Creates a dictionary with key value pairs in the form of a trigram"""
        tokens = tokenize()
        dic = {}
        for words in range(0, len(tokens) - 2):
            couple = "{0} {1}".format(tokens[words], tokens[words + 1])
            value = tokens[words + 2]
            dic.setdefault(couple, []).append(value)
        return dic

    def create_line(num, dic):
        """Creates a poem line"""
        keys = list(dic.keys())
        filtered_words = keys[random.randint(0, len(keys) - 1)]
        poemline = filtered_words.split(" ")
        while len(poemline) < num:
            new_key = "{0} {1}".format(poemline[-2], poemline[-1])
            if new_key in dic:
                temp = random.choice(dic[new_key])
                poemline.append(temp)
            else:
                temp = keys[random.randint(0, len(keys) - 1)]
                temp = temp.split(" ")
                poemline = poemline + temp
        poemline = poemline[0:num]
        return poemline

    def printoutline(num):
        """Prints out a poem line with given length."""
        dict = create_dict()
        line = create_line(num, dict)
        joined = " ".join(line)
        poem = joined.capitalize()
        return poem
    finalline = printoutline(num)
    banned_end_words = ["ve", "ile", "bir", "o", "ne", "daha", "en", "ay", "çok"]
    if finalline[-1] in banned_end_words:
        finalline.replace(finalline[-1], '')
    print(finalline)


def generate():
    """Generates the final poem with user input of structure."""
    print("What structure do you want?(e.g., 3 x 4, 2 x 4, 2 x 5): ")
    x, y, z = input().split()
    # print("Enter a seed word: ")
    print("How many words in a line do you want?: ")
    num = int(input())
    for stanza in range(1):
        for first_verse in range(1):
            firstverse(num)
        for verse in range(int(z)-1):
            singleverse(num)
        print('\n')
    for stanza in range(int(x)-1):
        for verse in range(int(z)):
            singleverse(num)
        print('\n')

generate()
