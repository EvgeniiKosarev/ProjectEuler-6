import numpy


def diff(n):

    '''
    (int) -> int

    Function returns the difference between the square of the sum and
    the sum of squares of the first n natural numbers

    >>> diff(10):
    2640


    '''

    
    sq_sm = 0
    sm_sq = 0
    for i in range(n+1):
        sq_sm+=i
        sm_sq += i**2

    return sq_sm**2 - sm_sq

    
    


