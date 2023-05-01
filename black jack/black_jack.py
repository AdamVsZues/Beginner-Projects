"""
This is v1 of blackjack. It is currently missing the following:
1. spliting: having two same value cards in your first dealt cards that you may split in two hands
2. betting: money
3. doubling: double your preset bet 
4. surrendering: bailing out after seeing the dealers cards
5. Bot players
"""

'''The idea is to make a deck of cards and generate values based off of what card drawn. The dealer and one other will also have cards and I will try to make cards not repeat so card counting is avalible. if over 21 total value you bust/loose and if under either the bot or dealer you also loose. Also if 21 is drawn turn one you get a black jack and win imediatly. Use random and if statements.'''
import random
import re


global rounds
rounds = 1


global wins
wins = 0


# generates new random card
def new_card():
    deck_of_cards = [
        'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades',
        'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',
        'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
        'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']
    if len(deck_of_cards) > 0:
        card = random.choice(deck_of_cards)
        deck_of_cards.remove(card)
        return (card)
    elif len(deck_of_cards) == 0:
        deck_of_cards = [
            'Ace of Spades', '2 of Spades', '3 of Spades', '4 of Spades', '5 of Spades', '6 of Spades', '7 of Spades', '8 of Spades', '9 of Spades', '10 of Spades', 'Jack of Spades', 'Queen of Spades', 'King of Spades',
            'Ace of Clubs', '2 of Clubs', '3 of Clubs', '4 of Clubs', '5 of Clubs', '6 of Clubs', '7 of Clubs', '8 of Clubs', '9 of Clubs', '10 of Clubs', 'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',
            'Ace of Hearts', '2 of Hearts', '3 of Hearts', '4 of Hearts', '5 of Hearts', '6 of Hearts', '7 of Hearts', '8 of Hearts', '9 of Hearts', '10 of Hearts', 'Jack of Hearts', 'Queen of Hearts', 'King of Hearts',
            'Ace of Diamonds', '2 of Diamonds', '3 of Diamonds', '4 of Diamonds', '5 of Diamonds', '6 of Diamonds', '7 of Diamonds', '8 of Diamonds', '9 of Diamonds', '10 of Diamonds', 'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds']


# runs the tutorial
def tutorial():
    if rounds == 1:
        tut = input(f'''
Welcome to black jack, {user}. Do you know how to play (Y/N): ''')

        if tut.upper() == 'N':
            input('''
The rules are simple. The goal is to have a higher number than the dealer. The dealer will have one shown card and one hidden card. 
They then deal each player two cards and reveal their hand. If they have less than seventeen always will draw.
All face cards equal 10 and Aces equal both 1 and 11 (whichever is better for you at the time). 
Your goal is to get as close to twenty one with out going over. Anymore and you will bust/lose. 
You may Hit(draw another card), or you can stand(not draw another card). ''')


# Totals cards
def scoring():
    if dealer_total(dealer_hand) > user_total(player_hand) and dealer_total(dealer_hand) <= 21:
        print(f'''
The dealer ended with the higher total, sorry but you lose.''')
        next_round()
    elif dealer_total(dealer_hand) <= 21 and user_total(player_hand) > 21:
        print(f'''
The dealer didn't bust so they win''')
        next_round()
    elif dealer_total(dealer_hand) == user_total(player_hand) and dealer_total(dealer_hand) <= 21:
        print(f'''
{user} and the dealer has tied, better luck next time.''')
        next_round()
    elif dealer_total(dealer_hand) < user_total(player_hand) and user_total(player_hand) <= 21:
        print(f'''
Congrats, you beat the dealer!''')
        global wins
        wins += 1
        next_round()
    elif dealer_total(dealer_hand) > 21 and user_total(player_hand) <= 21:
        print(f'''
Congrats, you beat the dealer!''')
        wins += 1
        next_round()


# deals the cards
def deal_in():
    print(f'''
The dealer places the {dealer_hand[0]} face up and places another face down.
Next you are dealt the {player_hand[0]} and the {player_hand[1]} bringing your total to {user_total(player_hand)}''')
# Black jack
    if user_total(player_hand) == 21:
        input(f'''
Congrats you got a black jack!''')
        dealer_reveal()
    elif user_total(player_hand) < 21:
        hit_stand()


# Hit or stand
def hit_stand():
    if user_total(player_hand) <= 20:
        move = input('''
Would you like to hit or stand: ''')
# Hit
        while move.upper() == 'HIT' and user_total(player_hand) < 21:
            player_hand.append(new_card())
            input(f'''
You are dealt {player_hand[-1]} bringing your total to {user_total(player_hand)}''')
# Bust
            if user_total(player_hand) > 21:
                user_total(player_hand)
                if user_total(player_hand) <= 21:
                    input(f'''
Your Ace has decreased to a 1 saving you... for now... ''')
                    hit_stand()
                print(f'''
Sorry but that brings you to {user_total(player_hand)}, in other word thats a bust''')
                dealer_reveal()
# Hit or Stand
            elif user_total(player_hand) < 21:
                move = input('''
Would you like to hit or stand: ''')
# Score cap
            elif user_total(player_hand) == 21:
                input(f'''
{user} has hit the highest score''')
                dealer_reveal()
# Stand
        if move.upper() == 'STAND':
            input(f'''
You stand with a total of {user_total(player_hand)}.''')
            dealer_reveal()
    if move.upper() != 'STAND' or move.upper() != 'HIT':
        print(f'''
PLease enter a valid input ''')
        hit_stand()


