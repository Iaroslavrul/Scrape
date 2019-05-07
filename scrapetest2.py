from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
    # html = urlopen('http://www.feetspace-forum.ru/showthread.php?t=2436')

    
bsObj = BeautifulSoup(html) #возвращает обьект BeautifulSoup

for sibling in bsObj.find('table', {'id':'giftList'}).findAll('tr')[1].next_siblings:
    print(sibling)



# for child in bsObj.find('table', {'id':'giftList'}).children:
#     print(child)



# image = bsObj.findAll("tr", {"id":"gift1"})[0].findAll('td')[3].findAll('img')

# imgArr = []
# for i in image:
#     print(i['src'])
#     print("-----------------------")

