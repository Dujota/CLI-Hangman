from ascii_art import get_hangman_art
from helpers import clear_screen


def display_game_state(tries_remaining, word_display, used_letters):
    """
    Display current game state including hangman, word, and used letters.
    Args:
        tries_remaining (int): Number of attempts left
        word_display (str): Current state of word with revealed letters
        used_letters (set): Set of letters already guessed
    """
    # clear any clutter on the screen for better UX when showing CLI UI
    clear_screen()
    print(get_hangman_art(tries_remaining))
    print(f"\nWord: {' '.join(word_display)}")
    print(f"Used letters: {' '.join(sorted(used_letters))}")
    print(f"Tries remaining: {tries_remaining}")


def display_game_result(game_won, word):
    """
    Display win/lose message.
    Args:
        game_won (bool): Whether player won
        word (str): The target word
    """
    if game_won:
        print("\nCongratulations! You won!")
    else:
        print(f"\nGame Over! The word was: {word}")