# reveals dealers cards and determines winner
def dealer_reveal():
    input(f'''
The dealer flips their card revealing {dealer_hand[-1]} bringing their total to {dealer_total(dealer_hand)}''')
    if dealer_total(dealer_hand) < 17:
        while dealer_total(dealer_hand) < 17:
            dealer_hand.append(new_card())
            input(f'''
The dealer draws the {dealer_hand[-1]} bringing them to {dealer_total(dealer_hand)}''')
        if dealer_total(dealer_hand) > 21 and user_total(player_hand) > 21:
            input(f'''
The dealer also busted! In other words you still lose... but it could be worse''')
            next_round()
        elif dealer_total(dealer_hand) > 21 and user_total(player_hand) <= 21:
            input(f'''
The dealer hit a total of {dealer_total(dealer_hand)}! In other words they busted''')
            global wins
            wins += 1
            next_round()
        elif dealer_total(dealer_hand) < user_total(player_hand) and user_total(player_hand) <= 21:
            input(f'''
Congrats, you beat the dealer! ''')
            wins += 1
            next_round()
        elif dealer_total(dealer_hand) >= 17:
            scoring()
    elif dealer_total(dealer_hand) >= 17:
        scoring()


# starts the next round
def next_round():
    play_again = input('''
Would you like to play again (Y/N): ''')
    if play_again.upper() == 'Y':
        global rounds
        rounds += 1
        input(f'''
Alright on to round {rounds}, Good luck!''')
        dealer_hand.clear()
        dealer_hand.append(new_card())
        dealer_hand.append(new_card())
        player_hand.clear()
        player_hand.append(new_card())
        player_hand.append(new_card())
        deal_in()
    elif play_again.upper() == 'N':
        print(f'''
Thank you for playing, You won {wins} out of {rounds}.
''')
        quit()
    elif play_again.upper() != 'Y' and play_again.upper() != 'N':
        print('''
Please enter a valid input''')
        next_round()


# user hand total calculator
def user_total(hand):
    player_total = 0
    global pl_aces
    pl_aces = 0
    for i in range(len(hand)):
        txt = str(hand[i])
        Two = re.search("2", txt)
        Three = re.search("3", txt)
        Four = re.search("4", txt)
        Five = re.search("5", txt)
        Six = re.search("6", txt)
        Seven = re.search("7", txt)
        Eight = re.search("8", txt)
        Nine = re.search("9", txt)
        Ten = re.search("10", txt)
        Jack = re.search("Jack", txt)
        Queen = re.search("Queen", txt)
        King = re.search("King", txt)
        Ace = re.search("Ace", txt)

        if Two:
            player_total += 2
        elif Three:
            player_total += 3
        elif Four:
            player_total += 4
        elif Five:
            player_total += 5
        elif Six:
            player_total += 6
        elif Seven:
            player_total += 7
        elif Eight:
            player_total += 8
        elif Nine:
            player_total += 9
        elif Ten or Jack or Queen or King:
            player_total += 10
        elif Ace:
            if player_total <= 10 and pl_aces == 0:
                player_total += 11
                pl_aces += 1
            elif player_total > 10 and player_total <= 21:
                player_total += 1
        while pl_aces > 0 and player_total > 21:
            player_total -= 10
            pl_aces -= 1

    return (player_total)


# dealer hand total calculator
def dealer_total(hand):
    house_total = 0
    global house_aces
    house_aces = 0
    for i in range(len(hand)):
        txt = str(hand[i])
        Two = re.search("2", txt)
        Three = re.search("3", txt)
        Four = re.search("4", txt)
        Five = re.search("5", txt)
        Six = re.search("6", txt)
        Seven = re.search("7", txt)
        Eight = re.search("8", txt)
        Nine = re.search("9", txt)
        Ten = re.search("10", txt)
        Jack = re.search("Jack", txt)
        Queen = re.search("Queen", txt)
        King = re.search("King", txt)
        Ace = re.search("Ace", txt)

        if Two:
            house_total += 2
        elif Three:
            house_total += 3
        elif Four:
            house_total += 4
        elif Five:
            house_total += 5
        elif Six:
            house_total += 6
        elif Seven:
            house_total += 7
        elif Eight:
            house_total += 8
        elif Nine:
            house_total += 9
        elif Ten or Jack or Queen or King:
            house_total += 10
        elif Ace:
            if house_total <= 10 and house_aces == 0:
                house_total += 11
                house_aces += 1
            elif house_total > 10 and house_total <= 21:
                house_total += 1
        while house_aces > 0 and house_total > 21:
            house_total -= 10
            house_aces -= 1

    return (house_total)


# dealer hand
dealer_hand = [new_card(), new_card()]
dealer_total(dealer_hand)


# player hand
player_hand = [new_card(), new_card()]
user_total(player_hand)


# bot hand
bot_hand = [new_card(), new_card()]


# main function
def black_jack():
    global game_state
    game_state = True

    input('''
Welcome to Black Jack, also known as 21. Enter anything to start: ''')

    global user
    user = input('''
What is your name: ''')

    while game_state == True:
        tutorial()

        deal_in()


if __name__ == "__main__":
    black_jack()


"""
This is v1 of blackjack. It is currently missing the following:
1. spliting: having two same value cards in your first dealt cards that you may split in two hands
2. betting: money
3. doubling: double your preset bet 
4. surrendering: bailing out after seeing the dealers cards
"""