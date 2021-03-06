import bottle
import pymongo

# handler para ruta por defecto
#@bottle.route('/')
@bottle.route('/cuentas/<name>')
def raiz(name):
    con = pymongo.MongoClient('localhost',27017)
    db = con.banco
    item = db.cuentas.find_one({"nombre":name})
    return bottle.template("datoscuenta_template", datos = item)

bottle.debug(True)
bottle.run(host='localhost', port=8082)
