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
    #twitter.twitte(contents.format(twidata.date, twidata.time, twidata.weather, twidata.temp, twidata.cloud_val, twidata.rain_val, twidata.wind_val))

get_start = False
while(True):
    time_temp = dt.datetime.now()
    print(time_temp.strftime('%H'))
    if int(time_temp.strftime('%H')) % 3 == 0 and int(time_temp.strftime('%M')) == 0:
        get_start = True
        
    if get_start:
        try:
            routine_work()
            get_start = False
            sleep(3600*2)
        except APIgetDataException(e):
            sleep(60)
            continue
    else:
        sleep(240)