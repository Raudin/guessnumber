# In this case, the random module's function "randint" is needed. The code will be used to generate a random number between 1 and 25.
import random
selectedNumber = random.randint(1,25)
print('Can you guess a number between 1 and 25?')

# Ask player to guess 8 times
for numberSelected in range(1,9):
    print('Please guess a number between 1 and 25')
    guess =int(input())

    if guess < selectedNumber:
        # If the player enters a number lesser than the number the computer chose
        print('Your selected number is smaller than actual number. TRY AGAIN!')
    elif guess > selectedNumber:
        # If the player enters a number greater than the number the computer chose
        print('Your selected number is bigger than actual number. TRY AGAIN')
    else:
        break
    
if guess == selectedNumber:
    #If the player enters the same number the computer chose
    print('CONGRATS!! You have successfully guessed my number in '+ str(numberSelected)  + 'guesses!')
else:
    #If the player doesn't get the number the computer chose after 8 attempts
    print('GAME OVER. The number in mind was '+  str(selectedNumber))
