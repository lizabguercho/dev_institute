import random
def number_guessing_game():
    random_number = random.randint(1,100)
    max_attempts = 7
    win = False
    for attempt in range(1, max_attempts+1):
        guess = int(input(f"Guess the number? (attempt {attempt}/7) :"))
        if guess > random_number:
            print("You are too high.")
        elif guess < random_number:
            print("You are too low")
        else:
            win = True
            print("You won!")
            break

    if not win:
        print("You lost!")
        print(f"The correct number was : {random_number}")
    return win
result = number_guessing_game()
