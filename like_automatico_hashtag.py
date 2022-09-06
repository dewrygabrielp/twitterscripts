import tweepy
import time

auth = tweepy.OAuthHandler('','')
auth.set_access_token('','')



api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)


user =  api.me()


search = 'Marketing'
lang = 'es'
nrTweets = 15

for tweet in tweepy.Cursor(api.search,search).items(nrTweets):
    try:

        print('He dado Like')
        tweet.favorite()
        time.sleep(50)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break