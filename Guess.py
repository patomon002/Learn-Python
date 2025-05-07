import random

favorites = ("rice", "beans", "egus")

favorite_food = random.choice(favorites)

food = input("what is your faveorite food: \n")

if food == favorite_food:
    print("You guessed right, " + food + " is one of my favorite foods")
else:
    print("Wrong guess, I dont line " + food)

print("Thank you for trying anyways :) ")