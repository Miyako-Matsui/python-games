def validate(hand):
  if hand < 0 or hand >2:
    return False
  return True

def print_hand(hand, name='guest'):
    hands = ["rock","scissors","paper"]
    print(name + ' chose' + " "+hands[hand])

def judge(player, computer):
  if player == computer:
    return "draw"

  elif player == 0 and computer ==1:
    return "win"

  elif player == 1 and computer ==2:
    return "win"

  elif player == 2 and computer ==0:
    return "win"

  else:
    return "loose"

print('Play Rock, Scissors, Paper')
player_name = input('Enter your name：')
print("Choose（0: rock, 1: scissors, 2: paper）")

player_hand = int(input("Enter number："))

if validate(player_hand):
  computer_hand = 1

  if player_name == '':
     print_hand(player_hand)
  else:
     print_hand(player_hand, player_name)

  print_hand(computer_hand,"computer")

  result =  judge(player_hand, computer_hand)
  print(player_name + " " + result )

else: 
  print("Choose from 0 to 2")