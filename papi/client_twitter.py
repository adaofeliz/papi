# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time
import pytz

from common_cachefetcher import fetcher
from dateutil import parser
from datetime import datetime, timedelta
from requests_oauthlib import OAuth1
from pytz import timezone

CONSUMER_KEY = config['twitter']['CONSUMER_KEY']
CONSUMER_SECRET = config['twitter']['CONSUMER_SECRET']

OAUTH_TOKEN = config['twitter']['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = config['twitter']['OAUTH_TOKEN_SECRET']

CACHE_TIMEOUT = config['twitter']['CACHE_TIMEOUT']

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def getTwitterNotifications(delta_days):

	response = 0
		
	try:
		r = fetcher.get_oauth("https://api.twitter.com/1.1/statuses/user_timeline.json?include_rts=1&exclude_replies=true&contributor_details=false&trim_user=true&days%d" % (delta_days), get_oauth(), CACHE_TIMEOUT)
		tweets = r.json()

		localtz = timezone('UTC')
		one_day_ago = localtz.localize(datetime.now() - timedelta(days = delta_days))
		for tweet in tweets:
		    tweeted_datetime = parser.parse(tweet['created_at'])
		    if tweeted_datetime > one_day_ago:
		        response = response + 1

	except:
		response = -1

	return {'twitter': response}