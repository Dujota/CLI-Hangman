import os


def clear_screen():
    """Clear console screen."""
    os.system("cls" if os.name == "nt" else "clear")


def update_word_display(word, word_display, guess):
    """
    Update display to show correctly guessed letter.
    Args:
        word (str): Target word
        word_display (str): Current display state
        guess (str): Letter guessed
    Returns:
        str: Updated display
    """
    word_display = list(word_display)
    # Loop through the display and find all instanes of the letter that matches the guess
    for i, letter in enumerate(word):
        if letter == guess:
            word_display[i] = guess
    return "".join(word_display)


def check_win_condition(word_display):
    """
    Check if word is completely revealed.
    Args:
        word_display (str): Current display state
    Returns:
        bool: True if won, False otherwise
    """
    # If there is no "blank" letters then the word is compelte
    return "_" not in word_display
