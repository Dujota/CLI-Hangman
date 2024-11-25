from game import play_game
from file_handler import create_default_word_file


def main():
    """Initialize and start the game."""
    create_default_word_file()
    play_game()


# Start the program
main()
