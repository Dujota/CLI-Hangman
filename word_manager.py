import csv


def load_words(filename="words.csv"):
    """
    Load words from CSV file or return defaults.
    Args:
        filename (str): Path to words file
    Returns:
        list: List of words in uppercase
    """
    try:
        # Attempt to open the file and create list from the data set, formatted properly
        with open(filename) as file:
            word_list = list(csv.reader(file))
            return [word[0].strip().upper() for word in word_list]
    except FileNotFoundError:
        # Have a fallback so that the program doesn't crash
        print("Warning: words.csv not found. Using default word list.")
        return ["PYTHON", "JAVA", "CODING", "COMPUTER", "PROGRAM"]
