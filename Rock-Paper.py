
import random

computer = random.choices('Rock')

me = input('Enter either Rock, Paper or Scissors: \n')
if computer == me:
    print('It is a tie')


