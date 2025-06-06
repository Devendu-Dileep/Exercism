def is_armstrong_number(number):
    sum=0
    for i in str(number):
        sum=int(i)**len(str(number))+sum
    return sum==number
    #return sum([int(x)**len(str(number)) for x in str(number)]) == number


        
