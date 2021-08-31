# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

from RPS_game import play
from random import choices, randrange
import random

import numpy as np

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
        if prev_play == "R":
            guess1 = random.choice(["P", "S"])
        elif prev_play == "P":
            guess1 = random.choice(["S", "R"])
        elif prev_play == "S":
            guess1 = "P"
        else:
            guess1 = "P"
        
        me[0] = guess1

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

    max_prob = np.argmax(probabilites)
    guess = me[max_prob]
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

































































# import numpy as np

# ideal_response = {"P": "S", "R": "P", "S": "R"}
# my_moves = ["R"]
# opponent_history = []
# strategy = [0, 0, 0, 0]
# opponent_guess = ["", "", "", ""]
# strategy_guess = ["", "", "", ""]
# opponent_play_order = {}
# my_play_order = {}


# def player(prev_play):
#     if prev_play in ["R", "P", "S"]:
#         opponent_history.append(prev_play)
#         for i in range(0, 4):
#             if opponent_guess[i] == prev_play:
#                 strategy[i] += 1
#     else:
#         reset()

#     my_last_ten = my_moves[-10:]
#     if len(my_last_ten) > 0:
#         my_most_frequent_move = max(set(my_last_ten), key=my_last_ten.count)
#         opponent_guess[0] = ideal_response[my_most_frequent_move]
#         strategy_guess[0] = ideal_response[opponent_guess[0]]

#     if len(my_moves) > 0:
#         my_last_play = my_moves[-1]
#         opponent_guess[1] = ideal_response[my_last_play]
#         strategy_guess[1] = ideal_response[opponent_guess[1]]

#     if len(opponent_history) >= 3:
#         opponent_guess[2] = predict_move(opponent_history, 3, opponent_play_order)
#         strategy_guess[2] = ideal_response[opponent_guess[2]]

#     if len(my_moves) >= 2:
#         opponent_guess[3] = ideal_response[predict_move(my_moves, 2, my_play_order)]
#         strategy_guess[3] = ideal_response[opponent_guess[3]]

#     best_strategy = np.argmax(strategy)
#     guess = strategy_guess[best_strategy]
#     if guess == "":
#         guess = "S"
#     my_moves.append(guess)
#     return guess


# def predict_move(history, n, play_order):
#     if "".join(history[-n:]) in play_order.keys():
#         play_order["".join(history[-n:])] += 1
#     else:
#         play_order["".join(history[-n:])] = 1
#     possible = ["".join(history[-(n - 1) :]) + k for k in ["R", "P", "S"]]
#     for pm in possible:
#         if not pm in play_order.keys():
#             play_order[pm] = 0
#     predict = max(possible, key=lambda key: play_order[key])
#     return predict[-1]


# def reset():
#     global my_moves, opponent_history, strategy, opponent_guess, strategy_guess, opponent_play_order, my_play_order
#     my_moves = ["R"]
#     opponent_history.clear()
#     strategy = [0, 0, 0, 0]
#     opponent_guess = ["", "", "", ""]
#     strategy_guess = ["", "", "", ""]
#     opponent_play_order = {}
#     my_play_order = {}








































































# def player(prev_play, opponent_history=[]):
#     opponent_history.append(prev_play)

#     # try to loop opponent_history get every three

    # probabilities = {
    #         "RR": [1/3, 1/3, 1/3],
    #         "RP": [1/3, 1/3, 1/3],
    #         "RS": [1/3, 1/3, 1/3],
    #         "PP": [1/3, 1/3, 1/3],
    #         "PS": [1/3, 1/3, 1/3],
    #         "PR": [1/3, 1/3, 1/3],
    #         "SS": [1/3, 1/3, 1/3],
    #         "SR": [1/3, 1/3, 1/3],
    #         "SP": [1/3, 1/3, 1/3],
    #     }

    # def defeat_kris():

    #     if prev_play == "R":
    #         guess = "P"
    #     elif prev_play == "P":
    #         guess = "S"
    #     elif prev_play == "S":
    #         guess = "R"
    #     else:
    #         guess = "R"

    #     if len(opponent_history) >= 759:
    #         guess = prev_play

    #     return guess


#     RPS = ["R", "P", "S"]

#     guess = random.choice(RPS)


#     if len(opponent_history) > 3:

#         last_two = "".join(opponent_history[-3:-1])

#         if last_two in probabilities:
#             if prev_play == "R":
#                 probabilities[last_two][0] = (probabilities[last_two][0] + 1) / 3
#             elif prev_play == "P":
#                 probabilities[last_two][1] = (probabilities[last_two][1] + 1) / 3
#             elif prev_play == "S":
#                 probabilities[last_two][2] = (probabilities[last_two][2] + 1) / 3

#         last = "".join(opponent_history[-2:])

#         try:
#             index = probabilities[last].index(max(probabilities[last]))

#             if index == 0:
#                 guess = "P"
#             elif index == 1:
#                 guess = "S"
#             elif index == 2:
#                 guess = "R"
#             else:
#                 guess = random.choice(RPS)
#         except:
#             guess = defeat_kris()



#     return guess



















    # # only defeats quincy
    # def defeat_quincy():
        # if prev_play == "R":
        #     guess = random.choice(["P", "S"])
        # elif prev_play == "P":
        #     guess = random.choice(["S", "R"])
        # elif prev_play == "S":
        #     guess = "P"
        # else:
        #     guess = "P"
        
        # return guess

    # # defeat both quincy and mrugesh
    # def defeat_mrugesh():
    #     if prev_play == "R":
    #         guess = "P"
    #     elif prev_play == "P":
    #         guess = "S"
    #     elif prev_play == "S":
    #         guess = "R"
    #     else:
    #         guess = "R"

    #     return guess

    # def defeat_kris():

        # if prev_play == "R":
        #     guess = "P"
        # elif prev_play == "P":
        #     guess = "S"
        # elif prev_play == "S":
        #     guess = "R"
        # else:
        #     guess = "R"

        # if len(opponent_history) >= 759:
        #     guess = prev_play

        # return guess


    # # try to copy abbey's function

    # guess = defeat_quincy()
    # guess = defeat_mrugesh()
    # guess = defeat_kris()