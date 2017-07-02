def is_list_permutation(L1, L2):
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
    
        
    
    
    

L1 = [] 
L2 = []
print(is_list_permutation(L1, L2))
        

