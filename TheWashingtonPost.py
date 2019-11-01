import requests
from bs4 import BeautifulSoup

url = 'https://www.washingtonpost.com/politics/as-trump-reels-democrats-wonder-which-of-their-candidates-can-beat-him/2019/10/19/5c00bbde-f1ef-11e9-89eb-ec56cd414732_story.html'
res = requests.get(url)
res.encoding = 'UTF-8'
soup = BeautifulSoup(res.text, 'html.parser')
#print(soup)
#print(soup.find('span',class_='title'))
print(soup.select('div',class_='article-body')[0].get_text())
