import json
class GenericModel:

	_aData = {}

	def __init__(self, aData = {}) :
		self._aData = self.createModel(aData)
	
	def asDict(self) :
		return self.createDict(self._aData)

	def asJson(self):
		return json.dumps(self.asDict())

	def getClassFields (self) :
		return self._aData.keys()

	def set(self, attr, *args, **kwargs):
		if kwargs :
			self._aData[attr] = kwargs;
		elif len(args) == 1 :	
			self._aData[attr] = args[0]

	def get(self, attr, *args, **kwargs):
		return self._aData[attr];

	def has(self, attr, *args, **kwargs):
		if attr in self._aData.keys(): return True
		return False

	def isScalar(self, value):
			return isinstance(value,(type(None),str,int,float,bool))

	def add(self, attr, *args, **kwargs):
		if attr not in self._aData.keys():
			self._aData[attr] = []
		if self.isScalar(self._aData[attr]):
			self._aData[attr] = [self._aData[attr]]
		self._aData[attr].append(args[0])

	def createModel	(self, aData) :
		data = {}
		for key, value in aData.iteritems() :
			data[key.lower()] = value if not isinstance(value, dict) else self.__class__(value)
		return data	

	def __getattr__(self, method):
		try:
			if method[:3] not in ['get', 'set', 'has', 'add'] :
				raise Exception('No such method Exists')
			else :
				def default(*args, **kwargs):
					print method[3:].lower()
					return getattr(self, method[:3])(method[3:].lower(), *args, **kwargs);
				return default
		except Exception as ex:
			print "Exception : " , ex.args 

	def createDict(self, aData) :
		data = {}
		for key, value in aData.iteritems() :
			data[key] = value if not isinstance(value, type(self)) else value.asDict()
		return data	

#d = GenericModel({"name" : "jeeva", "add" : {"Hello":"Hi"}})
#print d.getClassFields()
#print d.getAdd().getHello()
#d.setName("Hell")
#print d.getName()
#print d.hasValue()
#print d.hasName()
#d.addValue("AAA")
#print d.getValue()
#d.addValue(['BBB', 'CCC'])
#print d.getValue()
#print d.asJson()
#print d.getClassFields()
