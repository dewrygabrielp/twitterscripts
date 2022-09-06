import tweepy
from credenciales import credenciales
import time

CONSUMER_KEY = credenciales['consumer_key']
CONSUMER_SECRET = credenciales['consumer_secret']
ACCESS_TOKEN = credenciales['access_token']
ACCESS_TOKEN_SECRET = credenciales['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print("acabo de seguir a ")
    print(follower.screen_name)

    time.sleep(50) 