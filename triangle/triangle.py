def equilateral(sides):
    a,b,c=sides
    if a!=0:
       return a==b==c 
    return False
   


def isosceles(sides):

    a,b,c=sides
    if (a+b>=c and b+c>=a and a+c>=b):
       return (a==b or b==c or a==c or equilateral(sides))
    else:
       return False


def scalene(sides):
    a,b,c=sides
    if (a+b>=c and b+c>=a and a+c>=b):
       return not(a==b or b==c or a==c)
    else:
       return False
