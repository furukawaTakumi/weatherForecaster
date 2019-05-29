import WeatherApiUi as wau
import Twidata
import Twitter
import WeatherDataExtractor as tc
import APIgetDataException as apie
from time import sleep
import WeatherData as wd

seto = ('35.1815', '137.1087')
toyota = ('35.08', '137.15')
owariasahi = ('35.21', '137.03')
miyoshi = ('35.13','137.05')
nissin = ('35.17', '136.96')

twitter = Twitter.Twitter()
twiData = Twidata.Twidata()
weatherApi = wau.WeatherApiUi()
extractor = tc.WeatherDataExtractor()

def beSureToDo(city):
    while(True):
        try:
            data = weatherApi.getDataLatLon(city[0],city[1],1)
            weatherData = extractor.DataSetting(data)
            twitter.twitte( twiData.Create(weatherData) )
        except apie.APIgetDataException:
            sleep(60)
            continue
        break

beSureToDo(seto)
beSureToDo(toyota)
beSureToDo(owariasahi)
beSureToDo(miyoshi)
beSureToDo(nissin)
