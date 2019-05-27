import WeatherForecaster as wf
import Twidata as td
import datetime as dt
import Twitter
import APIgetDataException as apie
from time import sleep

def createContent(twidata):
    contentLine1 = 'ラズパイ天気予報 ~{0}~\n'
    contentLine2 = '{1}頃のAITは{2}になるでしょう！\n\n'

    contentLine3 = '詳細\n'
    contentLine4 = '　気温:{3}\n'
    cnt = 4
    contentLine5 = ""
    if twidata.weather == "曇り":
        contentLine5 = '　雲量:{4}\n'
        cnt = cnt + 1
    
    contentLine6 = '　降水量:{' + str(cnt) + '}\n'
    cnt = cnt + 1
    contentLine7 = '　風:{' + str(cnt) + '}'
    if cnt == 6:
        return ( contentLine1 + contentLine2 + contentLine3 + contentLine4 + contentLine5 + contentLine6 + contentLine7).format(
            twidata.date, twidata.time, twidata.weather, twidata.temp, twidata.cloud_val, twidata.rain_val, twidata.wind_val
        )
    else:
        return ( contentLine1 + contentLine2 + contentLine3 + contentLine4 + contentLine6 + contentLine7).format(
            twidata.date, twidata.time, twidata.weather, twidata.temp, twidata.rain_val, twidata.wind_val
        )

forecaster = wf.WeatherForecaster()
twidata = td.Twidata()
twitter = Twitter.Twitter()

while(True):
    try:
        twidata = forecaster.getTwiiteData()
        #twitter.twitte(createContent(twidata))
    except apie.APIgetDataException:
        sleep(60)
        continue
    print(createContent(twidata))
    break