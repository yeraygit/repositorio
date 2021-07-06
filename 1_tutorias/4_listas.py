'''
* Es una estructura de datos que nos permite almacenar gran catidad de valores.
* Es Equivalente a los arrays en otros lenguajes.
* Se pueden expandir dinamicamente añadiendo nuevos elementos (poderoso)
'''
# indices    0   1           2               3      4
elementos = [1, 2.5, 'Aprendiendo python', [5,6] ,True]

'''
print(elementos[:])
print(elementos[-2])
print(elementos[0:3]) # print(elementos[:3]) es lo mismo
print(elementos[2:4])
print(elementos[2:])
elementos2 = [1,True]
elementos3 = elementos + elementos2
print(elementos3[:])
print(elementos2*2)
print(len(elementos))
'''

for elemento in elementos:
    print(elemento)
dic = {'key':'elemento'}
elementos.append(dic)  
print("__________-------------------___________")
for elemento in elementos:
    print(elemento)

print("___________-------------------___________")
elementos.extend([False,10.5])    
for elemento in elementos:
    print(elemento)

print("___________-------------------___________")
elementos.remove(1)    
for elemento in elementos:
    print(elemento)

print("___________-------------------___________")
elementos.insert(2,4)    
for elemento in elementos:
    print(elemento)    

print("___________-------------------___________")
indice = elementos.index("Aprendiendo python")    
print(indice)

print("___________-------------------___________")
count_elements = elementos.count("otro elemento")    
print(count_elements)
