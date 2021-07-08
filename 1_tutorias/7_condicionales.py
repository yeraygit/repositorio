def tienePasaporte(pasaporte=True):
    if pasaporte :
        print("Puede viajar")
    else:
        print("No puede viajar")    

def esPar(numero):
    if numero%2 == 0:
        print('El numero {} es par {}.'.format(numero,'prueba'))
    else:
        print('El numero {} no es par {}.'.format(numero,'prueba'))


tienePasaporte(False)

esPar(30)