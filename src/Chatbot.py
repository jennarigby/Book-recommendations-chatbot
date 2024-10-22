# @author Jenna Rigby
# Handles the chatbot itself - input and output

import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Recommendations import Recommendations

class Chatbot:
    def __init__(this):
        this.Recommendations = Recommendations()

    def begin(this):
        print("Welcome to the book recommendation chatbot! ")

        while True:
            genre = input("What genre of books would you like to read? (enter 'exit' to quit) ")

            if (genre == 'exit' or genre == 'EXIT'):
                print("Thanks for participating! ")
                break

            #Retrieves books from the collection:
            books = this.Recommendations.recommend_genre(genre)

            print("\nHere are book recommendations of that genre:")
            for book in books:
                print(f"- {book}")




if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.begin()