import math 
r = float(input("podaj promień koła: "))
pole = math.pi * r ** 2
obwod = 2 * math.pi * r
print(f'Pole koła wynosi: {pole:.2f}')
print(f'Obwód koła wynosi: {obwod:.2f}')