
# Libreria

import pymongo
from bson import ObjectId

# Conectarse a la BBDD

cliente = pymongo.MongoClient("mongodb://localhost:27017")
db = cliente["Escuela"]
coleccion = db["Alumnos"]

# Datos a actualizar

datos = {"_id": ObjectId("6532537798c4f4853acfafe2")}
nuevos_datos = {"$set": {"Nombre": "Juan", "Sexo": "Femenino", "Calificacion": 7}}

# Actualizar

coleccion.update_one(datos, nuevos_datos)
cliente.close()