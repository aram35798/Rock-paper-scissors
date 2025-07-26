while True:
    Player1 = input("Player 1: Rock, paper, or scissors? ").lower()
    Player2 = input("Player 2: Rock, paper, or scissors? ").lower()

    Valid_answer = ("rock", "paper", "scissors")

    if Player1 not in Valid_answer or Player2 not in Valid_answer:
        print("Fuck dude")
        continue

    if Player1 == Player2:
        print("fuck")

    elif Player1 == ("rock" and Player2 == "scissors"):
        print("Player 1")
    else:
        print("2 won")
''' if player 1:
        pick rock paper or scissor
    now player 2 pick 
    now compare them 
    compare them to different events and see which one it matches
'''