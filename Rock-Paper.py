
import random

computer = ('Rock', 'Paper', 'Scissors')

computer_choice = random.choice(computer)

me = input('Enter either Rock, Paper or Scissors: \n')
if computer_choice == me:
    print('It is a tie')
elif computer_choice == 'Rock' and me == 'Scissors':
    print('Computer Wins')
elif computer_choice == 'Rock' and me == 'Paper':
    print('Computer Wins')
elif computer_choice == 'Paper' and me == 'Rock':
    print('You win')
elif computer_choice == 'Scissors' and me == 'Rock':
    print('You win')
else:
    print("Computer choice was " + computer_choice + " and this condition was not defined")



