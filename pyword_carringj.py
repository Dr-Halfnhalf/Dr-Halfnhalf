"""
Author: John Carrington-Warren, carringj@purdue.edu
Assignment: 12.1 - Pyword
Date: 04/19/2022

Description:
    This program is a variation of the game wordle. When the program start,
    you are taken into a main menu that gives you three options. The first option
    is to play the game. By selecting this, you will be asked your name and then
    the first round begins. In each round, you have six turns to guess the randomly
    chosen word. There will be a key with all of the letters that will help you
    see what letters have been used. After three rounds, your total score will be 
    compared to the leaderboard and you can possible make it. The second option
    on the main menu is to show the current leaderboard. The third is to quit
    out of the game.

Contributors:
    None

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import random as r
import string
"""Write new functions below this line (starting with unit 4)."""
#This begins the main menu wher you can select different options
def main_menu():
    while True:
        print('\n----- Main Menu -----')
        print('1. New Game\n2. See Hall of Fame\n3. Quit')
        choice = input('\nWhat would you like to do? ')
        if choice == '1':
            name = input("Enter your player name: ")
            game_time(name)
            break
        elif choice == '2':
            players, scores = read_HOF()
            scoreboard(scores,players)
        elif choice == '3':
            print('Goodbye.')
            break
        else:
            print('\nInvalid choice. Please try again.')
#This function ties all of the game-related function together
def game_time(name):
    total = 0
    words = unload_words()
    g_words = pick_game_words(words)
    for rounds in range(3):
        total += game(g_words[rounds],rounds)
    winner(name,total)
    main_menu()
#This unload all of the secret words used for game onto a list
def unload_words():
    secret = []
    with open('words.txt','r') as wrd:
        for line in wrd:
            secret.append(line.rstrip().lower())
    return(secret)
#This picks the three words that will be used for the game.
def pick_game_words(words):
    chosen = r.sample(words,3)
    return chosen
#This function goes through a round of the game
def game(chosen,round):
    spaces = []
    spaces.clear()
    print(f"\nRound {round+1}:")
    for t in range(26):
        spaces.append(' ')
    for turns in range(1,7):
        while True:
            guess = input(f"{turns}? ")
            if guess.isalpha() and len(guess) == 5:
                break
            elif len(guess) != 5:
                print('\nInvalid guess. Please enter exactly 5 characters.\n')
            else:
                print('\nInvalid guess. Please only enter letters.\n')
        alp = list(string.ascii_lowercase)
        ans,spaces = difference(guess, chosen, alp,spaces)
        out1 = ''.join(ans)
        out2 = ''.join(spaces)
        alp1 = ''.join(alp)
        print(f'   {out1}     {out2}')
        print(f'   {guess.lower()}     {alp1}')
        if guess.lower() == chosen:
            points = accolade(6 - turns)
            break
    if guess.lower() != chosen:
        points = 0
        print("You ran out of tries.")
        print(f"The word was {chosen}.")
    return points
#This function is used to tell the difference between the guess and chosen word
def difference(guess,chosen,alp,spaces):
    diff = []
    guess = guess.lower()
    for t in range(len(guess)):
        if guess[t] in chosen:
            if guess[t] == chosen[t]:
                diff.append('!')
            else:
                diff.append('?')
        else:
            diff.append('X')
        position = alp.index(guess[t])
        if diff[t] == '!':
            spaces[position] = diff[t]
        else:
            if spaces[position] != '!' and diff[t] == '?':
                spaces[position] = diff[t]
            else:
                if spaces[position] != '!' and spaces[position] != '?':
                    spaces[position] = diff[t]
    return diff, spaces
#This function tells you what accolade you have achieved from your total score
def accolade(turns):
    accolade = {0:'Phew', 1:'Great', 2:'Splendid', 3:'Impressive',
                4:'Magnificent', 5:'Genius', 6:'Impossible'}
    points = 2**(turns)
    print(f"{accolade[turns]}! You earned {points} points this round.")
    return points
#This takes the score and names of previous players who have made it on the
#leaderboard and puts it into a list
def read_HOF():
    scores = []
    players = []
    with open('hall_of_fame.txt','r') as HOF:
        for lines in HOF:
            line = lines.split(', ')
            line[0] = line[0].rstrip()
            if line[0] == '':
                break
            scores.append(int(line[0]))
            players.append(line[1].rstrip())
    return players, scores
#This prints the scoreboard
def scoreboard(scores,players):
    print("\n--- Hall of Fame ---\n ## : Score : Player")
    for t in range(len(players)):
        print(f' {(t+1):2d} :   {scores[t]:3d} : {players[t]}')
#This determines if the current player makes the leaderboard by comparing it
#to previous players
def winner(name,total):
    players, scores = read_HOF()
    if len(scores) == 0:
        scores.append(total)
        players.append(name)
        modify_winners(players,scores,name,total)
    else:
        if min(scores) >= total:
            if len(scores) >= 10:
                print(f"\nYou earned a total of {total} points.")
            else:
                scores.append(total)
                players.append(name)
                modify_winners(players,scores,name,total)
        else:
            for t in range(len(players)):
                if total > scores[t]:
                    scores.insert(t,total)
                    players.insert(t,name)
                    if len(scores) >= 10:
                        scores.pop()
                        players.pop()
                    modify_winners(players,scores,name,total)
                    break
                    
#This modifies the list of leaderboard players and writes a new text doc
#with thier names and scores
def modify_winners(player,score,name,total):
    lines = []
    with open('hall_of_fame.txt','w') as HOF:
        for t in range(len(player)):
            lines.append(str(score[t]))
            lines.append(player[t])
            line = ", ".join(lines)
            HOF.write(f'{line}\n')
            lines.clear()
    print(f"\nWay to go {name}!")
    print(f"You earned a total of {total} points and made it into the Hall of Fame!")
    scoreboard(score,player)
def main():
#This introduces the game and brings you into the main menu
    print("Welcome to PyWord.")
    main_menu()
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
