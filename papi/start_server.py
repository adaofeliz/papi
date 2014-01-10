# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import delegate_social

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def api():
    return jsonify(config["service_description"])

@app.route('/v1_0/notifications/', defaults= {'service': '', 'days': 1})
@app.route('/v1_0/notifications/<service>', defaults= {'days': 1})
@app.route('/v1_0/notifications/<service>/<int:days>')
def v1_0_notifications(service, days):
    return jsonify(notifications=delegate_social.notifications(service, days))

if __name__ == "__main__":
    app.run(debug=True, threaded=True)