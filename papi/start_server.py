# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

from flask import Flask
from flask import jsonify

from service_twitter import getTwitterNotifications
from service_facebook import getFacebookNotifications
from service_wordpress import getWordpressNotifications
from service_tumblr import getTumblrNotifications
from service_linkedin import getLinkedinNotifications
from service_meetup import getMeetupNotifications
from service_github import getGithubNotifications
from service_googleplus import getGoogleplusNotifications

app = Flask(__name__)

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

@app.route("/")
def api():
    return jsonify(config["service_description"])

@app.route('/v1_0/<service>', defaults={'days': 1})
@app.route('/v1_0/<service>/<int:days>')
def service_v1_0(service, days):
    return services.get(service, service_v1_0_not_avaiable)(days)

def service_v1_0_not_avaiable():
  return jsonify(error='service_v1_0_not_avaiable')

if __name__ == "__main__":
    app.run(debug=False, threaded=True)