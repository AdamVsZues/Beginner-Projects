import random

user_name = input("What is your name: ")

user_wins = 0

bot_wins = 0

gamestate = True

while gamestate == True:
    usermove = input("Rock, Paper, or Scissors: ")

    roshambo = random.choice(["Rock", "Paper", "Scissors"])

    print(f'Bot played {roshambo}')

    if (usermove.upper() == "ROCK" and roshambo == "Paper") or (usermove.upper() == "PAPER" and roshambo ==     "Scissors") or (usermove.upper() == "SCISSORS" and roshambo == "Rock"):
        bot_wins += 1 
        print(f'Sorry, you loose, {user_name}: {user_wins}, Bot: {bot_wins}')
        play_again = input('Would you like to play again (y,n): ')
        if play_again.upper() == 'N':
            gamestate = False
    elif (usermove.upper() == "ROCK" and roshambo == "Rock") or (usermove.upper() == "PAPER" and roshambo ==    "Paper") or (usermove.upper() == "SCISSORS" and roshambo == "Scissors"):
        print(f"It's a draw! {user_name}: {user_wins}, Bot: {bot_wins}")
        play_again = input('Would you like to play again (y,n): ')
        if play_again.upper() == 'N':
            gamestate = False
    elif (usermove.upper() == "ROCK" and roshambo == "Scissors") or (usermove.upper() == "PAPER" and roshambo   == "Rock") or (usermove.upper() == "SCISSORS" and roshambo == "Paper"):
        user_wins += 1 
        print(f"Congrats, you win! {user_name}: {user_wins}, Bot: {bot_wins}")
        play_again = input('Would you like to play again (y,n): ')
        if play_again.upper() == 'N':
            gamestate = False
    else:
        print(f'Enter a valid option')
