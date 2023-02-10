"""EX02 - One-Shot Wordle - Loops!"""
__author__ = "730394136"

SECRET: str = "python"
guess: str = input("What is your 6-letter guess? ")
playing: bool = True

idx: int = 0
emoji: str = ""

GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != len(SECRET):
    guess = input("That was not 6 letters! Try again: ")
while playing and idx < len(SECRET):
    if guess[idx] == SECRET[idx]:
        emoji = emoji + GREEN_BOX 
    else:
        yellow_letter: bool = False
        idx_2: int = 0
        while yellow_letter is not True and idx_2 < len(SECRET):
            if SECRET[idx] == guess[idx_2]:
                yellow_letter = True
            else:
                idx_2 = idx_2 + 1
        if yellow_letter is True:
            emoji = emoji + YELLOW_BOX
        if yellow_letter is False:
            emoji = emoji + WHITE_BOX 
    idx = idx + 1 

if guess != SECRET:
    print(emoji)
    print("Not quite. Play again soon")
    playing = False
if guess == SECRET: 
    print(emoji)
    print("Woo! You got it!")
    playing = False