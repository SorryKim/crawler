import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&sq=&o=&q=2021%EB%85%84+%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84")
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

images = soup.findAll("img", attrs={"class" : "thumb_img"})


for idx, image in enumerate(images):
    url = image["src"]
    image_res = requests.get(url)
    image_res.raise_for_status()

    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)


