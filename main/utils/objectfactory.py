import imp
import sys
from configmanager import ConfigManager

class Factory(type) :

	def __getattr__(self, method):
		try:
			if method[:3] not in ['get'] :
				raise Exception('No such module Exists')
			else :
				def default(*args, **kwargs):
					conf = getattr(ConfigManager.getMainConfig(), method)()
					moduleName = method[3:] if conf is None else conf  
					fp, pathName, description = imp.find_module('main.lib.db.' + moduleName.lower())
					print ConfigManager.getMainConfig()
					module = imp.load_module(moduleName, fp, pathName, description)
					return getattr(module, moduleName)()
				return default
		except ImportError:
			print "unable to locate module"

class ObjectFactory:
    __metaclass__ = Factory 

def getConf(module, confName):
	if confName == 'Db' :
		return "MongoDb"
	"""
	Mocking configmanager which will be implemented later
	"""
	return None
"""
This class ObjectFactory can be used to improve dynamicity of modules.
Ex :  If a user needs an instance of a class (whose name is specified in config), 
			lets say the Db is mysql as per the conf, then call
				ObjectFactory.getDb()
			It'll give you mysql object
			If it is not present in configuration, it'll try to load the Db class if exists, else throw an error.
	  If the user want to get an instance of a class which is not present in config, call using 'get' + classname + ()
			 ObjectFactory.getMongoDb()
			 It'll return you mongodb class instance.
	Usage :
	"""
myclass1 = ObjectFactory.getDb() 
print myclass1.findById("514ea3664443cf4cd93b2897", 'user').getName()
myclass2 = ObjectFactory.getMongoDb()
print myclass2.findById("514ea3664443cf4cd93b2897", 'user').getName()

