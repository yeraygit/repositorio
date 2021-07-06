# -*- coding: utf-8 -*-
import pymysql as mysql

def print_menu():
    print("1. Ingresar")
    print("2. Registrar")
    print("3. Salir")
    print("Ingrese un numero del 1 al 3: ")
    print(" ")

host = "localhost"
userx = "root"
passwordx = ""
db = "ldap"

def run_query(query=""):
 
    conect = mysql.connect(
        host= host,
        user= userx,
        password= passwordx,
        db= db
    )
    
    cursor = conect.cursor()
    cursor.execute(query)

    if query.upper().startswith('SELECT'):
        data = cursor.fetchall()
    else:
        conect.commit()
        data = None

    cursor.close()
    conect.close()

    return data

def consultar_datos(usuario):
    query = "SELECT * FROM datos WHERE Usuario=('%s')" % usuario
    data=run_query(query)
    return data
    
def insertar(usuario,password):
    query = "INSERT INTO datos (Usuario, Password) VALUES ('%s','%s')" %(usuario, password)
    run_query(query)


print_menu()
op=int(input())

while not op==3:
    if op==1:
        user= input("Ingrese su Nombre de Usuario: ")
        password= input ("Ingrese su Contraseña: ")
        resultado=consultar_datos(user)
        if resultado:
            for datos_usuario in resultado:
                if datos_usuario[0]==user:
                    if datos_usuario[1]==password:
                        print("Bienvenido!! Haz ingresado a nuestro sistema.")
                    else:
                        print("No ha podido ingresar.")
                        print("Sus datos son erroneos o no esta registrado en nuestro sistema.")
                        print("Por favor intente de nuevo.")
        else:
            print("Sus datos son erroneos o no esta registrado en nuestro sistema.")  

    elif op==2:
        user= input("Ingrese su Nombre de Usuario: ")
        password= input("Ingrese una contraseña (tiene que tener mas de 8 caracteres): ")
        password2= input("Repita su contraseña ingresada anteriormente: ")
        resultado=consultar_datos(user)
        if resultado:
            print("¡Usuario ya existente!")
        elif password==password2 and len(password)>=8:
            insertar(user,password)
            print("¡Su Usuario se ha registrado con exito!")
        else:
            print("Su contraseña no cumple con los estandares.")
            print("la contraseña debe tener mas de 8 caracteres.")
            
    print(" ")
    print_menu()
    op=int(input())
print("¡Haz salido del sistema con exito!")

