while True:
    Player1 = input("Player 1: Rock, paper, or scissors? ").lower()
    Player2 = input("Player 2: Rock, paper, or scissors? ").lower()

    valid_answers = ("rock", "paper", "scissors")

    if Player1 not in valid_answers or Player2 not in valid_answers:
        print("Not valid")
        continue

    if Player1 == Player2:
        print("Tie")

    elif (Player1 == "rock" and Player2 == "scissors") or \
         (Player1 == "paper" and Player2 == "rock") or \
         (Player1 == "scissors" and Player2 == "paper"):
        print("Player 1 won")
    else:
        print("Player 2 won")
