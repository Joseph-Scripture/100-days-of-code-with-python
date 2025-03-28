from bs4 import BeautifulSoup
import requests
response = requests.get('https://www.empireonline.com/movies/features/best-movies-2/')
empire_movie = response.text


soup = BeautifulSoup(empire_movie, 'html.parser')

all_movies = soup.find_all(name='h2')
movies_title = [movie.getText() for movie in all_movies]
movies = movies_title[::-1]


with open('day44/movies.txt', 'a') as folder:
    
    for movie in movies:
        folder.write(f"{movie}\n")

    # folder.write(title)
    
