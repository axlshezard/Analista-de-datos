import random
list_multplicaciones = [(r.randint(1,10),r.randint(1,10)) for i in range(10)]
def juego_multiplicar(cont:int, multiplicacion:tuple)->int:
    resultado = (Multi[0])*(multi[1])
    respuesta = int(input(f"{Multi[0]}*{multi[1]} "))
    if respuesta == resultado:
        cont+=1
        return cont
    else:
        print(f"Error la respuesta correcta es = {resultado}")
        puntos = reduce(juego_multiplicar,list_multplicaciones,0)


