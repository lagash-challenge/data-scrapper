import pprint
import json
from twitter_scraper import get_tweets

pp = pprint.PrettyPrinter(indent=4)

all_tweets = []

users = ["realDonaldTrump", "barackobama", "usagsessions"]

for user in users:
    for tweet in get_tweets(user, pages=1):
        tweet["user"] = user
        tweet["time"] = tweet["time"].isoformat()
        all_tweets.append(tweet)

print(json.dumps(all_tweets))