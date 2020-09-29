import tweepy
from keys import keys
from bro_articles import articles

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


mentions = api.mentions_timeline()

i = 0

def reply_to_tweets():
    for mention in mentions:
        print(mention.text)
        for i in range(151):
            if str(i) in mention.text:
                print(articles[i])
                api.update_status('@' + mention.user.screen_name + " " + articles[i], mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)
 


# for mention in mentions:
    # for mention in reversed(mentions):
    #     if 'code' in mention.full_text.lower():
    #         print('found #helloworld!', flush=True)
    #         print('responding back...', flush=True)
    #         api.update_status('@' + mention.user.screen_name +
    #                 'BrosBeforeHoes', mention.id)