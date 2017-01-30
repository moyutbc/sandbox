#coding: UTF-8
from requests_oauthlib import OAuth1Session
import json
import settings
import re

twitter = OAuth1Session(
		settings.CONSUMER_KEY,
		settings.CONSUMER_SECRET,
		settings.ACCESS_TOKEN,
		settings.ACCESS_TOKEN_SECRET)

params = {}
req = twitter.get("https://api.twitter.com/1.1/statuses/user_timeline.json", params = params)

timeline = json.loads(req.text)


for tweet in timeline:
    created_at = tweet['created_at']
    text = tweet['text']
    if text.find('Runtastic') > -1:
        distance = re.search(r'\d+\.\d+ km', text)
        time     = re.search(r'( ?\d+[h|m|s])+', text)
        print(created_at)
        print('distance: ' + distance.group() + ', time: ' + time.group())

