def steps(number):
    try:
        number = int(number)
        if number < 1:
            raise ValueError("Only positive integers are allowed")
        step=0
        while True:
            if number==1:
                    break
            #no need of the above two lines if while number!=1:(This is better)
            if number%2==0:
                number//=2
                step +=1
            else:
                number=number*3+1
                step +=1
            #number= number//2 if number%2==0 else number*3+1
            #step+=1
        return step        
    except (ValueError,TypeError) as e:
        raise e
