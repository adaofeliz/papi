# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
from config import config

import time
import requests

class CacheFetcher:

    def __init__(self):
        self.cache = {}

    def get(self, fetchurl, max_age=0):

        if self.cache.has_key(fetchurl):
            if int(time.time()) - self.cache[fetchurl][0] < max_age:
                # print 'CACHE', time.time()
                return self.cache[fetchurl][1]

        # Retrieve and cache
        # print 'READ-API', time.time()
        data = requests.get(url= fetchurl)
        self.cache[fetchurl] = (time.time(), data)

        return data

    def get_oauth(self, fetchurl, fetchauth, max_age=0):

        if self.cache.has_key(fetchurl):
            if int(time.time()) - self.cache[fetchurl][0] < max_age:
                # print 'CACHE', time.time()
                return self.cache[fetchurl][1]

        # Retrieve and cache
        # print 'READ-API', time.time()
        data = requests.get(url= fetchurl, auth=fetchauth)
        self.cache[fetchurl] = (time.time(), data)

        return data

# Singleton
fetcher = CacheFetcher()