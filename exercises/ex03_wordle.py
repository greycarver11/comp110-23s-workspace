"""EX03 - Structured Wordle"""
__author__ = "730394136"

def contains_char(word: str, letter: str) -> bool:
    """Returns bool when testing if guess contains letter."""
    assert len(letter) == 1
    idx: int = 0
    while idx < len(word):
        if word[idx] == letter:
            return True 
        idx = idx + 1
    return False

GREEN_BOX: str = "\U0001F7E9"
WHITE_BOX: str = "\U00002B1C"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret: str) -> str:
    """Returns secret's different colored emojis according to guess."""
    assert len(guess) == len(secret)
    idx: int = 0
    emoji: str = ""
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            emoji = emoji + GREEN_BOX
        elif contains_char(secret,guess[idx]):
            emoji = emoji + YELLOW_BOX
        else:
            emoji = emoji + WHITE_BOX
        idx = idx + 1
    return emoji

def input_guess(length: int) -> str:
    """Returns user's guess of expected length."""
    guess: str = input(f"Enter a {length} character word: ")
    while len(guess) != length:
        guess = input(f"That was not {length} chars! Try again: ")
    if len(guess) == length:
        return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    turns: int = 1 
    playing: bool = False 
    
    while turns <= 6 and not playing:
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        emoji = emojified(guess, secret)
        print(emoji)

        if guess == secret:
            print(f"You won in {turns}/6 turns!")
            playing = True 
        turns = turns + 1
        if turns == 7:
            print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()