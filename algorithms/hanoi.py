"""
Concept: Recursion
"""
def hanoi(n,A,B,C):
    ''' (int,str,str,str) -> messsage

    Gives the procedure to transfer n disks from peg A to peg B with the help of peg C
    '''
    if n==1:
        print('move from '+ A +' to '+B)
    else:
        hanoi(n-1,A,C,B)
        hanoi(1,A,B,C)
        hanoi(n-1,C,B,A)
