def gcd():
    '''(input_num1,input_num2) -> int

    Returns the GCD of two numbers input_number1 & input_number2 entered by a user
    '''
    x = int(input('Enter first number: '))
    y = int(input('Enter second number: '))

    while x != y:
        if x > y :
            x = x-y
        else:
            y = y-x
    return x 
