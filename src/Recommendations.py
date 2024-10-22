# @author Jenna Rigby
# 
from Google_books import Google_books

class Recommendations:
    def __init__(this):
        this.Google_books = Google_books()

    def recommend_genre(this, genre):
        return this.Google_books.recommend_genre(genre)