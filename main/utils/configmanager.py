"""
	Helper module that retrieves configurations from the file
"""

from ConfigParser import SafeConfigParser
from genericmodel import GenericModel
from main import configPath

class Manager(type) :
	_configurations = None
	def __getattr__(self, method):
		try :
			if method[:3] not in ['get', 'set'] :
				def default(*args, **kwargs):
					raise Exception('No such method Exists')
			else :
				def default(*args, **kwargs) :
					if self._configurations is None :
						self.loadConfig()
					return getattr(self, method[:3] + 'Config')(method[3:-6].lower(), *args)
			return default
		except Exception as ex:
			print "Exception : " , ex.args 

	def loadConfig(self) :
		"""
		Sets the _configuration variable with whole configuration of project. It'd be loaded once (Behaves like singleton)
		If there is a problem, this would return an empty GenericModel object. An example for the configuration 
		settings is as follows

			[DB]
			host = localhost
			port = 12345 ;Be sure to convert to an int
			db   = test

		Here, DB is the section name and the configuration names are host, port and db where as the
		configuration values are localhost, 12345, test respectively. The text that follows semi-colon (;)
		will be ignored. So to get the host value,

			print ConfigManager.getDbConfig().getHost()

		"""
		cfgFileName = configPath + 'project.cfg'
		self._configurations = GenericModel()
		try:
			parser = SafeConfigParser()
			parser.read (cfgFileName)
			for section in parser.sections():
				getattr (self._configurations, 'set' + section)(GenericModel())
				currentSection = getattr (self._configurations, 'get' + section)()
				for configName, configValue in parser.items (section):
					getattr (currentSection, 'set' + configName) (configValue)
		except:
			print sys.exec_info[0]
	
	def getConfig(self, configName, *args) :
		try :
			return getattr (self._configurations, 'get' + configName)()
		except Exception as e :
			print "Error in getting Configuration"
		
	def setConfig(self, configName, *args) :
		if len(args) == 1 :
			getattr (currentSection, 'set' + configName) (args[0])
		else :
			raise Exception('Given more parameters for setconfig')	
			
	def saveConfig() :
	    pass            #To be implemented		


class ConfigManager:
    __metaclass__ = Manager 
