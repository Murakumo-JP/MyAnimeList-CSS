from bs4 import BeautifulSoup
import requests
import re

animelist = []
page = 1
while True:
    request = requests.get("https://myanimelist.net/anime/genre/12/Hentai?page=" + str(page))
    soup = BeautifulSoup(request.text, 'html.parser')
    links = soup.find_all("a", class_="link-title")
    
    if(len(links)):
        page += 1
    else:
        break
        
    for link in links:
        temp = re.sub(r'(?:.*?myanimelist\.net)', '', link.get('href'))
        temp = re.sub(r'\/[^\/]*?$', '', temp)
        animelist.append('.data.image a[href^="'+temp+'/"]:before{content: var(--R18);}')

        f = open('R18Anime.css', 'w')
    for index in animelist:
        f.write(index + '\n')
    print(animelist)
f.close()
