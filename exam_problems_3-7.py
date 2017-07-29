# ---------------------- Problem - 3 ---------------------------

def sum_digits(s):
    """ assumes s a string
    Returns an int that is the sum of all of the digits in s.
    If there are no digits in s it raises a ValueError exception. """
    sum = 0
    haveDigits = False
    for letter in s:
        if letter.isdigit():
            haveDigits = True
            sum += int(letter)
    if haveDigits:
        return sum
    else:
        raise ValueError("String doesn't contain digits")
        
# ----------------------- Problem - 4 ------------------------------

def max_val(t): 
    """ t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t """ 
    maxVal = False
    
    def helper(obj):
        nonlocal maxVal
        for el in obj:
            if isinstance(el, int):
                if maxVal == False or maxVal < el:
                    maxVal = el
            else:
                helper(el)
                
    helper(t)
    return maxVal 

# ---------------------- Problem - 5 -------------------------------

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                      N unique lowercase letters. 
    code: string (assume it only contains letters also in map_from)
    Returns a tuple of (key_code, decoded).
    key_code is a dictionary with N keys mapping str to str where 
    each key is a letter in map_from at index i and the corresponding 
    value is the letter in map_to at index i. 
    decoded is a string that contains the decoded version 
    of code using the key_code mapping. """
    key_code = {}
    decoded = ''
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    for letter in code:
        decoded += key_code[letter]
    return (key_code, decoded)
        
# ----------------   Problem - 6 ----------------------------

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
        
# 6-1 and 6-2

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs one or more times in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        try:
            self.vals[e] -= 1
        except:
            return

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        try:
            return self.vals[e]
        except:
            return 0
    
    def __add__(self, other):
        sumBag = Bag()
        for key in self.vals.keys():
            sumBag.vals[key] = self.vals[key]
        for key in other.vals.keys():
            if key in sumBag.vals:
                sumBag.vals[key] += other.vals[key]
            else:
                sumBag.vals[key] = other.vals[key]
        return sumBag
    
# 6-3

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        try:
            del self.vals[e]
        except:
            return
        
    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return e in self.vals
    
# ---------------------- Problem 7 -----------------------

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist**2 + yDist**2)**0.5
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'
        
class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc
    def __str__(self):
        return str(self.center_loc)
    
# Ny class for problem 7 here:
    
class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """
    def __init__(self, center_loc, tent_loc = Location(0,0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        self.center_loc = center_loc
        self.tents = []
        self.tents.append(tent_loc)
      
    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        dist = 0.5
        for tent in self.tents:
            if tent.dist_from(new_tent_loc) < dist:
                return False
        self.tents.append(new_tent_loc)
        return True
            
      
    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        try:
            self.tents.remove(tent_loc)
        except:
            raise ValueError("There is no tent in this location")
                
      
    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        answ = []
        for tent in self.sort_tents(self.tents.copy()):
            answ.append(str(tent))
        return answ
        
        
#    Helper method for sorting a list with Location instances accoording to 
# the get_tents requirements: "The list should be sorted by the x coordinate 
# of the location."
    def sort_tents(self, L):
# Compare two Location instances with the x coordinate
        def compare(x, y):
            return x.getX() < y.getX()
# Use a Merge sort algorithm
        def mergeSort(L):
            if len(L) < 2:
                return L[:]
            else:
                middle = int(len(L)/2)
                left = mergeSort(L[:middle])
                right = mergeSort(L[middle:])
                return merge(left, right)
            
        def merge(left, right):
            result = []
            i,j = 0, 0
            while i < len(left) and j < len(right):
                if compare(left[i], right[j]):
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            while (i < len(left)):
                result.append(left[i])
                i += 1
            while (j < len(right)):
                result.append(right[j])
                j += 1
            return result
        
        return mergeSort(L)

