def convert(number):
    number=int(number)
    res=""
    if number%3==0:
        res+="Pling"
    if number%5==0:
        res+="Plang"
    if number%7==0:
        res+="Plong"
    return res if res!="" else str(number)
# same as return res or str(number)-or returns first true value
    
    
