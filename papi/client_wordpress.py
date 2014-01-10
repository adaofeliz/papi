# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time

from common_cachefetcher import fetcher

USER_ID = config['wordpress']['USER_ID']
CACHE_TIMEOUT = config['wordpress']['CACHE_TIMEOUT']

def getWordpressNotifications(delta_days_implement):

	response = 0

	try:

		r = fetcher.get('http://public-api.wordpress.com/rest/v1/sites/%s/posts/?days=%d' % (USER_ID, delta_days_implement), CACHE_TIMEOUT)
		wordpress_json = r.json()

		if wordpress_json['found']:
			response = wordpress_json['found']

	except Exception, err:
		print Exception, err
		response = -1

	return {'wordpress': response}