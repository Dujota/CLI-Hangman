def get_hangman_art(tries):
    """
    Get ASCII art for current game state.
    Args:
        tries (int): Number of tries remaining
    Returns:
        str: ASCII image of the hangman
    """
    # Dictionary of hangman states - from 6 tries to 0
    stages = {
        6: """
           --------
           |      |
           |
           |
           |
           |
           -
        """,
        5: """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        4: """
           --------
           |      |
           |      O
           |      |
           |
           |
           -
        """,
        3: """
           --------
           |      |
           |      O
           |     /|
           |
           |
           -
        """,
        2: """
           --------
           |      |
           |      O
           |     /|\\
           |
           |
           -
        """,
        1: """
           --------
           |      |
           |      O
           |     /|\\
           |     /
           |
           -
        """,
        0: """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |
           -
        """,
    }
    return stages[tries]
