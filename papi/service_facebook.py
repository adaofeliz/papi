# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time

from util_cachefetcher import fetcher

ACCESS_TOKEN = config['facebook']['ACCESS_TOKEN']
CACHE_TIMEOUT = config['facebook']['CACHE_TIMEOUT']

def getFacebookNotifications(delta_days_implement):

	try:
		
		response = 0

		r = fetcher.get('https://graph.facebook.com/me/notifications?format=json&suppress_http_code=1&access_token=%s&days=%d' % (ACCESS_TOKEN, delta_days_implement), CACHE_TIMEOUT)
		facebook_json = r.json()

		if facebook_json['summary']:
			response = facebook_json['summary']['unseen_count']

	except:
		response = -1


	return '{ \"facebook_notifications\" : %d }' % (response)