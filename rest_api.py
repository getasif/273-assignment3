import json
import bottle
from bottle import route, run, request, abort
from pymongo import Connection

connection = Connection('localhost',27017)
db = connection.shirts

@route('/')
def hello():
    return "Please specify a specific route!"

@route('/shirt/:shirtId')
def singleShirt(shirtId):
	entity = db['shirts'].find_one({'shirtId':shirtId})
	entity.pop('_id', None)
	if not entity:
		abort(404, 'No shirt with id %s' % shirtId)
	return entity

@route('/shirts', method = 'PUT')
def updateShirt():
	data = request.body.read()
	if not data:
		abort(400, 'No data received')

	entity = json.loads(data)
	if not entity.has_key('shirtId'):
		abort(400, 'No shirtId specified')
		return data
	
	db['shirts'].update({'shirtId':entity.get('shirtId')},{"$set": entity},upsert=False)
	return entity


@route('/shirts', method = 'POST')
def addShirt():
	data = request.body.read()
	if not data:
		abort(400, 'No data received')

	entity = json.loads(data)
	if not entity.has_key('shirtId'):
		abort(400, 'No shirtId specified')

	db['shirts'].save(entity)
	return data


@route('/shirts', method = 'DELETE')
def deleteShirt():
	data = request.body.read()
	if not data:
		abort(400, 'No data received')

	entity = json.loads(data)
	if not entity.has_key('shirtId'):
		abort(400, 'No shirtId specified')

	db['shirts'].remove({'shirtId':entity.get('shirtId')})
	return data


@route('/shoe/:shoeId')
def singleShirt(shoeId):
    return "get single shoe"+shoeId;

@route('/shoes', method = 'PUT')
def updateShirt():
    return "update shoe"

@route('/shoes', method = 'POST')
def addShirt():
    return "add shoe"

@route('/shoes', method = 'DELETE')
def deleteShirt():
    return "delete shoe"


run(host='localhost', port=8080, debug=True)
