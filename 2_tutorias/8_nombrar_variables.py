'''
    solo hay 64 caracteres validos para declarar un variable
        +   las letras del abecedario en mayusculas y minusculas, numeros , $ , _
        +   los demas caracteres se pueden usar como nombres de variables pero no son parte de la comvecion        

'''
#-------------------formatos para declarar variables-----------------------
#camelCase 
lenguajeDeProgramacionFavorito = 'python'

#PascalCase
LenguajeDeProgramacionFavorito = 'javaScript'

#SNAKE_CASE se suele usar para variables de solo lectura (variables constantes inmutables)
LENGUAJE_DE_PROGRAMACION_FAVORITO = 'java'

MAX_LONGITUD_NOMBRE = 80

def validarNombre(nombre = ''):
    if len(nombre) >= MAX_LONGITUD_NOMBRE:
        return 'El nombre es demasiado largo'

strNombre = 'gabriel' # no colocar el tipo de la variable en el nombre de la misma
intEdad = 22 # no colocar el tipo de la variable en el nombre de la misma
num=12.5 # no colocar palabras incompletas

# usar nombre de variables que se lean naturalmente
# los recomendado es usar sustantivos y si es el caso añadirle un adjetivo
primerNombre='Gabriel'
usuarioLogueado=True
productoComprado=False

'''
para variable booleanas tenemos cierto verbos 
*   es
*   esta       is , has
*   tiene
*   ha (acciones)
'''

haAceptadoLosTerminos = True

'''
como declarar el nombre de una funcion:

    + como las funciones hacen cosas, es mejor empezar con verbos infinitivos el cuales refleje que accion hace la misma.
'''

def crearUsuario(nombre):
    print(nombre)

'''
las funciones las nombramos en 'PascalCase'
'''





