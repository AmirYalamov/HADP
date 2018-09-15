from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

analyser = SentimentIntensityAnalyzer()
with open("controversial_words.txt") as f:
    controversial_words = [x.lower().strip() for x in f.readlines()]

sentiment_inversion = 1
sentence = "i hate adolf hitler"
for cwd in controversial_words:
    cwd_blob = TextBlob(cwd)
    if cwd_blob.words[0].singularize() in sentence or cwd_blob.words[0].pluralize() in sentence or cwd_blob.words[0] in sentence:
        sentiment_inversion = -1
        break
snt = analyser.polarity_scores(sentence)
print(snt["compound"]*sentiment_inversion)

# from textblob import TextBlob
# from nltk.tag import pos_tag
#
# tweet = "I fucking hate Hitler and Nazis"
# tagged_tweet = pos_tag(tweet.split())
# propernouns = [word for word,pos in tagged_tweet if pos == 'NNP']
#
# tweet_analysis = TextBlob(tweet)
# words = tweet_analysis.words
# for word in words:
#     word_analysis = TextBlob(word)
#     print(word)
#     print(word_analysis.sentiment)
# print(tweet_analysis.sentiment)
# print(propernouns)
