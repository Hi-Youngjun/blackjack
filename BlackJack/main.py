from art import logo
import random


def pick_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def score_calculation(cards):
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return int(sum(cards))

def compare(player_score, dealer_score):
  if player_score > 21:
    return "You lose"
  elif dealer_score > 21:
    return "You Win"
  elif player_score == dealer_score:
    return "Draw"
  elif player_score > dealer_score:
    return "You win!"
  elif player_score == 21:
    return "You win! Black jack!"
  elif dealer_cards ==21:
    return "You lose. Dealer has black jack"
  else:
    return "You lose"
  
play = input(print("Do you want to play a game of Blackjack? Type 'y' or 'n': ")).lower()
continue_game = True
keeping_game = True
print(logo)
player_cards = []
dealer_cards = []
while continue_game: 
  if play =='y':
    for i in range(2):
      player_cards.append(pick_cards())
      dealer_cards.append(pick_cards())
    player_score = score_calculation(player_cards)
    dealer_score = score_calculation(dealer_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {dealer_cards[0]}")     
    
    while keeping_game:
      keep_card_pick = input(print("Type 'y' to get another card, type 'n' to pass: ")).lower()
      if keep_card_pick =='y':
        player_cards.append(pick_cards())
        dealer_cards.append(pick_cards())
        player_score = score_calculation(player_cards)
        dealer_score = score_calculation(dealer_cards)
        if player_score > 21 or dealer_score >21:
          continue_game = False
          keeping_game = False
        else:
          print(f"Your cards: {player_cards}, current score: {player_score}")
          compare(player_score, dealer_score)
      else:
        keeping_game = False
        continue_game = False

  
  else:
    continue_game = False

print(f"   Your final hand: {player_cards}, final score: {player_score}")
print(f"   Computer's final hand: {dealer_cards}, final score: {dealer_score}")
print(compare(player_score, dealer_score))  
