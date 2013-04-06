"""
	Helper module that retrieves configurations from the file
"""

from ConfigParser import SafeConfigParser
from genericmodel import GenericModel

def GetConfigurations(CfgFileName):
	"""
	Returns a GenericModel filled with the configuration settings, read from the file `CfgFileName`.
	If there is a problem, this would return an empty GenericModel object. An example for the configuration 
	settings is as follows

		[DB]
		host = localhost
		port = 12345 ;Be sure to convert to an int
		db   = test

	Here, DB is the section name and the configuration names are host, port and db where as the
	configuration values are localhost, 12345, test respectively. The text that follows semi-colon (;)
	will be ignored. So to get the host value,

		config = GetConfigurations ('/var/lib/MyCfg.cfg')
		print config.getDB().getHost()

	"""
	Configurations = GenericModel()
	try:
		parser = SafeConfigParser()
		parser.read (CfgFileName)
		for Section in parser.sections():
			getattr (Configurations, 'set' + Section)(GenericModel())
			CurrentSection = getattr (Configurations, 'get' + Section)()
			for ConfigName, ConfigValue in parser.items (Section):
				getattr (CurrentSection, 'set' + ConfigName) (ConfigValue)
	except:
		print sys.exec_info[0]
	return Configurations
