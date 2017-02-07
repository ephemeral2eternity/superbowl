from twitter.getTopTrends import *
from twitter.getHashTag import *
import time
import sys

## Get current time in string
cur_time = time.strftime("%Y-%m%d%H%M")

## Read top 25 woeids for region we want to crawl
if len(sys.argv) > 1:
    typ = sys.argv[1]
else:
    typ = "top"

twitter_trends_all = getAllTopTrends(typ)

## Save crawled results
path = os.path.dirname(__file__)
rst_file = os.path.join(path, "twitterData", cur_time + "-" + typ + ".json")

with open(rst_file, 'w') as f:
    json.dump(twitter_trends_all, f, indent=4, sort_keys=True)

if typ == "top":
    hashtagTweets = getAllHashTags(typ)

    ## Save crawled results
    path = os.path.dirname(__file__)
    for hashtag in hashtagTweets.keys():
        hashtag_str = hashtag[1:]
        rst_file = os.path.join(path, "hashtagTweets", hashtag_str + "-" + cur_time + "-" + typ + ".json")

        with open(rst_file, 'w') as f:
            json.dump(hashtagTweets[hashtag], f, indent=4, sort_keys=True)