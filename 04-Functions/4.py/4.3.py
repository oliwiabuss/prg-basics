import math

def pole_trojkata(a,b,c):
    s = (a + b + c )/ 2
    p = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return p 

a = int(input("podaj bok 1; "))
b = int(input("podaj bok 2: "))
c = int(input("podaj bok 3: "))
pole = pole_trojkata(a,b,c)
print(pole)