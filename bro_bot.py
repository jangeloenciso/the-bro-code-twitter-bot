import tweepy
import time
import os
from os import environ
from bro_articles import articles

CONSUMER_KEY = environ[CONSUMER_KEY]
CONSUMER_SECRET = environ[CONSUMER_SECRET]
ACCESS_TOKEN = environ[ACCESS_TOKEN]
ACCESS_TOKEN_SECRET = environ[ACCESS_TOKEN_SECRET]

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


mentions = api.mentions_timeline()

i = 0

def reply_to_tweets():
    for mention in mentions:
        print(mention.text)
        for i in reversed(range(151)):
            if str(i) in mention.text:
                print(articles[i])
                api.update_status('@' + mention.user.screen_name + " " + articles[i], mention.id)
                break

while True:
    reply_to_tweets()
    time.sleep(5)
 

# for mention in mentions:
    # for mention in reversed(mentions):
    #     if 'code' in mention.full_text.lower():
    #         print('found #helloworld!', flush=True)
    #         print('responding back...', flush=True)
    #         api.update_status('@' + mention.user.screen_name +
    #                 'BrosBeforeHoes', mention.id)