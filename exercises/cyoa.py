"""Choose Your Own Adventure: Number Guessing Game."""
__author__ = "730394136"

import random
points: int = 0
player: str = ""
STAR_EYES: str = "\U0001F929"
CELEBRATE: str = "\U0001F973"
SAD_FACE: str = "\U0001F631"
BYE: str = "\U0001F44B"


def greet() -> None:
    """Welcome message."""
    global player
    print(f"Welcome to the number guessing game. The object of the game is to guess a number between 1 and 10 in 4 attempts.{STAR_EYES}")
    player = input("What is your name? ")


def guess(xs: int) -> int:
    """Begin Guessing Numbers."""
    global player
    guessing: int = int(input("Guess a number between 1 and 10: "))
    while guessing != 6: 
        xs += 1
        guessing = int(input("That was not correct! Try again: "))
    print(f"Congrats, {player} you have {xs} points!")
    return xs


def game(input_guess: int) -> None:
    """Game loop with hints."""
    number: int = random.randint(1, 10)
    attempts: int = 4
    global points 
    global player

    while attempts > 0 and input_guess != number:
        print(f"{attempts} attempts left.")

        if input_guess == number: 
            print("Yay! You guessed the correct number!{CELEBRATE}")
        elif input_guess > number: 
            number = int(input("Your guess is too high! Try again: "))
            attempts -= 1
        elif input_guess < number:
            number = int(input("Your guess is too low! Try again: "))
            attempts -= 1
    if attempts == 0:
        print(f"Out of attempts. The number was {number}. Better luck next time, {player}!{SAD_FACE}")
    points += input_guess 


def goodbye() -> str:
    """Goodbye message."""
    global points
    print(f"You have {points} adventure points. Thank you for playing, goodbye!{BYE}")


def main() -> None:
    """The entrypoint of the program and main game loop."""
    greet()
    guess_response: int = guess(0)
    game(guess_response)
    goodbye()


if __name__ == "__main__":
    main()