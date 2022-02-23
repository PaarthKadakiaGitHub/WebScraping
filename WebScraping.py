import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.imdb.com/chart/top')
sourcecode = BeautifulSoup(webpage.content, 'html.parser')
listofmovies = sourcecode.select("td.titleColumn a")
for anchor in listofmovies:
    print(anchor.text)  # Display the innerText of each anchor
