import random

def play():
    rnd = random.randint(1,3)
    ans = str(input("Rock, paper, scissors? "))

    if (ans == "rock"):
        if (rnd == 1):
            print("Computer plays rock. It's a tie.")
        if (rnd == 2):
            print("Computer plays paper. You lose.")
        if (rnd == 3):
            print("Computer plays scissors. You win.")
    if (ans == "paper"):
        if (rnd == 1):
            print("Computer plays rock. You win.")
        if (rnd == 2):
            print("Computer plays paper. It's a tie.")
        if (rnd == 3):
            print("Computer plays scissors. You lose.")
    if (ans == "scissors"):
        if (rnd == 1):
            print("Computer plays rock. You lose.")
        if (rnd == 2):
            print("Computer plays paper. You win.")
        if (rnd == 3):
            print("Computer plays scissors. It's a tie.")
    play()
    
play()
