import re
def clean_punc(str):
    """
    Removes the punctuation signs from the data.
    """
    punc = '!()[]{};”─+… :—“"…``\,- <>./?……@#…$%^&*_~……'
    for i in str:
        if i in punc:
            str = str.replace(i, " ")
    return str

try:
    with open("cleaned_poems.txt", 'r', encoding="utf-8") as f:
        data = f.read()
    with open("cleaned_poems.txt", "w+", encoding="utf-8") as f:
        f.write(clean_punc(data))
    print("Cleaned the punctuations from the data.")
except FileNotFoundError:
    print("File not found")

def clean_titles(str):
    """
    Removes the poem titles in the data.
    """
    return re.sub(r'\S[A-Z]|.+ ?[A-Z]?\S*(?=[A-Z]|[ŞÇÜĞÖ][a-z]+)', "", str)

try:
    with open("cleaned_poems.txt", 'r', encoding="utf-8") as f:
        data = f.read()
    with open("cleaned_poems.txt", "w+", encoding="utf-8") as f:
        f.write(clean_titles(data))
    print("Cleaned the titles in the data.")
except FileNotFoundError:
    print("File not found")

def lower(str):
    """
    Lowers all the characters in the data.
    """
    for i in str:
        return str.lower()

try:
    with open("cleaned_poems.txt", 'r', encoding="utf-8") as f:
        data = f.read()
    with open("cleaned_poems.txt", "w+", encoding="utf-8") as f:
        f.write(lower(data))
    print("Lowered all the characters in the data.")
except FileNotFoundError:
    print("File not found")

def clean_num(str):
    """
    Removes the numbers from the data.
    """
    return ''.join(i for i in str if not i.isnumeric())

try:
    with open("cleaned_poems.txt", 'r', encoding="utf-8") as f:
        data = f.read()
    with open("cleaned_poems.txt", "w+", encoding="utf-8") as f:
        f.write(clean_num(data))
    print("Cleaned the numbers in the data.")
except FileNotFoundError:
    print("File not found")
