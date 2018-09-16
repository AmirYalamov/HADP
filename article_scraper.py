import requests
from newspaper import Article
import csv

# SEARCH FOR POLITICO WEBSITE
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news&'
       'apiKey=e57ae719a0204b648096b52881173731')

response = requests.get(url)

extracted_data = []

print(response.json()['totalResults'])
for article in response.json()['articles']:
    title = article['title']
    url = article['url']

    article = Article(article['url'])
    article.download()
    article.parse()
    article.nlp()

    for word in article.keywords:
        extracted_data.append(("Fox News", title,url, word))

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=cbc-news&'
       'apiKey=e57ae719a0204b648096b52881173731')

response = requests.get(url)

print(response.json()['totalResults'])
for article in response.json()['articles']:
    title = article['title']

    article = Article(article['url'])
    article.download()
    article.parse()
    article.nlp()

    for word in article.keywords:
        extracted_data.append(("CBC News",  title, url,word))

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=cnn&'
       'apiKey=e57ae719a0204b648096b52881173731')

response = requests.get(url)

print(response.json()['totalResults'])
for article in response.json()['articles']:
    title = article['title']

    article = Article(article['url'])
    article.download()
    article.parse()
    article.nlp()

    for word in article.keywords:
        extracted_data.append(("CNN",  title, url,word))

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=fox-news&'
       'apiKey=e57ae719a0204b648096b52881173731')

response = requests.get(url)

print(response.json()['totalResults'])
for article in response.json()['articles']:
    title = article['title']

    article = Article(article['url'])
    article.download()
    article.parse()
    article.nlp()

    for word in article.keywords:
        extracted_data.append(("Fox News",  title, url,word))

url = ('https://newsapi.org/v2/top-headlines?'
       'sources=politico&'
       'apiKey=e57ae719a0204b648096b52881173731')

response = requests.get(url)

print(response.json()['totalResults'])
for article in response.json()['articles']:
    title = article['title']

    article = Article(article['url'])
    article.download()
    article.parse()
    article.nlp()

    for word in article.keywords:
        extracted_data.append(("Politico", title, url,word))

with open('training_data.csv', mode='w', newline='') as training_data:
    data_writer = csv.writer(training_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    data_writer.writerow(['News Organization', 'Article Title', 'URL', 'Keyword', 'Controversial Flag'])
    for entry in extracted_data:
        data_writer.writerow(entry)
