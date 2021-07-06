'''
def obtenerNumerosPares(limite):
    contador = 0
    numerosPar = 0
    numerosPares = []
    while limite>contador:
        numerosPar += 2
        numerosPares.append(numerosPar)
        contador+=1
    return numerosPares
'''

def obtenerNumerosPares(limite):
    contador = 0
    numerosPar = 0
    
    while limite>contador:
        numerosPar += 2
        yield numerosPar
        contador+=1
    
numerosPares = obtenerNumerosPares(10)

print(next(numerosPares))
