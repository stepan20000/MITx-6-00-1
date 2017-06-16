high = 100
low = 0
count = 0
print("Please think of a number between 0 and 100!")
while count < 100:
    guess = (high + low) // 2
    print("Is your secret number? " + str(guess))
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if user == "h":
        high = guess
    elif user == "l":
        low = guess
    elif user == "c":
        print("Game over. Your secret number was: " + str(guess))
        break;
    else:
        print("Sorry, I did not understand your input.")
    count+=1
    