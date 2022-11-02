theBoard = {'1': ' ' , '2': ' ' , '3': ' ' , 
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'] +"\n")

def instructions():
    print("\nThe point of the game is to get three of your chosen icons in a row")
    print("Here is how the board is set up:\n")
    print("1" + '|' + "2"+ '|' + "3")
    print('-+-+-')
    print("4" + '|' + "5" + '|' + "6")
    print('-+-+-')
    print("7" + '|' + "8" + '|' + "9\n")

def turn(c,tB,symbol):
    move = input("Where would you like to go?\n")
    if tB[move] == ' ':
        tB[move] = symbol
        printBoard(tB)
        c += 1
    else:
        print("Oh no! That space is already taken! \nPlease try again next turn.")

    return(tB,symbol)

def vibeCheck(tB,s,name):
    if tB["1"] ==  tB["2"] ==  tB["3"] !=  ' ':
        determineWinner(tB,s,name)
    elif tB["4"] ==  tB["5"] ==  tB["6"] !=  ' ':
        determineWinner(tB,s,name)
    elif tB["7"] ==  tB["8"] ==  tB["9"] !=  ' ':
        determineWinner(tB,s,name)
    elif tB["1"] ==  tB["5"] ==  tB["9"] !=  ' ':
        determineWinner(tB,s,name)
    elif tB["3"] ==  tB["5"] ==  tB["7"] !=  ' ':
        determineWinner(tB,s,name)
    elif tB["1"] ==  tB["4"] ==  tB["7"] !=  ' ':
        determineWinner(tB,s,name)
    elif tB["2"] ==  tB["5"] ==  tB["8"] !=  ' ':
        determineWinner(tB,s,name)
    elif tB["3"] ==  tB["6"] ==  tB["9"] !=  ' ':
        determineWinner(tB,s,name)

def determineWinner(tB,s,name):
    if tB["1"] ==  tB["2"] ==  tB["3"] == s:
        print(name + "is the winner!")
    elif tB["4"] ==  tB["5"] ==  tB["6"] == s:
        print(name + "is the winner!")
    elif tB["7"] ==  tB["8"] ==  tB["9"] == s:
        print(name + "is the winner!")
    elif tB["1"] ==  tB["5"] ==  tB["9"] == s:
        print(name + "is the winner!")
    elif tB["3"] ==  tB["5"] ==  tB["7"] == s:
        print(name + "is the winner!")
    elif tB["1"] ==  tB["4"] ==  tB["7"] == s:
        print(name + "is the winner!")
    elif tB["2"] ==  tB["5"] ==  tB["8"] == s:
        print(name + "is the winner!")
    elif tB["3"] ==  tB["6"] ==  tB["9"] == s:
        print(name + "is the winner!")

def main():
    ex = 'X'
    oh = 'O'
    count = 0   
    r = 0

    check = input("Would you like to see the instructions? (Y/N)")
    if check == "Y":
        instructions()

    n1 = input("Player 1, what is your name?")
    n2 = input("Player 2, what is your name?")

    while count <= 9:
        r += 1
        print("\nRound " + str(r) + "\n")
        printBoard(theBoard)

        print(n1 + ", it is your turn")
        turn(count,theBoard,ex)
        vibeCheck(theBoard,ex,n1)

        print("\n" + n2 + ", it is your turn")
        turn(count,theBoard,oh)
        vibeCheck(theBoard,oh,n2)

        if count == 9:
            print("GAME OVER")
            print("No one wins! :(")
            break

    print("The End")
        
main()