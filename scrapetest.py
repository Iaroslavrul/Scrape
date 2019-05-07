from urllib.request import urlopen
from bs4 import BeautifulSoup
try:
    html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
    # html = urlopen('http://www.feetspace-forum.ru/showthread.php?t=2436')

except HTTPError as e:
    print(e)
    # Возвратить null, прервать или выполнять операции по "Плану Б"

else:
    if html is None:
        print("URL is not found")
    # программа продолжает работу. Примечание: если возвращаите или прерываете в #exception catch, оператор "else" использовать не нужно
    
bs0bj = BeautifulSoup(html) #возвращает обьект BeautifulSoup

nameList = bs0bj.findAll("span", {"class":"green"})
# allhead = bs0bj.findAll({'h1', 'h2'})

# for head in allhead:
#     print(' '.join(head.get_text().split()))
#     print("-----------------------")


for name in nameList:
    print(' '.join(name.get_text().split()))
    print("-----------------------")


# try:
#     badContent = bs0bj.nonExistingTag.anotherTag
# except AttributeError as e:
#     print("TAG is not found")

# else:
#     if badContent == None:
#         print("TAG is not found")
#     else:
#         print(badContent)

# print(bs0bj.findAll("table")[4].findAll('tr')[2].find('td').findAll('div')[1].find('a'))