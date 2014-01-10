# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

from common_functionexecutor import executor

from client_twitter import getTwitterNotifications
from client_facebook import getFacebookNotifications
from client_wordpress import getWordpressNotifications
from client_tumblr import getTumblrNotifications
from client_linkedin import getLinkedinNotifications
from client_meetup import getMeetupNotifications
from client_github import getGithubNotifications
from client_googleplus import getGoogleplusNotifications

services = {
'facebook': getFacebookNotifications,
 'github': getGithubNotifications,
 'googleplus': getGoogleplusNotifications,
 'linkedin': getLinkedinNotifications,
 'meetup': getMeetupNotifications,
 'tumblr': getTumblrNotifications,
 'twitter': getTwitterNotifications,
 'wordpress': getWordpressNotifications
}

def notifications(service, days):

	functions = []

	if service == '':
		for client_name in list(services.values()):

			function = {
			'target': client_name,
			'args': days
			}

			functions.append(function)
	else:
		function = {
		'target': services.get(service, client_notifications_not_avaiable),
		'args': days
		}

		functions.append(function)

	return executor.execute(functions)

	
def client_notifications_not_avaiable(args):
	return {'error': 'client_notifications_not_avaiable'}







