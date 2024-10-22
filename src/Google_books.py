# @author Jenna Rigby
# This class will handle communication with the Google Books API

# import sys
# sys.path.append('../../')
# import config

import requests
from config.Config import API_KEY, BASE_URL

class Google_books:
    def recommend_genre(self, genre):
        url = f"{BASE_URL}?q=subject:{genre}&key={API_KEY}&maxResults=3"

        # Send the get request to retrieve books of that genre using the API and Base URL:
        response = requests.get(url)

        #If the request was successful:
        if response.status_code == 200:
            #Convert items into python format from json:
            data = response.json().get('items', [])
            return [
                f"{book['volumeInfo']['title']} by {', '.join(book['volumeInfo'].get('authors', ['Unknown Author']))}"
                for book in data
            ]
        return ["No books of that genre found."]

    def recommend_author(self, author):
        return "";
