import WeatherForecaster as wf
import Twidata as td

forecaster = wf.WeatherForecaster()
twidata = td.Twidata()

twidata = forecaster.getTwiiteData()
twidata.Print()
