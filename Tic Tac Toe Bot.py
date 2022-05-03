def main():
    ticTacToe()

def ticTacToe():
    row1 = [None,None,None]
    row2 = [None,None,None]
    row3 = [None,None,None]
    turnNum = 1
    mode = gamemode()
    if (mode != "Bot") and (mode != "Player") and (mode != "bot") and (mode != "player"):
        exit(print("Invalid Gamemode"))
    print("Now playing against",mode)
    result = None
    board(row1,row2,row3)
    while (result == None):
        print("Player 1's turn")
        eCheck = False
        while (eCheck == False):
            p1movR = player1MoveRow()
            p1movC = int(player1MoveCol()) - 1
            if (p1movR[0] == "1"):
                if (row1[p1movC] != None):
                    print("Please enter a valid space")
                else:
                    eCheck = True
            elif (p1movR[0] == "2"):
                if (row2[p1movC] != None):
                    print("Please enter a valid space")
                else:
                    eCheck = True
            elif (p1movR[0] == "3"):
                if (row3[p1movC] != None):
                    print("Please enter a valid space")
                else:
                    eCheck = True
            else:
                print("Please enter a valid row")
        if (p1movR[0] == "1"):
            if (row1[p1movC] == None):
                row1[p1movC] = "X"
                turnNum = turnNum + 1
        elif (p1movR[0] == "2"):
            if (row2[p1movC] == None):
                row2[p1movC] = "X"
                turnNum = turnNum + 1
        elif (p1movR[0] == "3"):
            if (row3[p1movC] == None):
                row3[p1movC] = "X"
                turnNum = turnNum + 1
        else:
            print("ERROR INVALID ROW")
        board(row1, row2, row3)
        result = checker(row1,row2,row3)
        tieCheck(turnNum)
        if (result == "win"):
            print("Player 1 Wins")
            playagain = replay()
            gamereset(playagain)
        if (mode == "Bot") or (mode == "bot"):
            botMoveCheck = False
            while (botMoveCheck == False):
                bmovR = randomNum(1,3)
                bmovC = randomNum(0,2)
                if (bmovR == 1):
                    if (row1[bmovC] == None):
                        row1[bmovC] = "O"
                        print("Bot made a move")
                        turnNum = turnNum + 1
                        botMoveCheck = True
                if (bmovR == 2):
                    if (row2[bmovC] == None):
                        row2[bmovC] = "O"
                        print("Bot made a move")
                        turnNum = turnNum + 1
                        botMoveCheck = True
                if (bmovR == 3):
                    if (row3[bmovC] == None):
                        row3[bmovC] = "O"
                        print("Bot made a move")
                        turnNum = turnNum + 1
                        botMoveCheck = True

        checker(row1,row2,row3)
        if (mode == "Player") or (mode == "player"):
            eCheck = False
            while (eCheck == False):
                p2movR = player2MoveRow()
                p2movC = int(player2MoveCol()) - 1
                if (p2movR[0] == "1"):
                    if (row1[p2movC] != None):
                        print("Please enter a valid space")
                    else:
                        eCheck = True
                elif (p2movR[0] == "2"):
                    if (row2[p2movC] != None):
                        print("Please enter a valid space")
                    else:
                        eCheck = True
                elif (p2movR[0] == "3"):
                    if (row3[p2movC] != None):
                        print("Please enter a valid space")
                    else:
                        eCheck = True
                else:
                    print("Please enter a valid row")
            if (p2movR[0] == "1"):
                if (row1[p2movC] == None):
                    row1[p2movC] = "O"
                    turnNum = turnNum + 1
            elif (p2movR[0] == "2"):
                if (row2[p2movC] == None):
                    row2[p2movC] = "O"
                    turnNum = turnNum + 1
            elif (p2movR[0] == "3"):
                if (row3[p2movC] == None):
                    row3[p2movC] = "O"
                    turnNum = turnNum + 1
        board(row1,row2,row3)
        result = checker(row1, row2, row3)
        if (result == "loss"):
            if (mode == "player") or (mode == "Player"):
                print("Player 2 wins")
                playagain = replay()
                gamereset(playagain)
            if (mode == "Bot") or (mode == "bot"):
                print("Bot wins")
                playagain = replay()
                gamereset(playagain)

def gamemode():
    return input ("Type Bot to play against bot or Player to play against player\n")

def player1MoveRow():
    return input ("Player 1 type row of move\n")

def player1MoveCol():
    return input ("Player 1 type column of move\n")

def player2MoveRow():
    return input ("Player 2 type row of move\n")

def player2MoveCol():
    return input ("Player 2 type column of move\n")

def checker(row1,row2,row3):
    if (row1 == ["X","X","X"]) or (row2 == ["X","X","X"]) or (row3 == ["X","X","X"]):
        return "win"
    elif (row1[0] == "X") and (row2[0] == "X") and (row3[0] == "X"):
        return "win"
    elif (row1[1] == "X") and (row2[1] == "X") and (row3[1] == "X"):
        return "win"
    elif (row1[2] == "X") and (row2[2] == "X") and (row3[2] == "X"):
        return "win"
    elif (row1[0] == "X") and (row2[1] == "X") and (row3[2] == "X"):
        return "win"
    elif (row1[2] == "X") and (row2[1] == "X") and (row3[0] == "X"):
        return "win"
    elif (row1 == ["O","O","O"]) or (row2 == ["O","O","O"]) or (row3 == ["O","O","O"]):
        return "loss"
    elif (row1[0] == "O") and (row2[0] == "O") and (row3[0] == "O"):
        return "loss"
    elif (row1[1] == "O") and (row2[1] == "O") and (row3[1] == "O"):
        return "loss"
    elif (row1[2] == "O") and (row2[2] == "O") and (row3[2] == "O"):
        return "loss"
    elif (row1[0] == "O") and (row2[1] == "O") and (row3[2] == "O"):
        return "loss"
    elif (row1[2] == "O") and (row2[1] == "O") and (row3[0] == "O"):
        return "loss"
    else:
        return None

def board(row1,row2,row3):
    print(row1)
    print(row2)
    print(row3)

def replay():
    return input("Would you like to play again?\nType Yes or No\n")

def tieCheck(turnNum):
    if (turnNum >= 10):
        print("The game has ended in a tie")
        playagain = replay()
        gamereset(playagain)


import numpy as np

def randomNum(x, y):
    return np.random.randint(x, y+1)

def gamereset(playagain):
    if (playagain == "Yes") or (playagain == "yes") or (playagain == "Y") or (playagain == "y"):
        exit(ticTacToe())
    elif (playagain == "No") or (playagain == "no") or (playagain == "N") or (playagain == "n"):
        exit(print("Thank you for playing"))
    else:
        exit(print("Invalid Option\nThank you for playing"))

main()