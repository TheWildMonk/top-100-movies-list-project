# Import necessary libraries
from bs4 import BeautifulSoup
import requests

# Extracting the webpage
response = requests.get(
    url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()
empire_webpage = response.text

# Creating the soup
soup = BeautifulSoup(empire_webpage, "html.parser")

# List of movie titles with html tags and reverse the list
movie_list = soup.find_all(name="h3", class_="title")
movie_list.reverse()

# Loop through the list and write the movie names in movies.txt file
for title in range(len(movie_list)):
    prefix_removed = str(movie_list[title]).removeprefix('<h3 class="title">')
    movie_title = str(prefix_removed.removesuffix('</h3>'))
    with open(file="movies.txt", mode="a") as movie_file:
        movie_file.write(f"{movie_title}\n")
