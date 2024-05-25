
# Libreria

import pymongo

# Conectarse a la BBDD

try:
	cliente = pymongo.MongoClient("mongodb://localhost:27017")
	cliente.close()
	print("¡Coneccion a Mongo exitosa!")	

except pymongo.errors.ConnectionFailure as ErrorConexion:
	print("Fallo al conectarse a MongoDB")