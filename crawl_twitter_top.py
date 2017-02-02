from twitter.getTopTrends import *
import time

## Get current time in string
cur_time = time.strftime("%Y-%m%d%H%M")

## Read top 25 woeids for region we want to crawl
twitter_trends_all = getAllTopTrends("woeid-top.json")

## Save crawled results
path = os.path.dirname(__file__)
rst_file = os.path.join(path, "twitterData", cur_time + "-top.json")

with open(rst_file, 'w') as f:
    json.dump(twitter_trends_all, f, indent=4, sort_keys=True)