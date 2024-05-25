
# Librerias

import pymongo

try:

	# Conectarse a la BBDD

	cliente = pymongo.MongoClient("mongodb://localhost:27017")
	db = cliente["Escuela"]
	coleccion = db["Alumnos"]

	# Crear e insertar documento

	documento = {"Nombre": "Lisa", "Sexo": "Femenina", "Calificacion": 10}
	coleccion.insert_one(documento)

	cliente.close()
	print("¡La coneccion fue un exito!")

except pymongo.errors.ConnectionFailure as ErrorConexion:
	print("Fallo al conectarse a MongoDB")