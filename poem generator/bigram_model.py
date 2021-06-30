import random
import nltk
from scipy import stats
from torchtext.data import get_tokenizer


def tokenize():
    """Tokenizes and cleans the poems."""
    with open("cleaned_poems.txt", "r", encoding='utf8') as f:
        corpus = f.read()

    corpus2 = corpus.split('\n')
    corpus1 = ["<s> " + sent + " </s>" for sent in corpus2]
    tokenizer = get_tokenizer('basic_english') # Not an english tokenizer, just an argument.
    tokens = []
    for s in corpus1:
        tokens += tokenizer(s)

    unwanted_tokens = ['i', 'e', 'a', 'ö', 'ı', 'u', 'ü', 'b', 'c', 'ç,', '’', 'guk', 'lir', 'd', 'f', 'g', 'ğ',
                       'h', 'j', 'k', 'l', 'm', 'n', 'p', 'r', 's', 'ş', 't', 'v', 'y', 'z', 'ir', "'",
                       "'üç", 'kiki', 'muc’ın', 'x', 'iiçimde', 'ssağ', 'vvar', 'hhissim', 'gu', 'lee', 'na',
                       'gabriel', "straits'in", "'sabahattin", 'kkabul', "böylece'", 'se', 'nin', '””hayatın',
                       "yi", 'lık', "ming", "'rivayetdi", "peking", "huu", "ı'dir", "hokkaömeroğlu", "topluiğne",
                       "gcceye", "'uzaklara", "'coşkun", "'of'", "bü'yü'r", "zararı'", "yo", "başlıyor'", "eğe",
                       "olmuşt", "lü", "fazy", "tü", "ydu", "nl" "dı", "çifşeşmeye", "sy", "www", "nurican", "mutluk"
                        "olmyan", ]  # Words with typos that shouldn't appear in the poem.
    filtered_tokens = []
    for w in tokens:
        if w not in unwanted_tokens:
            filtered_tokens.append(w)
    return filtered_tokens


filtered_tokens = tokenize()
random_choice_list = []  # A list to randomly choose a word without start and end tokens.
for i in filtered_tokens:
    if i != "<s>" and i != "</s>":
        random_choice_list.append(i)


def singleverse(num): # Takes an argument for the length of the line.
    """
    Generates bigrams, calculates their frequency and probabilities and
    generates a poem line starting with a random word.
    """
    ts_bigrams = [(filtered_tokens[i], filtered_tokens[i + 1]) for i in range(len(filtered_tokens) - 1)]
    bigram_cfd = nltk.ConditionalFreqDist(ts_bigrams)
    bigram_pbs = nltk.ConditionalProbDist(bigram_cfd, nltk.MLEProbDist)

    seedword = random.choice(random_choice_list)
    banned_words = ['ile', 'misin', 'mısın', 'müsün', 'musun', 'mi', 'mu', 'mı', 'mü', 've', 'gibi']  # Limits the  words that can appear line initially.
    if seedword in banned_words:
        seedword = random.choice(random_choice_list)
    else:
        seedword = seedword
    start_word = seedword.lower()
    data = []
    for i in range(num):
        probable_words = list(bigram_pbs[start_word].samples())
        word_probabilities = [bigram_pbs[start_word].prob(word) for word in probable_words]
        result = stats.multinomial.rvs(1, word_probabilities)
        index_of_probable_word = list(result).index(1)
        start_word = probable_words[index_of_probable_word]
        data.append(start_word)

    line = []
    a = seedword
    line.insert(0, a)
    for i in data:
        if i != "<s>" and i != "</s>":  # Removes start and end tokens from the output.
            line.append(i)
    poem_line = ' '.join([str(i) for i in line])

    line_words = poem_line.split()
    banned_end_words = ['ile', 've', 'bir', 'her', 'bu', 'şu', 'bi', 'in']  # Limits the words that can appear as final.
    if line_words[-1] in banned_end_words:
        line_words.remove(line_words[-1])
    line = ' '.join([str(i) for i in line_words]).capitalize()
    print(line)


def firstverse(num, seedword):  # Takes two arguments for length of line and start word.
    """
    Generates bigrams, calculates their frequency and probabilities and
    generates a poem line with given input.
    """
    ts_bigrams = [(filtered_tokens[i], filtered_tokens[i + 1]) for i in range(len(filtered_tokens) - 1)]

    bigram_cfd = nltk.ConditionalFreqDist(ts_bigrams)
    bigram_pbs = nltk.ConditionalProbDist(bigram_cfd, nltk.MLEProbDist)

    start_word = seedword
    data = []
    for i in range(num):
        probable_words = list(bigram_pbs[start_word].samples())
        word_probabilities = [bigram_pbs[start_word].prob(word) for word in probable_words]
        result = stats.multinomial.rvs(1, word_probabilities)
        index_of_probable_word = list(result).index(1)
        start_word = probable_words[index_of_probable_word]
        data.append(start_word)

    line = []
    a = seedword
    line.insert(0, a)
    for i in data:
        if i != "<s>" and i != "</s>":
            line.append(i)
    poem_line = ' '.join([str(i) for i in line])

    line_words = poem_line.split()
    banned_end_words = ['ile', 've', 'bir', 'her', 'bu']
    if line_words[-1] in banned_end_words:
        line_words.remove(line_words[-1])
    line = ' '.join([str(i) for i in line_words]).capitalize()
    print(line)


def generate():
    """Generates the final poem with user input of structure."""
    print("What structure do you want?(e.g., 3 x 4, 2 x 4, 2 x 5): ")
    while True:
        try:
            x, y, z = input().split()  # Input for poem structure.
        except:
            print("Enter the structure as shown above")
            continue
        break
    num = random.randint(7, 8)
    while True:
        seedword = str(input("Enter a seed word: "))  # Input for start word.
        try:
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
        except IndexError:
            print("This was not a valid seed word please try again.")
            continue
        break


generate()
