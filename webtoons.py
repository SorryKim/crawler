import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

webtoons = soup.find_all("span", attrs={ "class" : "text"})

print(soup)

#for webtoon in webtoons:
    #print(webtoon.get_text())


#print(soup.find("title").get_text())
