import pymongo
from pymongo import MongoClient

# conexión
con = MongoClient ('localhost', 27017)
db = con.banco

# colección
cuentas = db.cuentas
resultado = cuentas.find_one()

print (resultado['nombre'], resultado['cuentas']) 
#print resultado [ 'cuentas' ]
