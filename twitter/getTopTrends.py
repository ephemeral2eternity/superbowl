import json
import oauth2
import os

def get_keys(typ):
    if typ == "top":
        CONSUMER_KEY='bmtsCiwUTeDyJjMJKx4VZLpxl'
        CONSUMER_SECRET='amkVl80vMuinaIzZNeiLE5OhJyAuDGPzZZBRH1oT3k7cUDYyjZ'
        key = '339823648-t6vj5SnV6Dk9gPKbEjOI3ZodejO1CqhSDUlFY3HY'
        secret = 'vXeXIuhTjwWmlKkZ8esHQiIYfYIJA57u9j72XycJhNHeL'
    else:
        CONSUMER_KEY = 'n2xbXvzZLvsfFQMYC92yPX1tz'
        CONSUMER_SECRET = 'ENJJnzBOxE0UGRdJdaTvKfzGHOZkWhLfd1PBtyYa946IukfkoN'
        key = '827263783546482693-zBPeUzEkfgrcLAF8W0xWEvwCeDL3R4G'
        secret = 'XNbXjwGrEYJNLI6JTUDZi765HEsf0SAVeJKJ0Ft5Cn9A9'

    return (CONSUMER_KEY, CONSUMER_SECRET, key, secret)

def oauth_req(url, key, secret, CONSUMER_KEY, CONSUMER_SECRET,
              http_method="GET", post_body="", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return content

def getTopTrends(woeid, typ):
    url = 'https://api.twitter.com/1.1/trends/place.json?id=' + str(woeid)

    (CONSUMER_KEY, CONSUMER_SECRET, key, secret) = get_keys(typ)
    content = oauth_req(url, key, secret, CONSUMER_KEY, CONSUMER_SECRET)
    top_trends = json.loads(content)
    return top_trends

def getWoeids(woeids_file):
    path = os.path.dirname(__file__)
    woeid_file = os.path.join(path, woeids_file)

    with open(woeid_file, 'r') as f:
        woeids = json.load(f)
        return woeids

def getAllTopTrends(typ):
    if typ == "top":
        woeids_file = "woeid-top.json"
    else:
        woeids_file = "woeid-all.json"

    woeids = getWoeids(woeids_file)
    twitter_trends_all = {}
    rank = 1
    for woeid_obj in woeids:
        twitter_trends_all[rank] = getTopTrends(woeid_obj["woeid"], typ)
        rank += 1

    return twitter_trends_all


if __name__ == "__main__":
    twitter_trends_all = getAllTopTrends("top")
    with open("top-trends.json", 'w') as f:
        json.dump(twitter_trends_all, f, indent=4, sort_keys=True)

    print len(twitter_trends_all.keys())


