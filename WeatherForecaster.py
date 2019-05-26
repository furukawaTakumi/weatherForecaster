# -*- coding: utf-8 -*-

import json
import requests
import Twidata
import APIgetDataException as apide

# 天気を予想するクラス
class WeatherForecaster:
    def __init__(self, lat='35',lon='137'):
        self.api_key = 'b78fc959028d96ca6dffa19705903ee6'
        self.api_page = 'http://api.openweathermap.org/data/2.5/forecast?lat={0}&lon={1}&APPID={2}&cnt=1'
        self.lat = lat
        self.lon = lon

    # 三時間毎の天気を取得する
    def getJsonData(self):
        # {0},{1}の部分にそれぞれ場所とAPIキーを設定する
        url = self.api_page.format(self.lat, self.lon, self.api_key)
        req_response = requests.get( url )
        res = json.loads(req_response.text)
        if "message" in res and 'Internal error: 500001' == res["message"]:
            raise apide.APIgetDataException("APIサービスが混んでいるようです")
        return res

    def getTwiiteData(self):
        twidata = Twidata.Twidata()
        data = {}
        try:
            data = self.getJsonData()["list"][0]
        except apide.APIgetDataException:
            raise apide.APIgetDataException("APIサービスが混んでいるようです")

        date = data["dt_txt"]
        twidata.date = date.split(" ")[0]

        utc_time = data["dt_txt"].split(" ")[1]
        jp_hour = (int(utc_time.split(":")[0]) + 9) % 24
        hour_formatFunc = lambda x: "0" + str(x) if x < 10 else str(x)
        jp_time = hour_formatFunc(jp_hour) + ":" + utc_time.split(":")[1]
        twidata.time = jp_time

        twidata.weather = self.translate(int(data["weather"][0]["id"]))

        twidata.temp = str( "{:.2f}".format( float(data["main"]["temp"]) - 273.15) ) + "℃"
        twidata.cloud_val = str( data["clouds"]["all"] ) + "％"

        rain_val = 0
        if( "rain" in data and "3h" in data["rain"] ):
            rain_val = data["rain"]["3h"]
            twidata.rain_val = str( data["rain"]["3h"] ) + "mm"
        else:
            twidata.rain_val = str(rain_val) + "mm"
        twidata.wind_val = str(data["wind"]["speed"]) + "m/s"

        return twidata

    def translate(self, weatherID):
        if weatherID // 100 == 2:
            return "雷雨"
        elif weatherID // 100 == 3:
            return "霧雨"
        elif weatherID // 100 == 5:
            return "雨"
        elif weatherID // 100 == 6:
            return "雪"
        elif weatherID // 100 == 7:
            return "特殊気象(霧など)"
        elif weatherID == 100:
            return "晴天"
        elif weatherID // 100 == 8:
            return "曇り"
        else:
            return "不明"