# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time

from pytz import timezone
from dateutil import parser
from datetime import datetime, timedelta

from common_cachefetcher import fetcher
from requests_oauthlib import OAuth1

USER_ID = config['tumblr']['USER_ID']

CONSUMER_KEY = config['tumblr']['CONSUMER_KEY']
CONSUMER_SECRET = config['tumblr']['CONSUMER_SECRET']

OAUTH_TOKEN = config['tumblr']['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = config['tumblr']['OAUTH_TOKEN_SECRET']

CACHE_TIMEOUT = config['tumblr']['CACHE_TIMEOUT']

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def getTumblrNotifications(delta_days):

	response = 0

	try:
		r = fetcher.get_oauth("http://api.tumblr.com/v2/blog/%s/posts?api_key=%s&days%d" % (USER_ID, CONSUMER_KEY, delta_days), get_oauth(), CACHE_TIMEOUT)
		tumblr_json = r.json()
		
		localtz = timezone('UTC')
		one_day_ago = localtz.localize(datetime.now() - timedelta(days = delta_days))

		for item in tumblr_json['response']['posts']:
		    item_datetime = parser.parse(item['date'])
		    if item_datetime > one_day_ago:
	    		response = response + 1

	except:
		response = -1	

	return {'tumblr': response}