'''
Concept : Modules & name space
		
			Observations:
			1) While importing a module it executes another module (which we can prevent)
			2) Name space will be different
			
'''

from parent2 import *

print("In useParent2 module name space is ",__name__)
