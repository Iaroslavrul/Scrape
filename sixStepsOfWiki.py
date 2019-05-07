import requests
from bs4 import BeautifulSoup
import re
import datetime
import random
# from urllib.request import urlopen

# html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)

random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    URL = "https://en.wikipedia.org"+articleUrl
    res = requests.get(URL).text
    bsObj = BeautifulSoup(res, 'lxml')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)