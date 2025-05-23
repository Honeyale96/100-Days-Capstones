# Imports
import random


# Function - Deal Cards
def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Function - Calculate
def calculate(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Function - Declarations
def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "It's a draw"
    elif dealer_score == 0:
        return "Dealer Blackjack, You Lose."
    elif player_score == 0:
        return "Blackjack, You Win!"
    elif player_score > 21:
        return "Bust, You lose."
    elif dealer_score > 21:
        return "Dealer Bust, You Win!"
    elif player_score > dealer_score:
        return " You Win!"
    else:
        return "You Lose"


# Function - Game Start
def play_game():
    player_cards = []
    dealer_cards = []
    game_over = False

    for _ in range(2):
        player_cards.append(deal())
        dealer_cards.append(deal())

    # Calculate dealt Cards
    while not game_over:
        player_score = calculate(player_cards)
        dealer_score = calculate(dealer_cards)
        print(" \n")
        print(f"  Your cards: {player_cards}, current score: {player_score}")
        print(f"  Dealer's first card: {dealer_cards[0]}\n")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            # Player's Turn
            player_hits = input("type 'y' to hit, type 'n' to stand: ")
            if player_hits == 'y':
                player_cards.append(deal())
            else:
                game_over = True

    # Dealer's Turn
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal())
        dealer_score = calculate(dealer_cards)
    print(" \n")
    print(f"  Player's hand: {player_cards}, total: {player_score}")
    print(f"  Dealer's hand: {dealer_cards}, total: {dealer_score}")
    print(compare(player_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    play_game()
