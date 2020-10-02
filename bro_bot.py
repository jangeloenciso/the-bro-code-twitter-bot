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

FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


i = 0


def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(
        last_seen_id,
        tweet_mode='extended')
    for mention in reversed(mentions):
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        for i in reversed(range(151)):
            if str(i) in mention.full_text:
                try:
                    api.update_status(
                        '@' + mention.user.screen_name + " " + articles[i], mention.id)
                    break
                # except tweepy.TweepError:
                #     print("error")


while True:
    reply_to_tweets()
    time.sleep(15)
