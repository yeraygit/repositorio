'''
    -------------------Exepciones------------------
    * errores que ocurren en tiempo de ejecucion.
    * errores que la computadora no puede controlar.

	estructura:

	try:
		lo que causa la exepcion
	except nombre_de_la_exepcion:
		lo que queramos indicar cuando la exepcion sucede	
'''


'''
def sumar(primer_numero, segundo_numero):
	return primer_numero+segundo_numero

def restar(primer_numero, segundo_numero):
	return primer_numero-segundo_numero

def multiplicar(primer_numero, segundo_numero):
	return primer_numero*segundo_numero

def dividir(primer_numero, segundo_numero):		
	return primer_numero/segundo_numero
	

primer_numero=(int(input("Introduce el primer numero: ")))

segundo_numero=(int(input("Introduce el segundo numero: ")))		
	
operacion=input("Introduce una operacion (suma,resta,multiplica,divide): ")

if operacion=="sumar":
	print(sumar(primer_numero,segundo_numero))

elif operacion=="restar":
	print(restar(primer_numero,segundo_numero))

elif operacion=="multiplicar":
	print(multiplicar(primer_numero,segundo_numero))

elif operacion=="dividir":
	print(dividir(primer_numero,segundo_numero))

else:
	print ("Operacion no coincide con las mostradas.")

print("El programa pudo continuar.")
'''

def dividir():
	try:
		primer_numero=(int(input("Introduce el primer numero: ")))

		segundo_numero=(int(input("Introduce el segundo numero: ")))

		print(primer_numero/segundo_numero)
	except ValueError:
		print('El valor tipeado por teclado tiene que ser un numero')
	except ZeroDivisionError:
		print('No se puede dividir por cero')
	except TypeError:
		print('error general')				
	finally:
		print('proceso finalizado')

dividir()		