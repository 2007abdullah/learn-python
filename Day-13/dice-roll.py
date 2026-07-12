import random

while True:
    input("Press Enter to roll dice...")
    print("You got:", random.randint(1, 6))

    break_choice = input("Roll again? (y/n): ")
    if break_choice.lower() != 'y':
        break
     
     