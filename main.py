import requests
import bs4
import lxml
from time import sleep


## Определяем список ключевых слов:
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
## Вывод результата
def result_value():
    for i in KEYWORDS:
        for j in previews:
            if j.lower().find(i) != -1:
                result = f' <{date}> - <{title}> - <{link}>'
                print(result)
                return

response = requests.get('https://habr.com/ru/articles/')
soup = bs4.BeautifulSoup(response.text, features='lxml')
article_list = soup.find_all('article', class_='tm-articles-list__item')

for article in article_list:
    previews = []
    title = article.find('h2').text.strip()
    previews.append(title)
    preview = article.find(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    sleep(1)
    if preview:
        previews.append(preview.text)
    # print(previews)
    link = f'https://habr.com{article.find('a', class_='tm-title__link')['href']}'
    date = article.find('time')['datetime']

    result_value()





