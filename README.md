# weatherForecaster
##概要
ラズパイ天気予報！　〜for AIT〜
[AIT周辺にある市の三時間後の天気をTweetするアカウント](あかうんとURL)を作りました。

内部で動作しているプログラムを公開しています。

　天気をツイートする市一覧
 - 豊田市
 - みよし市
 - 瀬戸市
 - 日進市
 - 尾張旭市

## 使用API
 - [OpenWeatherMap](https://openweathermap.org/)
 　三時間後の天気予報を取得するために利用しました。
  
 - [ThingSpeakのThingTweet](https://thingspeak.com/apps)
 　ツイッターで呟くために使用しました。
 
## 運用方法
　ラズパイの`cron`コマンドを利用して定期実行します。
 OpenWeatherMapの情報が更新される時刻(3,6,9,12,15,18,21時)に実行します。
 設定ファイルであるcrontabに記述するのは、
 
 `0 3,6,9,12,15,18,21 0 0 0 python3 /hogehoge/hoge/fuga/Main.py`

です。

## こだわったところ
