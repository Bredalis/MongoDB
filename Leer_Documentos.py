
# Libreria

import pymongo

try:

	# Conectarse a la BBDD

	cliente = pymongo.MongoClient("mongodb://localhost:27017")
	db = cliente["Escuela"]
	coleccion = db["Alumnos"]

	# Leer documentos

	for documento in coleccion.find():
		print(documento["Nombre"], documento["Sexo"], documento["Calificacion"])

	cliente.close()

except pymongo.errors.ConnectionFailure as ErrorConexion:
	print("Fallo al conectarse a MongoDB")