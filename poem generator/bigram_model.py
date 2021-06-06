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


def singleverse(num):
    """Output the generated poem line."""
    tokens = tokenize()
    i = 1
    dict = {}
    count = num
    for word in tokens[i:]:
        key = tokens[i - 1]
        if key in dict:
            dict[key].append(word)
        else:
            dict[key] = [word]
        i += 1
    word1 = random.choice(list(dict.keys()))
    poem = word1.capitalize()
    while len(poem.split(' ')) < count:
        word2 = random.choice(dict[word1])
        word1 = word2
        poem += ' ' + word2
    banned_end_words = ["ve", "ile", "bir", "o", "ne", "daha", "en", "ay", "çok"] #Doesn't work
    if poem[-1] in banned_end_words:
        poem.replace(poem[-1], '')
    print(poem)


def firstverse(num, seedword):
    """Creates a different poem line that takes an input as the seedword."""
    tokens = tokenize()
    i = 1
    dict = {}
    count = num
    for word in tokens[i:]:
        key = tokens[i - 1]
        if key in dict:
            dict[key].append(word)
        else:
            dict[key] = [word]
        i += 1
    word1 = seedword
    poem = word1.capitalize()
    while len(poem.split(' ')) < count:
        word2 = random.choice(dict[word1])
        word1 = word2
        poem += ' ' + word2
    banned_end_words = ["ve", "ile", "bir", "o", "ne", "daha", "en", "ay", "çok"]
    if poem[-1] in banned_end_words:
        poem.replace(poem[-1], '')
    print(poem)


def generate():
    """Generates the final poem with user input of structure."""
    print("What structure do you want?(e.g., 3 x 4, 2 x 4, 2 x 5): ")
    x, y, z = input().split()
    print("How many words in a line do you want?: ")
    num = int(input())
    seedword = str(input("Enter a seed word: "))
    for stanza in range(1):
        for first_verse in range(1):
            firstverse(num, seedword)
        for verse in range(int(z) - 1):
            singleverse(num)
        print('\n')
    for stanza in range(int(x) - 1):
        for verse in range(int(z)):
            singleverse(num)
        print('\n')


generate()
