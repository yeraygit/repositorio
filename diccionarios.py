lista = [{'nombre': 'admin', 'password': 'admin'},]
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
        