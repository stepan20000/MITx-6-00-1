def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    it = 1
    sum = 0
    while sum <= k:
        if sum != k:
            sum = sum + it
            it += 1
        else:
            return True
    return False



def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = ['a', 'e', 'i', 'o', 'u']
    ans = ''
    for letter in s:
        if not (letter.lower() in vowels) and not (letter.upper() in vowels):
            ans += letter
    print(ans)
    
    
def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    l = L.copy()
    l.sort()
    l.reverse()
    for x in l:
        if l.count(x) % 2:
            return x
    return None


def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    
    Write a function called dict_invert that takes in a dictionary with 
    immutable values and returns the inverse of the dictionary. 
    The inverse of a dictionary d is another dictionary whose keys are 
    the unique dictionary values in d. The value for a key in the inverse 
    dictionary is a sorted list (increasing order) of all keys in d that 
    have the same value in d.

Here are two examples:

    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
    If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
    If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
    '''
    valUniqList = [];
    res = {}
    for key, value in d.items():
        if not value in valUniqList:
            valUniqList.append(value)
            res[value] = [key]
        else:
            res[value].append(key)
            res[value].sort()
    return res


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    import math
    
    def fun(x):
        sum = 0
        for i in reversed(range(len(L))):
            sum += L[i] * math.pow(x, len(L) - 1 - i)
        if math.floor(sum) == sum:
            return int(sum)
        else:
            return sum
    return fun 


def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    ''' 
    if len(L1) != len(L2):
        return False
    else:
        if len(L1) == 0 and len(L2) == 0:
            return(None, None, None)
    count = 0
    element = L1[0]
    for el in L1:
        tempCount = L1.count(el)
        if tempCount != L2.count(el):
            return False
        else:
            if tempCount > count:
                element = el
                count = tempCount
    return (element, count, type(element))

