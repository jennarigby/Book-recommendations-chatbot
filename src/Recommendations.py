# @author Jenna Rigby
# This class handles passing the genre to Google_books to return the requested genre's books

from Google_books import Google_books

class Recommendations:
    def __init__(this):
        #Creates an instance of the Google_books class:
        this.Google_books = Google_books()

    def recommend_genre(this, genre):
        return this.Google_books.recommend_genre(genre)