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




if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.begin()