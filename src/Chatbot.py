# @author Jenna Rigby
# Handles the chatbot itself - input and output
from src.Recommendations import Recommendations

class Chatbot:
    def __init__(this):
        Recommendations = Recommendations()

    def begin(this):
        print("Welcome to the book recommendation chatbot! ")

        while True:
            genre = input("What genre of books would you like to read? (enter 'exit' to quit) ")

            if (genre == 'exit' or genre == 'EXIT'):
                print("Thanks for participating! ")
                break

            #Retrieves books from the collection:
            books = this.recommender.get_recommendations(genre)

            print("\nHere are book recommendations of that genre:")
            for book in books:
                print(f"- {book}")




if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.begin()