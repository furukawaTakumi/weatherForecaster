# coding: utf-8

import json
import requests
import Twidata
import APIgetDataException as apide

class WeatherApiUi:
    def __init__(self):
        self.api_key = 'b78fc959028d96ca6dffa19705903ee6'
        self.baseUrl = 'http://api.openweathermap.org/data/2.5/forecast?&APPID={0}'

    def getDataLatLon(self, lat, lon, cnt=0):
        api_page = self.baseUrl + '&lat={1}&lon={2}'
        if 0 < cnt and cnt <= 30:
            api_page = api_page + '&cnt=' + str( cnt )
        url = api_page.format(self.api_key, lat, lon)
        req_response = requests.get( url )
        res = json.loads(req_response.text)
        if "message" in res and 'Internal error: 500001' == res["message"]:
            raise apide.APIgetDataException("APIサービスが混んでいるようです")
        return res

    def getDataZip(self, zip, cnt=0):
        api_page = self.baseUrl + '&zip={1}'
        if 0 < cnt and cnt <= 30:
            api_page = api_page + '&cnt=' + str( cnt )
        url = api_page.format(self.api_key,zip)
        req_response = requests.get( url )
        res = json.loads(req_response.text)
        if "message" in res and 'Internal error: 500001' == res["message"]:
            raise apide.APIgetDataException("APIサービスが混んでいるようです")
        return res
