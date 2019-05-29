# coding: utf-8

import urllib
import urllib.error
import urllib.request
import Twidata

# Twitterクラス
class Twitter:
    def __init__(self):
        self.base_url = 'https://api.thingspeak.com/apps/thingtweet/1/statuses/update/'
        self.key = 'H0ICTWU0EYAU5QJO'

    def twitte(self, contents):
        data = urllib.parse.urlencode({'api_key' : self.key, 'status' : contents}).encode('utf-8')
        response =  urllib.request.urlopen(url=self.base_url, data=data)
