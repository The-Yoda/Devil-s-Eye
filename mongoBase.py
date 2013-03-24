from pymongo import MongoClient
from bson.objectid import ObjectId
from genmodel import GenericModel

class MongoBase :

	def __init__(self, dbName = None, host = None, port = None) :
		_host = getConf('host') if (host == None) else host
		_port = getConf('port') if (port == None) else port
		_dbName = getConf('db') if (dbName == None) else dbName
		connection = MongoClient(_host, _port)
		self._db = connection[_dbName]

	def insert(self, data, collection) :
		self._db[collection].insert(data.asDict())
	
	def remove(self, pattern, collection) :
		self._db[collection].remove(pattern)

	def removeById(self, _id, collection) :
		self._db[collection].remove({"_id" :  ObjectId(_id)})
	
	def update(self, pattern, data, collection, option = 'set', _upsertStatus = False) :
		_data = data.asDict()
		self._db[collection].update(pattern, { '$' + option : _data}, upsert = _upsertStatus)
	
	def save(self, pattern, data, collection, option = 'set') :
		self.update(pattern, data, collection, option, True)
	
	def find(self, pattern, collection) :
		resultSet = self._db[collection].find(pattern)
		return [self._processResult(document) for document in resultSet]
	
	def _processResult(self, result) :
		result['id'] = str(result['_id'])
		del result['_id']
		print type(result)
		return GenericModel(result)
	
	def findById(self, _id, collection) :
		result = self._db[collection].find_one({"_id": ObjectId(_id)})
		return self._processResult(result)

def getConf() :
	# mocking getconfig 
	return None

#db = MongoBase("pymongo", "localhost", 27017)
#db.insert(GenericModel({"name":"jeeva"}), "user")
#print db.removeById("514dbe2a4443cf2a78438beb", "user")
#print [user for user in db.find({"name":"jeeva"}, "user")]
#db.update({"name":"jeeva"}, GenericModel({"age": 23}), "user")
#db.save({"name":"arpit"},GenericModel({"age":23}), "user")
#print [user for user in db.find({"name":"jeeva"}, "user")]
#print 'Hello' == u'Hello'
#x = db.findById("514ea3664443cf4cd93b2897","user")
#print x.getName()
#y = db.find({"name":"arpit"}, 'user')
#print y[0].getName()
