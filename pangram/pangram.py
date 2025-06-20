import string
def is_pangram(sentence):
    Alphabet=set(string.ascii_lowercase)
    return Alphabet.issubset(sentence.lower())
       

    
    
