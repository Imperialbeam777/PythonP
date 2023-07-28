# conversion 
## en py se puede identificar el tipo de dato de una variable 
# por medio de la conversion 
## int 
numero=int(3.45)
print(numero)
print(type(numero))
numero=str(3)
print(numero)
print(type(numero))
numero=int(45)
print(numero)
print(type(numero))
## float 
decimal=float(12)
print(decimal)
print(type(decimal))
decimal=float("45.3")
print(decimal)
print(type(decimal))
decimal=float(78.2)
print(decimal)
print(type(decimal))
# Tipos de datos incorporados 
# tipo texto   srt
# tipos numericos int, float, complex
# tipos secuencia list, tuplas, range 
# tipo de mapeo  dict
# boolean bool
# tipos binario bytes,bytearray,memoryview
# ningun tipo Nonetype
# complex
# los numeros complejos se escribe con una "j" como parte imaginaria 
x=3+5j
print(x)
y=5j
print(y)
z=-5j
print(z)
## numeros aleatorios 
## py no tiene una funcion random() para trabajar con numeros aleatorios 
# pero tiene un nmodulo integrado llamado random que se puede usar para realizar numeros aleatorios
import random
print(random.randrange(1,101))# 0,100 omitiendo el 101
## py random tiene un conjunto de metodos 
# randint()
print(random.randint(1,100))
## getStates()
print(random.getstate())
# random()
print(random.random())

