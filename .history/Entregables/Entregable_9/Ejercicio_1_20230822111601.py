import random as randint
from functools import reduce

listmultplicaciones = [(r.randint(1,10),r.randint(1,10)) for i in range(10)]

def juego_multiplicar(cont:int, multiplicacion:tuple)->int:
    resultado = mult[0] * mult[1]
    respuesta = int(input(f"{Mult[0]} * {mult[1]} "))
    if respuesta == resultado:
        cont+=1
        return cont
    else:
        print(f"Error la respuesta correcta es = {resultado}")
        return cont

puntos = reduce(juego_multiplicar,listmultplicaciones,0)    

