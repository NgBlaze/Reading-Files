from collections import Counter


def read_file_content(filename):
    f = open(filename, "r")
    text = f.read()
    return text


def count_words():
    text = read_file_content("./story.txt")
    words = text.split()
    print(Counter(words))


count_words()
