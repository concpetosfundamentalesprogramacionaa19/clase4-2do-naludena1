"""
    @naludena1
    Manejo de estructuras
"""

diccionario = {"nombre": "René", "apellidos": "Elizalde"}
diccionario2 = {"nombre": "Luis", "apellidos": "Alvarez"}

lista = [diccionario, diccionario2]

print("Imprimir diccionario")
for l in diccionario.keys():
	midiccionario = l
	print ("Mi nombre es: %s y mi apellido es: %s" % (midiccionario["nombre"], midiccionario["apellidos"]))