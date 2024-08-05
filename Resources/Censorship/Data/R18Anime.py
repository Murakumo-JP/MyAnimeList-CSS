from bs4 import BeautifulSoup
import requests
import re
import os

animelist = []
page = 1

file_path = 'R18Anime.css'
if not os.path.exists(file_path):
    open(file_path, 'w').close()

while True:
    request = requests.get(f"https://myanimelist.net/anime/genre/12/Hentai?page={page}")
    soup = BeautifulSoup(request.text, 'html.parser')
    links = soup.find_all("a", class_="link-title")

    if links:
        page += 1
    else:
        break

    for link in links:
        temp = re.sub(r'(?:.*?myanimelist\.net)', '', link.get('href'))
        temp = re.sub(r'\/[^\/]*?$', '', temp)
        animelist.append(f'.data.image a[href^="{temp}/"]:before{{content: var(--R18);}}')

with open(file_path, 'w') as f:
    for index in animelist:
        f.write(index + '\n')

print(animelist)