import WeatherForecaster as wf
import Twidata as td
import datetime as dt
import Twitter
import APIgetDataException
from time import sleep

contents = '{0}\n{1}頃のAITは{2}になるでしょう！\n\n詳細\n 気温:{3}\n 雲量:{4}\n 降水量:{5}\n 風:{6}'
forecaster = wf.WeatherForecaster()
twidata = td.Twidata()
twitter = Twitter.Twitter()

def routine_work():
    twidata = forecaster.getTwitteData()
    twitter.twitte(contents.format(twidata.date, twidata.time, twidata.weather, twidata.temp, twidata.cloud_val, twidata.rain_val, twidata.wind_val))

while(True):
        try:
            routine_work()
        except APIgetDataException(e):
            sleep(60)
            continue
        
    break