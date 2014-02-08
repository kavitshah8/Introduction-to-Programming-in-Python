'''
Concept : Modules & name space
		
			Observations:
			1) While importing a module it executes another module (which we can prevent)
			2) Name space will be different
			
'''
from parent1 import *

print("In useParent module name space is ",__name__)
