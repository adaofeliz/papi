# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time

from common_cachefetcher import fetcher
from requests_oauthlib import OAuth1

CONSUMER_KEY = config['linkedin']['CONSUMER_KEY']
CONSUMER_SECRET = config['linkedin']['CONSUMER_SECRET']

OAUTH_TOKEN = config['linkedin']['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = config['linkedin']['OAUTH_TOKEN_SECRET']

ACCESS_TOKEN = config['linkedin']['ACCESS_TOKEN']

CACHE_TIMEOUT = config['linkedin']['CACHE_TIMEOUT']

def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

def getLinkedinNotifications(delta_days):
		
	response = 0

	try:

		time_after = int(round(time.time() * 1000)) - (delta_days * 86400000)
		r = fetcher.get_oauth("https://api.linkedin.com/v1/people/~/network/updates?scope=self&format=json&oauth2_access_token=%s&after=%d" % (ACCESS_TOKEN, time_after), get_oauth(), CACHE_TIMEOUT)
		linkedin_json = r.json()

		if linkedin_json['_total']:
			response = linkedin_json['_total']

	except Exception, err:
		print Exception, err
		response = -1	

	return {'linkedin': response}