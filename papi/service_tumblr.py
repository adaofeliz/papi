# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time

from util_cachefetcher import fetcher
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

def getTumblrNotifications(delta_days_implement):

	try:
		r = fetcher.get_oauth("http://api.tumblr.com/v2/blog/%s/posts?api_key=%s&days%d" % (USER_ID, CONSUMER_KEY, delta_days_implement), get_oauth(), CACHE_TIMEOUT)
		tumblr_json = r.json()

		response = 0
		if tumblr_json['response']:
			response = tumblr_json['response']['total_posts']

	except:
		response = -1	

	return '{ \"tumblr_notifications\" : %d }' % (response)