import random

'''lista = [{'nombre': 'admin', 'password': 'admin'},]
lista_values = []
while True:
    alta_usuario = input('quiere ingresar un nuevo usuario?: s/n')
    if alta_usuario=='s':
        nuevo_usuario= input('introduzca el nombre de usuario: ')  
        for diccionario in lista:     
            lista_values.append(diccionario['nombre'])
        if nuevo_usuario in lista_values:
            print('el nombre ya existe')
        else:
            nueva_contraseña= input('introduzca la contraseña. ')
            lista.append({'nombre': nuevo_usuario, 'password':nueva_contraseña})
    elif alta_usuario=='n':
        break
    else:
        print('ingrese s o n: ')
'''
   #---------------------------------------------------------------------------
'''
numeros = []
menor = 0
mayor = 0
for j in range(10):
    numero_aleatorio = random.randint(1,100)
    numeros.append(numero_aleatorio)     
for i in range(len(numeros)):
    if i==9:
        break
    elif  numeros[i]<numeros[i+1]:
        menor=numeros[i]
    else:
        menor==numeros[i+1]
print (numeros)
print ('----------------')
print (menor)
#-------------------------------------------------------------------------
tabla_diez = []
numero_multiplicacion = int(input('digame que numero quiere multiplicar'))
for i in range(11):
    tabla_diez.append(numero_multiplicacion*i)
print(tabla_diez)
'''
#--------------------------------------------------------------------

'''lista_numeros = []
numeros_para_ingresar = 1
while numeros_para_ingresar!=0:
    numeros_para_ingresar = int(input('ingrese numero para guardar, si quiere salir pulse 0'))
    if numeros_para_ingresar!=0:
        lista_numeros.append(numeros_para_ingresar)
print(lista_numeros)
'''
#----------------------------------------------------------------------


Luisa = {'nombre':'luisa', 'apellido':'sosa', 'sexo':'mujer'}
Juan = {'nombre': 'juan', 'apellido': 'sosa', 'sexo':'varon'}
Gabriel = {'nombre':'Gabriel', 'apellido':'martinez', 'sexo':'varon'}
familia = [Luisa, Juan, Gabriel]
for value in familia:
    print(value)
   

#----------------------------------------------------------------------------------

