con = "yes"
while con.upper() != "NO":
    a = input("player_a: please enter your selection: ")
    b = input("player_b: please enter your selection: ")
    if a == b:
        print("DRAW")
    elif a.upper() == "ROCK":
        if b.upper() == "SCISSORS":
            print("Congratulations Plaer A You Won!")
        else:
            print("Player B you WON")
    elif a.upper() == "SCISSORS":
        if b.upper() == "PAPER":
            print("Player A Won")
        else:
            print("Player B Won")
    elif a.upper() == "PAPER":
        if b.upper() == "SCISSORS":
            print("Player B Won")
        else:
            print("Player A Won")
    else:
        print("Error You entered a have not entered rock, paper os scissors please try again")
    con = input("so you want to play again? ")


