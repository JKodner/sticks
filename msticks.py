import random
colors = ["R", "B"]
player_score = 0
com_score = 0
count = 1
TURNS = ' '
STICKS_COUNT = ' '
print """Welcome to the Sticks Game! In this game, both players have 6 sticks. Each sticks have 2 sides, with the color Red or Black on one side.

In this game, both players throw down their sticks, which will land on either color. The goal is to get as many sticks with the red side up as possible. The amount of Sticks that are Red side-up equal your Score for that round. Each Score will be added up after every round. The player who has the greater score at the end of the game wins.
-*-"""
while type(TURNS) != int:
    try:
        TURNS = int(raw_input("How many Rounds in this game do you want?"))
        TURNS = TURNS + 1
    except ValueError:
        print "-*-"
while type(STICKS_COUNT) != int:
    try:
        STICKS_COUNT = int(raw_input("How many Sticks do you want in each deck?"))
    except ValueError:
        print "-*-"
if type(TURNS) == int and type(STICKS_COUNT) == int:
    while count < TURNS:
        player_sticks = []
        com_sticks = []
        while len(player_sticks) < STICKS_COUNT:
            player_sticks.append(random.choice(colors))
        player_round_score = player_sticks.count('R')
        player_score = player_score + player_sticks.count('R')
        while len(com_sticks) < STICKS_COUNT:
            com_sticks.append(random.choice(colors))
        com_round_score = com_sticks.count('R')
        com_score = com_score + com_sticks.count('R')
        print "-*-"
        v = raw_input("Type any word to continue.")
        print "-*-"
        print "Round %d:" % count
        print "Your Deck: %s" % player_sticks
        print "Computer's Deck: %s" % com_sticks
        print "Your Score This Round: %d" % player_round_score
        print "Your Total Score: %s" % player_score
        print "Computer's Score This Round: %d" % com_round_score
        print "Computer's Total Score: %s" % com_score
        count += 1
    print "-*-" 
    print "The Final Scores were:"
    print "You: %d" % player_score
    print "Computer: %d" % com_score
    print "-*-"
    if player_score > com_score:
        print "You Win!"
    elif com_score > player_score:
        print "You Lose!"
    elif player_score == com_score:
        print "You and the Computer Tied! Play Again!"
