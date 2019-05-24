
class Twidata:
    def __init__(self, date=None, time=None, weather=None, temp=None,cloud_val=None, rain_val=None, wind_val=None):
        self.date = date
        self.time = time
        self.weather = weather
        self.temp = temp
        self.cloud_val = cloud_val
        self.rain_val = rain_val
        self.wind_val = wind_val

    def Print(self):
        print("日付　" + self.date)
        print("時間　" + self.time)
        print("天気　" + self.weather)
        print("気温　" + self.temp)
        print("雲量　" + self.cloud_val)
        print("雨量　" + self.rain_val)
        print("風速　" + self.wind_val)
