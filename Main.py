import WeatherForecaster as wf
import Twidata as td
import datetime as dt
import Twitter
import APIgetDataException as apie
from time import sleep

contents = 'ラズパイ天気予報\n{0}\n{1}頃のAITは{2}になるでしょう！\n\n詳細\n 気温:{3}\n 雲量:{4}\n 降水量:{5}\n 風:{6}'
forecaster = wf.WeatherForecaster()
twidata = td.Twidata()
twitter = Twitter.Twitter()

while(True):
        try:
            twidata = forecaster.getTwiiteData()
            #twitter.twitte(contents.format(twidata.date, twidata.time, twidata.weather, twidata.temp, twidata.cloud_val, twidata.rain_val, twidata.wind_val))
        except apie.APIgetDataException:
            sleep(60)
            continue
        
        print(contents.format(twidata.date, twidata.time, twidata.weather, twidata.temp, twidata.cloud_val, twidata.rain_val, twidata.wind_val))
        break