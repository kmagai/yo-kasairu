#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import os

def yo_all(api_token):
    requests.post("http://api.justyo.co/yoall/", data={'api_token': api_token})

def kasairu(api_token):
    location_id = 130010  # 東京
    weather_data = requests.get(
        'http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'
            % location_id).json()

    print weather_data
    
    if any(x in weather_data['forecasts'][0]['telop'] for x in [u'雨', u'雪']):
        print "You definitely need one today!"
        print api_token
        yo_all(api_token)
    else:
        print "you don't need one today"


kasairu_token = os.environ.get('kasairu_token')
print kasairu_token
kasairu(kasairu_token)
