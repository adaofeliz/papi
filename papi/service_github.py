# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time
import pytz

from pytz import timezone
from dateutil import parser
from datetime import datetime, timedelta

from util_cachefetcher import fetcher

USER_ID = config['github']['USER_ID']
CACHE_TIMEOUT = config['github']['CACHE_TIMEOUT']

def getGithubNotifications(delta_days):

	try:
		
		response = 0

		r = fetcher.get('https://api.github.com/users/%s/events/public?days=%d' % (USER_ID, delta_days), CACHE_TIMEOUT)
		github_json = r.json()

		localtz = timezone('UTC')
		one_day_ago = localtz.localize(datetime.now() - timedelta(days = delta_days))
		for activity in github_json:
		    activity_datetime = parser.parse(activity['created_at'])
		    if activity_datetime > one_day_ago:
		    	response = response + 1

	except:
		response = -1


	return '{ \"github_notifications\" : %d }' % (response)