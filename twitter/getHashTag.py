import json
import oauth2
import os
import csv
from getTopTrends import *

def getHashTag(tag, intvl="top", type="recent", count=100):
    tag_str = tag[1:]
    url = "https://api.twitter.com/1.1/search/tweets.json?q=%23" + tag_str + "&result_type=" + type + "&count=" + str(count)

    (CONSUMER_KEY, CONSUMER_SECRET, key, secret) = get_keys(intvl)
    content = oauth_req(url, key, secret, CONSUMER_KEY, CONSUMER_SECRET)
    tweets = json.loads(content)
    return tweets

def getHashTags(hashtag_file):
    path = os.path.dirname(__file__)
    hashtag_file = os.path.join(path, hashtag_file)

    with open(hashtag_file) as f:
        content = f.readlines()

    hashtags = [x.strip() for x in content]
    return hashtags


def getAllHashTags(intvl):
    if intvl == "top":
        hashtag_file = "top-hashtags.csv"
    else:
        hashtag_file = "all-hashtags.csv"

    hashtags = getHashTags(hashtag_file)
    tweets = {}
    for hashtag in hashtags:
        tweets[hashtag] = getHashTag(hashtag)

    return tweets

if __name__ == "__main__":
    tweets = getHashTag("#SuperBowlCommercials")
    with open("SuperBowlCommercials.json", 'w') as f:
        json.dump(tweets, f, indent=4, sort_keys=True)