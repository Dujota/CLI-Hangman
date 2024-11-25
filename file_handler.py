import csv
import os


def create_default_word_file():
    """Create words.csv with default words if it doesn't exist."""
    if not os.path.exists("words.csv"):
        default_words = [
            "PYTHON",
            "JAVA",
            "CODING",
            "COMPUTER",
            "PROGRAM",
            "ALGORITHM",
            "DATABASE",
            "NETWORK",
            "SOFTWARE",
            "HARDWARE",
            "INTERNET",
            "KEYBOARD",
            "MONITOR",
            "BROWSER",
            "FUNCTION",
            "VARIABLE",
            "LIBRARY",
            "SYNTAX",
            "DEBUG",
            "COMPILER",
        ]

        with open("words.csv", "w", newline="") as file:
            writer = csv.writer(file)
            for word in default_words:
                writer.writerow([word])
