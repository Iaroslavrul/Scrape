from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/page3.html')
    # html = urlopen('http://www.feetspace-forum.ru/showthread.php?t=2436')
# работа с родительскими элементами

    
bsObj = BeautifulSoup(html) #возвращает обьект BeautifulSoup

print(bsObj.find('img', {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# for sibling in bsObj.find('table', {'id':'giftList'}).findAll('tr')[1].next_siblings:
#     print(sibling)


