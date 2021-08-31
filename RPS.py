# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

from RPS_game import play

my_guess = {"P": "S", "R": "P", "S": "R"}
my_moves = ["R"]
opponent_history = []
probabilites = [0, 0, 0, 0]
opponent = ["", "", "", ""]
me = ["", "", "", ""]
opponent_plays = {}
my_plays = {}
RPS = ["R", "P", "S"]

def player(prev_play):
    if prev_play in RPS:
        opponent_history.append(prev_play)
        i = 0
        while i < 4:
            if opponent[i] == prev_play:
                probabilites[i] += 1
            i += 1
    else:
        clear()

    last_ten = my_moves[-10:]
    if len(last_ten) > 0:
        RPS_0 = [last_ten.count("R"), last_ten.count("P"), last_ten.count("S")]
        index = RPS_0.index(max(RPS_0))

        move = RPS[index]

        opponent[0] = my_guess[move]
        me[0] = my_guess[opponent[0]]

    if len(my_moves) > 0:
        my_prev_play = my_moves[-1]
        opponent[1] = my_guess[my_prev_play]
        me[1] = my_guess[opponent[1]]

    if len(opponent_history) >= 3:

        if "".join(opponent_history[-3:]) in opponent_plays.keys():
            opponent_plays["".join(opponent_history[-3:])] += 1
        else:
            opponent_plays["".join(opponent_history[-3:])] = 1

        guesses = ["".join(opponent_history[-(3 - 1) :]) + k for k in RPS]
        for g in guesses:
            if not g in opponent_plays.keys():
                opponent_plays[g] = 0

        move = max(guesses, key=lambda key: opponent_plays[key])

        opponent[2] = move[-1]
        me[2] = my_guess[opponent[2]]

    if len(my_moves) >= 2:
        if "".join(my_moves[-2:]) in my_plays.keys():
            my_plays["".join(my_moves[-2:])] += 1
        else:
            my_plays["".join(my_moves[-2:])] = 1

        guesses = ["".join(my_moves[-(2 - 1) :]) + k for k in RPS]
        for g in guesses:
            if not g in my_plays.keys():
                my_plays[g] = 0

        move = max(guesses, key=lambda key: my_plays[key])

        opponent[3] = my_guess[move[-1]]
        me[3] = my_guess[opponent[3]]

    max_index = probabilites.index(max(probabilites))
    guess = me[max_index]
    if guess == "":
        guess = "S"
    my_moves.append(guess)
    return guess

def clear():
    global my_moves, opponent_history, probabilites, opponent, me, opponent_plays, my_plays
    my_moves = ["R"]
    opponent_history.clear()
    probabilites = [0, 0, 0, 0]
    opponent = ["", "", "", ""]
    me = ["", "", "", ""]
    opponent_plays = {}
    my_plays = {}



































