#!/usr/bin/env python2.7

import tweepy
import time
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
from unidecode import unidecode

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 9600, timeout=5)

consumer_key = "YOUR KEY HERE"
consumer_secret = "YOUR SECRET HERE"
access_key = "YOUR KEY HERE"
access_secret = "YOUR SECRET HERE"

#auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#auth.set_access_token(access_key, access_secret)
#api = tweepy.API(auth)

#new_tweets = tweepy.Cursor(api.search, q='tweetstorm').items(10)

#for tweet in new_tweets:
#    printer.print(tweet.text)
#printer.invertOn()

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
    	tweeted = unidecode(json.loads(data)['text'])	
        #printer.inverseOn()
        #printer.setSize('M')
        #printer.setLineHeight(50)
        printer.feed(2)
        printer.println(tweeted)

        print(tweeted)

        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    stream = Stream(auth, l)
    stream.filter(track=['STRING TO TRACK 1', 'STRING TO TRACK 2'])
