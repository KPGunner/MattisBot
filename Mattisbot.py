import tweepy
from time import sleep

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_SECRET = ''

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

    
