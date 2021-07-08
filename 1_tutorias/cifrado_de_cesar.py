
fraseEncriptada = 'ñdylgdhvehññd'
fraseDesencriptada = ""
desplazamiento = 3
alfabeto = 'zyxwvutsrqpoñnmlkjihgfedcba'  #abcdefghijklmnñopqrstuvwxyz  zyxwvutsrqpoñnmlkjihgfedcba

for x in range(20):             
    for letra in fraseEncriptada:
        
        if letra in alfabeto:
            indice = alfabeto.index(letra)
            aux = indice + x
            if aux >= len(alfabeto):
                fraseDesencriptada += alfabeto[indice % len(alfabeto)]
            else:
                fraseDesencriptada += alfabeto[aux]
    print(fraseDesencriptada)
    fraseDesencriptada=''