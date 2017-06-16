secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
from string import ascii_lowercase
def getAvailableLetters(lettersGuessed):
    res= ""
    for c in ascii_lowercase:
        if c not in lettersGuessed:
            res += c
            
    return res
print(getAvailableLetters(lettersGuessed))

