import datetime
import WeatherData

# 処理するデータ
#
# {'cod': '200', 'message': 0.0058, 'cnt': 1, 'list': [{'dt': 1559120400, 'main': {'temp': 292.48, 'temp_min': 292.48, 'temp_max': 293.544, 'pressure': 1008.15, 'sea_level': 1008.15, 'grnd_level': 986.86, 'humidity': 32, 'temp_kf': -1.07}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 39}, 'wind': {'speed': 4.51, 'deg': 313.581}, 'sys': {'pod': 'd'}, 'dt_txt': '2019-05-29 09:00:00'}], 'city': {'id': 1852663, 'name': 'Seto', 'coord': {'lat': 35.2333, 'lon': 137.1}, 'country': 'JP', 'population': 134246, 'timezone': 32400}}

class WeatherDataExtractor:
    def __init__(self):
        self.cityDic = {'Seto': '瀬戸市', 'Toyota': '豊田市', 'Nisshin': '日進市', 'owariasahi': '尾張旭市', 'Miyoshi':"みよし市", 'Aichi-ken':'愛知県'}
        self.weatherDic = {'Clear':'晴天', 'Clouds':'曇り', 'Thunderstorm':'雷雨', 'Drizzle':'霧雨', 'Rain':'雨', 'Snow':'雪', 'Mist':'うすい霧', 'Smoke':'煙', 'Haze':'もや', 'Dust':'ほこり','Fog':'霧','Sand':'砂','Dust':'ほこり','Ash':'灰','Squall':'スコール','Tornado':'竜巻',}

    def DataSetting(self, data):
        weatherData = WeatherData.WeatherData()
        weatherData.date = self.getDate()
        weatherData.time = self.getTime()
        weatherData.city = self.getCity( data )
        weatherData.weather = self.getWeather( data )
        weatherData.humidity = self.getHumidity( data )
        weatherData.cloud_val = self.getClouds( data )
        weatherData.temp = self.getTemp( data )
        weatherData.pressure = self.getPressure( data )
        weatherData.lat = self.getLatitude( data )
        weatherData.lon = self.getLongitude( data )
        weatherData.wind_val = self.getWind( data )
        return weatherData

    #　辞書から変更する
    def getCity(self,data):
        city_name = data["city"]["name"]
        return self.cityDic[city_name]

    def getLatitude(self, data):
        return str( data["city"]['coord']['lat'] )

    def getLongitude(self, data):
        return str( data["city"]["coord"]["lon"])

    def getWeather(self, data):
        return self.weatherDic[ str( data["list"][0]['weather'][0]['main'] ) ]

    def getDate(self):
        jp_date = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        )
        jp_date = jp_date+ datetime.timedelta(hours=3)
        return jp_date.strftime("%Y年%m月%d日(%a)")

    def getTime(self):
        jp_time = datetime.datetime.now(
            # utc時間に＋９することで日本時間になり、さらに三時間先の予報なので、12足している
            datetime.timezone(datetime.timedelta(hours=9))
        )
        jp_time = jp_time + datetime.timedelta(hours=3)
        return jp_time.strftime("%H:00")

    def getWind(self, data):
        return str(data['list'][0]["wind"]["speed"]) + "m/s"

    def getClouds(self, data):
        return str( data['list'][0]['clouds']['all'] ) + '%'

    def getHumidity(self, data):
        return str( data['list'][0]['main']['humidity'] ) + '%'

    def getPressure(self, data):
        return str( data['list'][0]['main']['pressure'] ) + 'hPa'

    def getTemp(self, data):
        return '{:.2f}'.format( data['list'][0]['main']['temp'] - 273.15 ) + '℃'
