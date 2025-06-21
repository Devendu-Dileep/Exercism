import string 


def is_pangram(sentence):
    lower_sentence = sentence.lower()
    return all(i in lower_sentence for i in string.ascii_lowercase)