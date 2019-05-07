import requests
from bs4 import BeautifulSoup
import re

pages = set()


def getLinks(pageUrl):
    global pages
    URL = "https://en.wikipedia.org"+pageUrl
    res = requests.get(URL).text
    bsObj = BeautifulSoup(res, 'lxml')
    try:
        print(bsObj.h1.get_text())
        print(bsObj.find(id='mw-content-text').findAll('p')[0])
        print(bsObj.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('На этой странице что-то пропущенно!')

    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # мы получили новую страницу
                newPage = link.attrs['href']
                print('------------\n' + newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')
