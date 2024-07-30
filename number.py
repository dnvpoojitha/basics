print("Welcome to the Number Guessing Game!")
import random

i = random.randint(1, 100)


while True:
    user_input = int(input("enter the value b/w 1 to 100:"))
    if user_input < i:
        print("its too low! try again")
    elif user_input > i:
        print("its too high ! try again")
    else:
        print("you won")
