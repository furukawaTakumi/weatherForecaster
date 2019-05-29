# coding: utf-8

class WeatherData:
    def __init__(self):
        self.city = "city"
        self.date = "date"
        self.time = "time"
        self.weather = "weather"
        self.temp = "temp"
        self.humidity = "humidity"
        self.cloud_val = "cloud_val"
        self.pressure = "pressure"
        self.rain = "rain_val"
        self.wind = "wind_val"
        self.lon = "longitude"
        self.lat = "latitude"

    def Print(self):
        print("日付　" + self.date)
        print("時間　" + self.time)
        print("天気　" + self.weather)
        print("気温　" + self.temp)
        print("湿度　" + self.humidity)
        print("雲量　" + self.cloud_val)
        print("雨量　" + self.rain_val)
        print("風速　" + self.wind_val)
