import requests
import re
from bs4 import BeautifulSoup

url = "https://search.11st.co.kr/Search.tmall?kwd=%25EB%2585%25B8%25ED%258A%25B8%25EB%25B6%2581&fromACK=recent"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

item = soup.find("div", attrs={ "class" : "c_prd_name c_prd_name_row_2"})

print(item.get_attribute_list())
