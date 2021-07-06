# sirven para no repetir codigo

def sumar(primer_numero,sugundo_numero):
    resultado = primer_numero + sugundo_numero
    return resultado

def restar(primer_numero,sugundo_numero):
    resultado = primer_numero - sugundo_numero
    return resultado

def imprimir():
    print('Hola mundo')    


resultado = sumar(15,15)
print(resultado)

resultado = restar(sumar(15,15),30)
print(resultado)

imprimir()
