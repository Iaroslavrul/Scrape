from bs4 import BeautifulSoup
import re
from urllib.request import urlopen


pages = ()


def getLinks(pageUrl):
    global pages
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html)
    for link in bsObj.findAll('a', href=re.compile("^(/wiki/)")):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                # мы получили новую страницу
                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')
