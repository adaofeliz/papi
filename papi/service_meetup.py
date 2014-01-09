# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import requests
import time

from util_cachefetcher import fetcher

KEY = config['meetup']['KEY']
CACHE_TIMEOUT = config['meetup']['CACHE_TIMEOUT']

def getMeetupNotifications(delta_days_implement):

	try:
		
		response = 0

		r = fetcher.get('https://api.meetup.com/dashboard?key=%s&days=%d' % (KEY, delta_days_implement), CACHE_TIMEOUT)
		meetup_json = r.json()

		if meetup_json['stats']:
			response = meetup_json['stats']['upcoming_events']
			
	except:
		response = -1

	return '{ \"meetup_notifications\" : %d }' % (response)