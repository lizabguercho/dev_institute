import random
num = random.randint (1,100)
win = False

# for each attempt
for attempt in range (1,8):
    # catch the user's answer to the question
    guess_str = input(f'Guess the number (attempt {attempt}/7): ')
    # cast the guess into an int type
    guess = int(guess_str)
    if guess > num:
        print("You are too high")
    elif guess < num:
        print("You are too low.")
    else:
        # if we enter here, the user won, let's finish the game
        win = True
        break
# check if the user has won before the game is finished
if win:
    print("You won!")
else:
    print("You lost!")