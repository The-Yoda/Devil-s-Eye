import json
class GenericModel:

	_aData = {}

	def __init__(self, aData = {}) :
		self._aData = aData;

	def __getattr__(self, method):
		try:
			if method[:3] not in ['get', 'set', 'has', 'add'] :
				raise Exception('No such method Exists')
			else :
				def default(*args, **kwargs):
					return getattr(self, method[:3])(method[3:], *args, **kwargs);
				return default
		except Exception as ex:
			print "Exception : " , ex.args 

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

	def _is_scalar(self, value):
			return isinstance(value,(type(None),str,int,float,bool))

	def getClassFields (self) :
		return self._aData.keys()

	def add(self, attr, *args, **kwargs):
		if attr not in self._aData.keys():
			self._aData[attr] = []
		if self._is_scalar(self._aData[attr]):
			self._aData[attr] = [self._aData[attr]]
		self._aData[attr].append(args[0])
	
	def asJson(self):
		return json.dumps(self._aData)

d = GenericModel()
d.setName("Hell")
print d.getName()
print d.hasValue()
print d.hasName()
d.addValue("AAA")
print d.getValue()
d.addValue(['BBB', 'CCC'])
print d.getValue()
print d.asJson()
print d.getClassFields()
