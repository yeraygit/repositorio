'''
* Estructura de datos que nos permite almacenar valores de diferente tipo 
(enteros, cadenas de texto, decimales) e incluso listas y otros diccionarios.

* La principal caracteristicas de los diccionarios es que los datos se 
almecenan asociados a una clave de tal forma que se crea una asociacion de tipo
clave:valor para cada elemento almacenado.

* Los elementos almacenados no estan ordenados. El orden es indiferente a la hora de almacenar
infomación de un diccionario.
'''

persona = {'nombre':'Gabriel','apellido':'Paz','sexo':'Masculino'}
print(persona['nombre'])

persona['dni']='1234?'
print(persona)

persona['dni']='1234'
print(persona)

del persona['dni']
print(persona)

persona[1]=23
print(persona)
#               0          1       2
atributos = ('nombre','apellido','sexo')

persona = {atributos[0]:'Gabriel',atributos[1]:'Paz',atributos[2]:'masculino'}
print(persona)

persona = {atributos[0]:'Gabriel',atributos[1]:'Paz',atributos[2]:'masculino','hijos':['manuel','oriana']}
print(persona)

persona = {atributos[0]:'Gabriel',atributos[1]:'Paz',atributos[2]:'masculino','hijos_apellido':{'manuel':'Paz Guedez','oriana':'Paz Herrera'}}

hijos_apellido = persona['hijos_apellido']
hijos_apellido['manuel']

print(persona['hijos_apellido']['manuel'])

print(persona.keys())
print(persona.values())
print(len(persona))