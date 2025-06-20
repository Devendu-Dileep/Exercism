from string import ascii_lowercase
def is_pangram(sentence):
    return all(i in sentence.lower() for i in ascii_lowercase)
       

    
    
