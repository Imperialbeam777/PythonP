## cadenas py
# las cadenas se trabajan en " o ' 
# la funcion print para mostar texto ""
# cadena multilinea 
# podemos asiganar una cadena a una variable usando 3 comillas dobles
txt="""
 es simplemente el texto de relleno de las imprentas y 
 archivos de texto. Lorem Ipsum ha sido el texto de relleno 
 estándar de las industrias desde el año 1500, cuando un impresor 
 (N. del T. persona que se dedica a la imprenta) desconocido usó una 
 galería de textos y los mezcló de tal manera que logró hacer un libro
 de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó
 como texto de relleno en documentos electrónicos, quedando esencialmente 
 igual al original. Fue popularizado en los 60s con la creación de las hojas "Letraset",
 las cuales contenian pasajes de Lorem Ipsum, y más recientemente con software de .
 autoedición, como por ejemplo Aldus PageMaker, el cual incluye versiones de Lorem 
 Ipsum.
"""
print(txt)
txt1="Lorem Ipsum es simplemente el texto de relleno de las"
#Nota: en el resultado, los saltos de linea se insertan en la misma posicion que en el codigo
# las cadenas son matrices 
# se puede acceder a los elementos de la cadena por corchetes 
print(txt[5])
# una cadena atraves de un ciclo 
for elemento in txt:
    print(elemento)
# len() para obtener la longitud de una cadena 
print(len(txt))
## Comprobar cadenas 
print("año 150" in txt)
## not in 
print("relleno" not in txt)

### ejercio 
## 1. valide si las palabras simplemente,estándar,estandar,(.)," ",(,) # existen
## 2. valide si las palabras juan,archivos,estan,hola,tex," ",(,) # No existen
# 3. recorrer en for txt y validar si el caracter i existe y la cantidad
# 4. recorrer en for txt y validar si el caracter " " existe y la cantidad
# 5. recorrer en for txt y validar si el caracter , existe y la cantidad
# 6. recorrer en for txt y validar si el caracter Lorem no existe y la cantidad en caso de que exista 0
# 7. recorrer en for txt y validar si el caracter hola no existe y la cantidad en caso de que exista 0
## cortar cadena
## rango
print(txt[:100])## no incluye el 100 -> 0,99
print("-----------------------------------------------------")
print(txt[100:])## no incluye el 100 -> 0,99
## negativa
b=" Hola, mundo!"
print(b[:-1])

## realizar un ejercio basico con el random() float y vamos a cortar el numero 1:3,inicio:6 y del fin:-4
## cadena sacar la longitud, inicio hasta longitud 
## Upper case
## Lower case
## strip #Ana
## replace # esteban
# split # johan
# count # juan camilo
# find # juan jose}

## En Python, el método find() se utiliza para buscar la primera ocurrencia de una subcadena dentro de otra cadena. Este método devuelve el índice de la primera 
# aparición de la subcadena si se encuentra, o -1 si no se encuentra ninguna coincidencia.
##La sintaxis general del método find() es la siguiente:

cadena="Hola, este es un ejemplo de find en Python."

indice = cadena.find("ejemplo")
print(indice)

buscar= cadena.find("juan")
print(buscar)

encuentra = cadena.find("es", 1, 20)  #rangos
print(encuentra)  


# format # maria camila
# index # santiago
# join # sebastian 
# translate # thomas 


"""

Para una campaña de salud se requiere determinar de un

grupo de N personas cuantos pueden beneficiarse.

Serán beneficiarios quienes siendo mujeres no pasen

de 30 años y quienes siendo hombres no superen los 35 años.

La campaña es solo para estratos 1 y 2. Se debe mostrar:

 

a. Cuantos hombres son beneficiados

b. Cuantas mujeres son beneficiadas

c. Mostrar el promedio de edad de hombres beneficiados

d. Mostrar el promedio de edad de mujeres beneficiadas

Indicar mediante un mensaje cuando no se es beneficiado."""

def calcular_beneficiados(personas):
    beneficiados_hombres = []
    beneficiados_mujeres = []
    suma_edad_hombres = 0
    suma_edad_mujeres = 0
    cantidad_hombres = 0
    cantidad_mujeres = 0

    for persona in personas:
        genero, edad, estrato = persona

        if genero == "M" and edad <= 35 and estrato in ["1", "2"]:
            beneficiados_hombres.append(edad)
            suma_edad_hombres += edad
            cantidad_hombres += 1

        elif genero == "F" and edad <= 30 and estrato in ["1", "2"]:
            beneficiados_mujeres.append(edad)
            suma_edad_mujeres += edad
            cantidad_mujeres += 1

    # Preguntas a, b, c y d
    print("a. Cuantos hombres son beneficiados:", cantidad_hombres)
    print("b. Cuantas mujeres son beneficiadas:", cantidad_mujeres)

    if cantidad_hombres > 0:
        promedio_edad_hombres = suma_edad_hombres / cantidad_hombres
        print("c. Promedio de edad de hombres beneficiados:", promedio_edad_hombres)
    else:
        print("c. No hay hombres beneficiados.")

    if cantidad_mujeres > 0:
        promedio_edad_mujeres = suma_edad_mujeres / cantidad_mujeres
        print("d. Promedio de edad de mujeres beneficiadas:", promedio_edad_mujeres)
    else:
        print("d. No hay mujeres beneficiadas.")


# Ejemplo de uso del programa
personas = [("M", 28, "2"),
            ("F", 32, "1"),
            ("M", 40, "1"),
            ("F", 25, "2"),
            ("F", 28, "1")]

calcular_beneficiados(personas)







