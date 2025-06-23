def rotate(text, key):
    stri = ""
    for i in text:
        if i.isalpha():
            cased = ord('A') if i.isupper() else ord('a')
            pos = ord(i) - cased 
            stri += chr((pos + key) % 26 + cased)
        else:
            stri += i
    return stri



    
       
