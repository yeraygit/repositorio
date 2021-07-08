def obtenerCiudades(ciudades):
    for ciudad in ciudades:
        yield from ciudad

letraDeCadaCiudad= obtenerCiudades(['Madrid','Barcelona','Bilbao','Valencia'])

print(next(letraDeCadaCiudad))
print(next(letraDeCadaCiudad))
print(next(letraDeCadaCiudad))