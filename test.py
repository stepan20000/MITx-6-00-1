import string

def foo(shift):
    shiftDict = {}
    for l in string.ascii_lowercase:
        shiftDict[l] = chr((ord(l) - 97 + shift)%26 + 97)
    for l in string.ascii_uppercase:
        shiftDict[l] = chr((ord(l) - 65 + shift)%26 + 65)
    return shiftDict
print(foo(1))
