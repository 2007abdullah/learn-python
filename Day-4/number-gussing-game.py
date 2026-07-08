secret = 7

while True:
    guess = int(input("Guess number: "))

    if guess == secret:
        print("You win!")
        break
    else:
        print("Try again")