import sys
import os
from configmanager import ConfigManager
from main import rootAbsDir
from main import rootDir
class Factory(type) :

	def findModule(self, moduleName, dirName):
		files = os.listdir(dirName)
		for element in files:
			file = os.path.abspath(dirName) + os.sep + element
			if os.path.isdir(file) and os.path.exists(file + os.sep + "__init__.py") :
				modulePath, isFound = self.findModule(moduleName, file)
				if isFound == True :
					return modulePath, True 
			elif element[:-3] == moduleName :
				return file , True
		return None, False

	def loadModule(self, rootAbs, moduleName) :
		path, isFound = self.findModule(moduleName.lower(), rootAbs)
		if isFound == False : 
			raise Exception('No such module exists')
		moduleName = (rootDir + path[len(rootAbsDir):-3]).replace('/','.')
		return __import__(moduleName, fromlist = ["*"])

	def __getattr__(self, method):
		try:
			if method[:3] not in ['get'] :
				raise Exception('No such module Exists')
			else :
				def default(*args, **kwargs):
					conf = getattr(ConfigManager.getMainConfig(), method)()
					moduleName = method[3:] if conf is None else conf  
					module = self.loadModule(rootAbsDir, moduleName)	
					return getattr(module, moduleName)()
				return default
		except ImportError:
			print "unable to locate module"

class ObjectFactory:
    __metaclass__ = Factory 

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
		myclass1 = ObjectFactory.getDb() 
		print myclass1.findById("514ea3664443cf4cd93b2897", 'user')
		myclass2 = ObjectFactory.getMongoDb()
		print myclass2.findById("514ea3664443cf4cd93b2897", 'user').getName()
"""
