# -*- coding: utf-8 -*-

import json
import datetime
import os
import requests
import sys

from pytz import timezone

# 天気を予想するクラス
class WeatherForecaster:
    def __init__(self, lat='35',lon='137'):
        self.api_key = 'b78fc959028d96ca6dffa19705903ee6'
        self.api_page = 'http://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&APPID={2}'
        self.lat = lat
        self.lon = lon

    # 三時間毎の天気を取得する
    def getJsonData(self):
        # {0},{1}の部分にそれぞれ場所とAPIキーを設定する
        url = self.api_page.format(self.lat, self.lon, self.api_key)
        print(url)
        req_response = requests.get(url)
        return json.loads(req_response.text)

    def getCityData(self):
        return self.getJsonData()["city"]

    def getDataList(self):
        return self.getJsonData()["list"]


forecaster = WeatherForecaster()
print(str( forecaster.getJsonData()) )
