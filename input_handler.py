def get_valid_guess(used_letters):
    """
    Get and validate letter guess from user.
    Args:
        used_letters (set): Previously guessed letters
    Returns:
        str: Valid single letter guess
    """
    while True:
        # Make sure that the input from the user is only a valid letter or not a duplicate
        guess = input("\nEnter a letter: ").strip().upper()
        if not guess:
            print("Please enter a letter.")
        elif len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a letter from A-Z.")
        elif guess in used_letters:
            print("You already guessed that letter.")
        else:
            return guess


def get_play_again_input():
    """
    Ask if player wants another game.
    Returns:
        bool: True for yes, False for no
    """
    while True:
        # After game is over allow user to make a choice to quit or play again
        play_again = input("\nWould you like to play again? (y/n): ").lower()
        if play_again in ["y", "n"]:
            return play_again == "y"
        print("Please enter 'y' or 'n'.")
