import bottle
import pymongo

#handler para ruta por defecto
@bottle.route('/')
def raiz():
    con = pymongo.MongoClient('localhost',27017)
    db = con.banco
    item = db.cuentas.find_one()
    return '<b>Hombre, %s!</b>' % (item ['nombre'],)
bottle.run(host='localhost',port =8082)
