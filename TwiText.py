# coding utf-8

#　ツイートする文章のクラス
class TwiText:
    def __init__(self):
        source1 = '{0}\n{1}頃の{2}は天気は{3}です！\n\n詳細\n'
        source2 = ' 気温：{4}\n'
        source3 = ' 湿度：{5}\n'
        source4 = ' 雲量：{6}\n'
        source5 = ' 風量：{7}\n'
        source6 = ' 気圧：{8}\n'
        source7 = ' ※北緯{9}度, 東経{10}度あたりの情報'

        self.base_srt = source1 + source2 + source3 + source4 + source5 + source6 + source7
        pass

    def Build(self, weatherData):
        str = self.base_srt.format(
            weatherData.date,
            weatherData.time,
            weatherData.city,
            weatherData.weather,
            weatherData.temp,
            weatherData.humidity,
            weatherData.cloud_val,
            weatherData.wind_val,
            weatherData.pressure,
            weatherData.lat,
            weatherData.lon
        )
        return str
