# -*- coding: utf-8 -*-

import json
import datetime
import os
import requests
import sys

from pytz import timezone

# 天気を予想するクラス
class WeatherForecaster:
    def __init__(self, locate='470-0356,JP'):
        self.api_key = 'b78fc959028d96ca6dffa19705903ee6'
        self.api_page = 'http://api.openweathermap.org/data/2.5/forecast?zip={0}&units=metric&lang=ja&APPID={1}'
        self.locate = locate

    # 三時間毎の天気を取得する
    def getWeatherForecast(self):
        # {0},{1}の部分にそれぞれ場所とAPIキーを設定する
        url = self.api_page.format(self.locate, self.api_key)
        req_response = requests.get(url)
        return json.loads(req_response.text)


forecaster = WeatherForecaster()
print(str( forecaster.getWeatherForecast()) )
