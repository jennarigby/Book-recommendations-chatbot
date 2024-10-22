# @author Jenna Rigby
# 
from src.Google_books import Google_books

class Recommendations:
    def __init__(self):
        self.Google_books = Google_books

    def recommend_genre(self, genre):
        return self.Google_books.recommend_genre(genre)