import socket
import random
import urllib.request
import json 

#TODO: error handling for when an endpoint is down


# TODO: implement some sorta searching by flags?
# cliradio -search --name somaFM --codec MP3

class StationFetcher:

    BASE_URLS = ['https://fi1.api.radio-browser.info', 'https://de1.api.radio-browser.info', 'https://de2.api.radio-browser.info']

    def fetch_json(self):
        endpoint = self.BASE_URLS[0] + '/json/stations'

        req = urllib.request.Request(endpoint)
        req.add_header('User-Agent', 'cliradio/0.0.1')

        data = json.load(urllib.request.urlopen(req))
        print(data)


    def fetch_by_name(self, query):
        endpoint = self.BASE_URLS[0] + '/json/stations/search?name=' + query
        print(endpoint)

        req = urllib.request.Request(endpoint)
        req.add_header('User-Agent', 'cliradio/0.0.1')

        data = json.load(urllib.request.urlopen(req))
        # print(data)
        # print(json.dumps(data, indent = 2))
        
        results = [Station.from_json(item) for item in data]

        return (results)
        




class Station:
    def __init__(self, name, country, url, quality):
        self.name = name
        self.country = country
        self.url = url
        self.quality = quality

    def __repr__(self):
        return(f"{self.name} | {self.country} | {self.quality}")

    @staticmethod
    def from_json(data):
        return Station(
            data.get('name'),
            data.get('country'),
            data.get('url_resolved'),
            f"{str(data.get('bitrate'))} {data.get('codec')}"
        )





