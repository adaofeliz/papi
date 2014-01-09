# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time
import pytz

from pytz import timezone
from dateutil import parser
from datetime import datetime, timedelta

from util_cachefetcher import fetcher

USER_ID = config['googleplus']['USER_ID']
KEY = config['googleplus']['KEY']
CACHE_TIMEOUT = config['googleplus']['CACHE_TIMEOUT']

def getGoogleplusNotifications(delta_days):

	try:
			
		r = fetcher.get('https://www.googleapis.com/plus/v1/people/%s/activities/public?key=%s&days=%d' % (USER_ID, KEY, delta_days), CACHE_TIMEOUT)
		googleplus_json = r.json()

		response = 0
		
		localtz = timezone('UTC')
		one_day_ago = localtz.localize(datetime.now() - timedelta(days = delta_days))

		for item in googleplus_json['items']:
		    item_datetime = parser.parse(item['published'])
		    if item_datetime > one_day_ago:
	    		response = response + 1

	except:
		response = -1

	return '{ \"googleplus_notifications\" : %d }' % (response)