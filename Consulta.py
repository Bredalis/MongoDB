
# Libreria

import pymongo

# Conectarse a la BBDD

cliente = pymongo.MongoClient("mongodb://localhost:27017")
db = cliente["Escuela"]
coleccion = db["Alumnos"]

# Consultas

for documento in coleccion.find({"Nombre": "Juan"})
	print(documento)
 
cliente.close()