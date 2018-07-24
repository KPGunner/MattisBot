import tweepy
from time import sleep

CONSUMER_KEY = 'XNmbY7rCqxnschmjBTZ9aRwzw'
CONSUMER_SECRET = 'Nv7jFprDe5way8cUkzsu1Z24Hj8mYaus4rBiKsB5QsD63xL02K'
ACCESS_TOKEN = '1013506057459597312-gYYJE7kCzkaHEFke7FXe2RZlyRyHtN'
ACCESS_SECRET = 'SLgDCDbQ7ViQa54UpJg5D7ymjf5OKWoTrMF1qnABZ1aXk'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)

file=open('mattis1.txt', 'r')
f=file.readlines()
file.close()

for line in f:
    try:
        print(line)
        if line != '\n':
            api.update_status(line)
            print('Success')
            for follower in tweepy.Cursor(api.followers).items():
                follower.follow()
                print('Followed ')
            sleep(21600)
        else:
            pass
    except tweepy.TweepError as e:
        print(e.reason)
        sleep(21600)

print('Script Complete')

    
