import utlis
import random

print('Play Rock, Scissors, Paper')
player_name = input('Enter your name：')
print("Choose（0: rock, 1: scissors, 2: paper）")

player_hand = int(input("Enter number："))

if utlis.validate(player_hand):
  computer_hand = random.randint(0,2)

  if player_name == '':
     utlis.print_hand(player_hand)
  else:
     utlis.print_hand(player_hand, player_name)

  utlis.print_hand(computer_hand,"computer")

  result =  utlis.judge(player_hand, computer_hand)
  print(player_name + " " + result )

else: 
  print("Choose from 0 to 2")