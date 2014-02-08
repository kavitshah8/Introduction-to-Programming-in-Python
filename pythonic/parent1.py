'''
Concepts: Name space, Modules

	1. Every module has its name space stored in __name__ variable which is by default __main__
	2. When you import one module into another module we have two name spaces. 
		Name space of imported module is the name of the module i.e. <module_name.py>
		Name space of the calling module is __main__
	3. When you import one module into another module first it runs the imported module.
		To avoid that every module has following condition:
			if __main__ == '__main__':
				main()
		Because of that it will not run the module when we import the module.

'''
print ("In parent module name space is:", __name__)

class Parent(object):
        
	def __init__(self,name='Anonymous'):
		object.__init__(self)
		self.name = name
	
	def setName(self,name):
		self.__name = name
		
	def getName(self):
		return self.__name
	
        # careful with the arguments of property
	name = property (fget = getName,fset = setName)
	
def main():
	a = Parent('kavit')
	print(a.getName())
	
main()

        
