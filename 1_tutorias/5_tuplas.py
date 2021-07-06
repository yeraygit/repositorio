'''
-----------------Caracteristicas-------------------
* Las tuplas son inmutables, no se pueden modificar despues de su creacion.
        + No permiten: añadir,eliminar, mover elementos (no append,extend,remove).
        + Permiten extraer porciones, pero el resultado es un tupla nueva.
        + No permiten busquedas (no index).
        + Si permite comprobar si un elemento se encuentra en una lista.

* Ventaja correspecto a las listas:
        + Mas rapidas.
        + Menos espacios.
        + Formatean Strings
        + pueden utilizarse como claves en un diccionario.
'''

tupla = ("Yeray",12,25.5,True)
print(tupla[:])
print('-------------------------------------------------------------')

lista = list(tupla)
print(lista[:])
print('-------------------------------------------------------------')

tupla = tuple(lista)
print(tupla)
print('-------------------------------------------------------------')
print()

print('Yeray' in tupla)
print(len(tupla))
print('-------------------------------------------------------------')
print()

tupla = ('España',) # tupla unitaria (poner la coma al final de los elementos)
print(len(tupla))
print('-------------------------------------------------------------')
print()

tupla = 'Gabriel',22,'Venezolano' # empaquetado de tupla
print(tupla)

nombre,años,nacionalidad = tupla # desempaquetado de tupla (destructuring)
print(nombre)
print(años)
print(nacionalidad)
