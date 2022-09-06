import tweepy
from credenciales import credenciales
import time

SCREEN_NAME = credenciales['screen_name']
CONSUMER_KEY = credenciales['consumer_key']
CONSUMER_SECRET = credenciales['consumer_secret']
ACCESS_TOKEN = credenciales['access_token']
ACCESS_TOKEN_SECRET = credenciales['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

for f in friends:
    if f not in followers:
        api.destroy_friendship(f)
        print("He dejado de seguir a {0}".format(api.get_user(f).screen_name))
        time.sleep(50)
Dejar
de
seguir
a
quien
no
te
sigue
sin
pregunta
import tweepy
from credenciales import credenciales
import time

SCREEN_NAME = credenciales['screen_name']
CONSUMER_KEY = credenciales['consumer_key']
CONSUMER_SECRET = credenciales['consumer_secret']
ACCESS_TOKEN = credenciales['access_token']
ACCESS_TOKEN_SECRET = credenciales['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

followers = api.followers_ids(SCREEN_NAME)
friends = api.friends_ids(SCREEN_NAME)

for f in friends:
    if f not in followers:
        api.destroy_friendship(f)
        print("He dejado de seguir a {0}".format(api.get_user(f).screen_name))
        time.sleep(50)

Seguir
a
quien
te
sigue
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