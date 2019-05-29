# -*- coding: utf-8 -*-

import json
import requests
import Twidata
import APIgetDataException as apide
import datetime

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

        print(data)

        date = data["dt_txt"]
        twidata.date = self.__getForecastDate()
        twidata.time = self.__getForecastTime()
        twidata.weather = self.__weatherTranslator( data["weather"][0]["id"] )
        twidata.temp = str( "{:.2f}".format( float(data["main"]["temp"]) - 273.15) ) + "℃"

        if twidata.weather == "曇り":
            twidata.cloud_val = self.__cloudsTranslator( data["weather"][0]["id"] )

        rain_val = 0
        if( "rain" in data and "3h" in data["rain"] ):
            rain_val = data["rain"]["3h"]
            twidata.rain_val = str( data["rain"]["3h"] ) + "mm"
        else:
            twidata.rain_val = str(rain_val) + "mm"
        twidata.wind_val = str(data["wind"]["speed"]) + "m/s"

        return twidata

    def __getForecastDate(self):
        jp_date = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=12))
        )
        return jp_date.strftime("%Y年%m月%d日(%a)")

    def __getForecastTime(self):
        jp_time = datetime.datetime.now(
            # utc時間に＋９することで日本時間になり、さらに三時間先の予報なので、12足している
            datetime.timezone(datetime.timedelta(hours=12))
        )
        return jp_time.strftime("%H:00")

    def __weatherTranslator(self, weatherID):
        num = weatherID // 100
        if num == 2:
            return "雷雨"
        elif weatherID // 100 == 3:
            return "霧雨"
        elif weatherID // 100 == 5:
            return "雨"
        elif weatherID // 100 == 6:
            return "雪"
        elif weatherID // 100 == 7:
            return "特殊気象(霧など)"
        elif weatherID == 800:
            return "晴天"
        elif weatherID // 100 == 8:
            return "曇り"

    def __cloudsTranslator(self, weatherID):
        if weatherID == 801:
            return "11-25%"
        if weatherID == 802:
            return "26-50%"
        if weatherID == 803:
            return "51-84%"
        if weatherID == 804:
            return "85-100%"
