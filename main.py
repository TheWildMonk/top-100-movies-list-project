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
movie_title_list = [title.getText() for title in movie_list]

# Reversing the list of the movies
titles = movie_title_list[::-1]

# Write the movie names in movies.txt
with open(file="movies.txt", mode="w") as movies:
    for each_title in titles:
        movies.write(f"{each_title}\n")
