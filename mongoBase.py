from pymongo import MongoClient
from bson.objectid import ObjectId
import genmodel

class MongoBase :

	def __init__(self, dbName = None, host = None, port = None) :
		_host = getConf('host') if (host == None) else host
		_port = getConf('port') if (port == None) else port
		_dbName = getConf('db') if (dbName == None) else dbName
		connection = MongoClient(_host, _port)
		self._db = connection[_dbName]

	def insert(self, data, collection) :
		self._db[collection].insert(collection.asDict())
	
	def remove(self, pattern, collection) :
		self._db[collection].remove(pattern)

	def removeById(self, _id, collection) :
		self._db[collection].remove({"_id" :  ObjectId(_id)})
	
	def update(self, pattern, data, collection) :
		self._db[collection].update(pattern, data)
	
	def save(self, pattern, data, collection) :
		self._db[collection].update(pattern, data, upsert=True)
	
	def find(self, pattern, collection) :
		return self._db[collection].find(pattern)
	
	def findById(self, _id, collection) :
		return self._db[collection].findOne({"_id": ObjectId(_id)})

def getConf() :
	return None

#db = MongoBase("pymongo", "localhost", 27017)
#db.insert({"name":"jeeva"}, "user")
#print db.removeById("514dbe2a4443cf2a78438beb", "user")
#print [user for user in db.find({"name":"jeeva"}, "user")]
#db.update({"name":"jeeva"}, {'$set' :{"age": 23} }, "user")
#db.save({"name":"arpit"},{'$set' :{"age":22}}, "user")
#print [user for user in db.find({"name":"jeeva"}, "user")]
