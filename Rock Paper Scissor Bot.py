import numpy as np



def random_number(x, y):
    """
    Takes an integer x, and randomly generates a number between x and y, inclusive.

    :param
        x: an integer
        y: an integer
    :return:
        an integer
    """
    return np.random.randint(x, y+1)


def bot_move_to_console(move):
    if (move == 0):
        print("Bot used scissors!\n")
    elif (move == 1):
        print("Bot used rock!\n")
    elif (move == 2):
        print("Bot used paper!\n")
    else:
        print("Invalid move!\n")


def player_input():
    return input("Type \"rock\", \"paper\" or \"scissor\" to make a move.\n")

def player_response(input_):
    if ((input_ == "rock") or (input_ == "r") or (input_ == "R")):
        print("player used rock\n")
    elif (input_ == "scissors") or (input_ == "scissor") or (input_ == "s") or (input_ == "S"):
        print("player used scissors\n")
    elif (input_ == "paper") or (input_ == "p") or (input_ == "P"):
        print("player used paper\n")
    else:
        print("player used an invalid move\n")


def decider():
    move = random_number(0,2)
    input_ = player_input()
    player_response(input_)
    bot_move_to_console(move)
    if (input_ == "rock") and (move == 0):
        print("player wins\n")
    elif (input_ == "paper") and (move == 0):
        print("bot wins\n")
    elif (input_ == "scissors") and (move == 0):
        print("tie\n")
    elif (input_ == "rock") and (move == 1):
        print("tie\n")
    elif (input_ == "paper") and (move == 1):
        print("player wins\n")
    elif (input_ == "scissors") and (move == 1):
        print("bot wins\n")
    elif (input_ == "rock") and (move == 2):
        print("bot wins\n")
    elif (input_ == "paper") and (move == 2):
        print("tie\n")
    elif (input_ == "scissors") and (move == 2):
        print("player wins\n")

def Main():
    decider()



if __name__ == "__main__":
    Main()