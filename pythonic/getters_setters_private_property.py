'''
Concepts: Access Methods, Data hiding, Data Protection

          getters_setters_private_property

'''
class Contact(object):

    def __init__(self,name='Anonymouse',age='0',email='x@x.com'):
        object.__init__(self)
        self.name = name
        self.age = age
        self.email = email

    def setName(self,name):
        if name is not '':
            self.__name = name
        else:
            print('Enter a valid name.Setting a name to Anonymous.')
            self.__name = 'Anonymous'
            
    def getName(self):
        return self.__name

    name = property(fget = getName,fset = setName)

    def setAge(self,age):
        if age > 0:
            self.__age = age           
        else:
            print ("Enter a valid age. Age can not be negative. Setting age to 0.")
            self.__age = 0
            
    def getAge(self):
        return self.__age

    age = property(fset = setAge,fget = getAge)

    def setEmail(self,email):
        if '@' in email:
            self.__email = email
        else:
            print('Invalid email address.Setting an email to x@x.com')
            self.__email = 'x@x.com'
            
    def getEmail(self):
        return self.__email

    email = property(fget = getEmail,fset = setEmail)

def main():
    c = Contact('',0,'kavit.shah8@gmail.com')
    print (c.name,c.email,c.age)

if __name__ == "__main__":
    main()

