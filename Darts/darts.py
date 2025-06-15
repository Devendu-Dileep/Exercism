import math
def score(x, y):
    dist=math.sqrt(x**2+y**2)
    return (0 if dist>10 else 1 if 5<dist<=10 else 5 if 1<dist<=5 else 10)
    
    
