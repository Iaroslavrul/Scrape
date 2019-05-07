from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://pythonscraping.com/pages/page3.html')
    # html = urlopen('http://www.feetspace-forum.ru/showthread.php?t=2436')
# работа с regexp

    
bsObj = BeautifulSoup(html) #возвращает обьект BeautifulSoup

images = bsObj.findAll('img', {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})

for img in images:
    print(img['src'])



# print(bsObj.img['src'])




# tags = bsObj.findAll(lambda tag: len(tag.attrs) == 2)

# for tag in tags:
#     print(tag)
