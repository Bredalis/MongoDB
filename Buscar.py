
# Libreria

import pymongo

# Conectarse a la BBDD

cliente =  pymongo.MongoClient("mongodb://localhost:27017")
db = cliente["Escuela"]
coleccion = db["Alumnos"]

# Datos a buscar

datos_1 = {"Nombre": "Lisa"}
datos_2 = {"Sexo": "Femenino"}

# Buscar

for documento in coleccion.find(datos_1, datos_2):
	print(documento)

cliente.close()