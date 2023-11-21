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