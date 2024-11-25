from display import display_game_state, display_game_result
from word_manager import load_words
from input_handler import get_valid_guess, get_play_again_input
from helpers import update_word_display, check_win_condition
import random


def play_round():
    """
    Execute a single round of Hangman.
    Returns:
        bool: True if player wants to play again, False otherwise
    """
    max_tries = 6
    tries_remaining = max_tries
    used_letters = set()
    word = random.choice(load_words())
    word_display = "_" * len(word)
    game_won = False

    # Main game loop
    while tries_remaining > 0 and not game_won:
        display_game_state(tries_remaining, word_display, used_letters)
        guess = get_valid_guess(used_letters)
        used_letters.add(guess)

        # Check the guess, update display and verify if user won game otherwise reduce tries
        if guess in word:
            word_display = update_word_display(word, word_display, guess)
            game_won = check_win_condition(word_display)
        else:
            tries_remaining -= 1

    # Show final state and get play again choice
    display_game_state(tries_remaining, word_display, used_letters)
    display_game_result(game_won, word)
    return get_play_again_input()


def play_game():
    """Main game loop handling multiple rounds."""
    print("Welcome to Hangman!")
    play_again = True
    while play_again:
        play_again = play_round()
    print("\nThanks for playing!")
