
# Libreria

import pymongo

# Conectarse a la BBDD

cliente = pymongo.MongoClient("mongodb://localhost:27017")
db = cliente["Escuela"]
coleccion = db["Alumnos"]

# Datos a borrar

datos = {"Nombre": "Juan"}

# Borrar

coleccion.delete_one(datos)
cliente.close()