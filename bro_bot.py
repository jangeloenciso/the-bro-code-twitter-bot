import tweepy
import time
import os
from os import environ
from bro_articles import articles

CONSUMER_KEY = "dHeOwB2crnAckGNiBK7GXAPZj"
CONSUMER_SECRET = "IgEEbdmXdSmv3B6WJp0uzQFCLtGAl8YSqIDPiMSw9KQ6pyJ4GF"
ACCESS_TOKEN = "1305620177699004416-PGWvy9q8PRPHJHceBUUs7J6yfISca8"
ACCESS_TOKEN_SECRET = "6xaEkrRT1c1dpRJ5E39xOP8miCt8f24RNi700NmvSbtLF"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


mentions = api.mentions_timeline()

i = 0

def reply_to_tweets():
    for mention in mentions:
        for i in reversed(range(151)):
            if str(i) in mention.text:
                api.update_status('@' + mention.user.screen_name + " " + articles[i], mention.id)
                break

while True:
    print('Running...')
    reply_to_tweets()
    time.sleep(15)
 

# for mention in mentions:
    # for mention in reversed(mentions):
    #     if 'code' in mention.full_text.lower():
    #         print('found #helloworld!', flush=True)
    #         print('responding back...', flush=True)
    #         api.update_status('@' + mention.user.screen_name +
    #                 'BrosBeforeHoes', mention.id)