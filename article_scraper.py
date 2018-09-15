import requests
from newspaper import Article

# SEARCH FOR POLITICS
# url = ('https://newsapi.org/v2/everything?'
#        'q=politics&from=2018-09-14&to=2018-09-14&sortBy=popularity&'
#        'apiKey=e57ae719a0204b648096b52881173731')

# SEARCH FOR POLITICO WEBSITE
url = ('https://newsapi.org/v2/top-headlines?'
       'sources=politico&'
       'apiKey=e57ae719a0204b648096b52881173731')


response = requests.get(url)

for article in response.json()['articles']:
    print(article['title'])

    article = Article(article['url'])
    article.download()
    article.parse()
    article.nlp()

    print(article.keywords)
