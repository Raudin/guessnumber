# In this case, the random module's function "randint" is needed. The code will be used to generate a random number between 1 and 25.
import random
selectedNumber = random.randint(1,25)
print('Can you guess a number between 1 and 25?')

# Ask player to guess 8 times
for numberSelected in range(1,9):
    print('Please guess a number between 1 and 25')
    guess =int(input())

    if guess < selectedNumber:
        # If the player enters a number lesser than the computer chosed number
        print('Your selected number is smaller than actual number. TRY AGAIN!')
    elif guess > selectedNumber:
        # If the player enters a number greater than the computer chosed number
        print('Your selected number is bigger than actual number. TRY AGAIN')
    else:
        break
    
if guess == selectedNumber:
    print('CONGRATS!! You have successfully guessed my number in '+ str(numberSelected)  + 'guesses!')
else:
    print('GAME OVER. The number in mind was '+  str(selectedNumber))
