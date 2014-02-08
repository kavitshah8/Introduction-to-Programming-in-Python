'''
Concepts: Name space, Modules
			http://docs.python.org/2/tutorial/modules.html
'''

class Parent(object):
        
	def __init__(self,name='Anonymous'):
		object.__init__(self)
		self.name = name
	
	def setName(self,name):
		self.__name = name
		
	def getName(self):
		return self.__name

	name = property (fset = setName,fget = getName)
	
def main():
	a = Parent('kavit')
	print(a.getName())

if __name__=='__main__':
	main()

        
