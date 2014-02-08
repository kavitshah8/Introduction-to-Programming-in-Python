"""
Concept : Recursion

Raising a number to a positive integer power 
"""
def exponent(x,n):
    '''(number,int) -> number

    Returns exponent of two numbers entered by user
    '''
    if(n==1):
        return x
    else:
        return x* exponent(x,n-1)

def fastExponent(x,n):
    '''(number,int) -> int

    Returns exponent of two numbers entered by user with less computation
    '''
    if(n==1):
        return x
    elif(n%2==0):
        return pow(fastExponent(x,n/2),2)
    else:
        return x*fastExponent(x,n-1)

def superFastExponent(x,n):
    '''(number,int) -> int

    Returns exponent of two numbers entered by user with efficient calcuations
    '''
    if(n==1):
        return x
    elif(n%2==0):
        return pow(superFastExponent(x,n/2),2)
    else:
        return x*pow(superFastExponent(x,(n-1)/2),2)
    
