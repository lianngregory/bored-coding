def read():
    myfile = open("stats.txt",'r') #opens empty file!
    stats = [] #to be filled in
    for line in myfile: #for each line, strips extra stuff and appends it!
        line = line.strip() 
        stats.append(line)
    myfile.close() #closes empty txt file!
    return(stats)

def instructions():
    print("\nRock Paper Scissors is a classic two-person game")
    print("Players start each round by saying, 'rock, paper, scissors, shoot'")
    print("On “shoot,” each player holds out their fist for rock, flat hand for paper, or their index and middle finger for scissors.\n")
    print("     1. Rock crushes scissors")
    print("     2. Scissors cut paper")
    print("     3. Paper covers rock")

    cont = input("\nAre you ready to continue? Type 'Y' when you are ready to proceed.")
    if cont == "y":
        return()
        

def start(p1,p2,stats,date):
    r = 0
    turn1 = 0
    turn2 = 0
    win = 0

    while r < 3:
        r += 1
        print("\nRound " + str(r) + "\n")

        print(p1 + ", what do you choose?")
        c1 = choose(p1,turn1)

        print("\n" + p2 + ", what do you choose?")
        c2 = choose(p2,turn2)
        
        w = vibeCheck(p1,p2,c1,c2,win)
        #win isnt working, need to create a new variable or something

    win(p1,p2,w,stats,date)


def choose(p,t):
    print("\nHere are your choices:\n")
    print("     1. Rock")
    print("     2. Paper")       
    print("     3. Scissors")
    choice = input("\nWhat would you like to do? (Please choose the numerical value associated)\n")
    if choice == "1":
        v = 1
    elif choice == "2":
        v = 4
    elif choice == "3":
        v = 3

    return(v)


def vibeCheck(p1,p2,t1,t2,win):
    sum = int(t1) + int(t2)

    #fix math

    if sum == 2:
        print("\nNo one wins this round")
    elif sum == 4:
        if t1 == 1:
            win += 1
            print("\n" + p1 + " wins this round!")
        else:
            win += 2
            print("\n" + p2 + " wins this round!")
    elif sum == 5:
        if t1 == 4:
            win += 1
            print("\n" + p1 + " wins this round!")
        else:
            win += 2
            print("\n" + p2 + " wins this round!")
    elif sum == 6:
        print("\nNo one wins this round")
    elif sum == 7:
        if t1 == 3:
            win += 1
            print("\n" + p1 + " wins this round!")
        else:
            win += 2
            print("\n" + p2 + " wins this round!")
    elif sum == 8:
        print("\nNo one wins this round")

    return(win)

def win(p1,p2,w,s,d):
    if w % 2 != 0:
        print(p1 + " wins this game of Rock Paper Scissors!")
        print("Congratulations " + p1 + "!!!")
        s.append("Winner: " + p1 + " | " + str(d))
    elif w % 2 == 0:
        print(p2 + " wins this game of Rock Paper Scissors!")
        print("Congratulations " + p2 + "!!!")
        s.append("Winner: " + p2 + " | " + str(d))
    else:
        print("No one wins! :(")  

    return(p1,p2,w,s,d)

def view(gs):
    print()
    for line in gs: #prints each thing on a different line!
        print(line)
    print()

def main():
    import datetime
    dt = datetime.datetime.now()

    keepGoing = True
    game_stats = read()

    print("\nWelcome to Rock Paper Scissors!\n")
    print("Today is: " + str(dt))

    player1 = input("\nPlayer 1, what is your name?")
    player2 = input("\nPlayer 2, what is your name?")

    print("\nWelcome " + player1 + " and " + player2 + "!!")

    while keepGoing == True: #while loop that ensures that the user can keep making choices until they want to exit!
        print("\nWhat would you like to do?!\n")
        print("     1. Hear the Instructions")
        print("     2. Start the Game")       
        print("     3. Hear the Stats")
        print("     4. Exit\n")
        choice = input("What would you like to do? (Please choose the numerical value associated)\n")
        if choice == "1":
            instructions()
            keepGoing = True
        elif choice == "2":
            start(player1,player2,game_stats,dt)
            keepGoing = True
        elif choice == "3":
            view(game_stats)
            keepGoing = True
        elif choice == "4": #choice to end while loop, makes keepGoing false :(
            keepGoing = False
            myfile = open("stats.txt",'a') #opens empty file!
            for line in game_stats: #for each line, strips extra stuff and appends it!
                myfile.write(line+"\n")
            myfile.close() #closes empty txt file!
        else:
            break
    

    start()


main()