import json
from time import time
import requests
from flask import Flask, jsonify, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob

'''
@Author : Aman Adhav
@Description : Creating a webhook/api for REST Calls between the android keyboard
@Date : 2018-09-15
'''

class Analysis : 
    
    def __init__(self, text="", image_url = "", video_url = ""):
        self._messages = text
        self._image_address = image_url
        self._video_address = video_url
    
    def sentiment_analysis(self):
        self.analyzed_place_interest = ""
        
        analyser = SentimentIntensityAnalyzer()
        with open("controversial_words.txt") as f:
            controversial_words = [x.lower().strip() for x in f.readlines()]
        
        sentiment_inversion = 1
        sentence = self._messages
        for cwd in controversial_words:
            cwd_blob = TextBlob(cwd)
            if cwd_blob.words[0].singularize() in sentence or cwd_blob.words[0].pluralize() in sentence or cwd_blob.words[0] in sentence:
                sentiment_inversion = -1
                break
        snt = analyser.polarity_scores(sentence)
        return((snt["compound"]*sentiment_inversion))


app = Flask(__name__)
@app.route('/api/message', methods=['POST'])
def message_recieve():
    message_recieved = request.get_json()
    #print(message_recieved["message"])
    required = ['message','image','video'] #defines what are our 3 different platforms
    '''
    if not all(k in message_recieved for k in required):
        return "Missing values", 400    
    '''
    init_analyzer = Analysis(message_recieved["message"],message_recieved["image"],message_recieved["video"])
    response = {'sentiment analysis' : ((str)(init_analyzer.sentiment_analysis())),
                'place interest' : ("Good"),
                }
    return jsonify(response), 200

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int,help='port to listen on')
    args = parser.parse_args()
    port = args.port
    app.run(host="0.0.0.0", port = port)