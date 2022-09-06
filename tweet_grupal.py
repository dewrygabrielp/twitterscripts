import tweepy, sys, time
from random import randint
from credenciales import credenciales

CONSUMER_KEY = credenciales['consumer_key']
CONSUMER_SECRET = credenciales['consumer_secret']
ACCESS_TOKEN = credenciales['access_token']
ACCESS_TOKEN_SECRET = credenciales['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

usuarios = sys.argv[1]
f = open(usuarios, "r")
h = f.readlines()
f.close()

for i in h:
    i = i.rstrip()
    m = i + " " + sys.argv[2]
    s = api.update_status(m)
    nap = randint(1, 60)
    time.sleep(nap)