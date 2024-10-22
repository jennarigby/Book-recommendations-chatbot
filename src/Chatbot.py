# @author Jenna Rigby
# Handles the chatbot itself - input and output, and calling methods

from Recommendations import Recommendations

class Chatbot:
    def __init__(this):
        #Creates an instance of the Recommendations class: 
        this.Recommendations = Recommendations()

    def begin(this):
        print("Welcome to the book recommendation chatbot! ")

        while True:
            genre = input("What genre of books would you like to read? (enter 'exit' to quit) ")

            if (genre == 'exit' or genre == 'EXIT'):
                print("Thanks for participating! ")
                break

            #Retrieves books from the API:
            books = this.Recommendations.recommend_genre(genre)

            print("\nHere are book recommendations of that genre:")
            if not books:
                print("Genre does not exist. Please try again")
            else:
                for book in books:
                    print(f"- {book}")
            print("\n")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.begin()