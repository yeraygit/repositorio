'''
    * palabra clave raise
    * Creaccion de exepciones propias
'''

'''
def comprobar_edad(edad):

    #if edad < 0:
        raise TypeError("No puedes tener un edad negativa")
    
    if edad >= 0 and edad < 18:
        print('Eres muy joven para acceder.')
    elif edad >= 18:
        print('Tienes la edad para poder acceder.')

comprobar_edad()
'''

import math

def calular_raiz(numero):
    
    if numero < 0:
        raise ValueError('Numero no puede ser negativo.')
    else:
        return math.sqrt(numero)    

numero = int(input('Tipea un numero:'))  

print(calular_raiz(numero))