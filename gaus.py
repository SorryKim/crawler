import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=799793"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("span", attrs={ "class" : "EpisodeListList__title--lfIzU"})

title = cartoons[0]
print(title.get_text())