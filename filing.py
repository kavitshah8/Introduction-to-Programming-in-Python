def readfile():
    path = 'C:\\Users\\Kavit\\Google Drive\\Tallac\\Questions.txt'
    file_handler = open(path,'r')

    '''
    First method to read a file from top to bottom
    '''
    #print(file_handler.read())
    
    '''
    Second method to read a file from top to bottom
    '''
    #line = file_handler.readline()
    #while line !='':
    #    print (line,end='')
    #    line = file_handler.readline()

    '''
    Third method to read a file from top to bottom
    '''
    #for line in file_handler:
    #    print (line,end='')

    '''
    Fourth method to read a file from top to bottom
    '''
    #print(file_handler.read())

    '''
    Fifth method to read a file from top to bottom
    '''
    lines = file_handler.readlines()
    for line in lines:
        print(line,end='')
    file_handler.close()    
