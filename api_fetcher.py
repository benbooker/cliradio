import requests
from typing import Dict, Any 
import json 

#TODO: error handling for when an endpoint is down


# TODO: implement some sorta searching by flags?
# cliradio -search --name somaFM --codec MP3

class StationFetcher:

    SERVERS = ['https://fi1.api.radio-browser.info', 'https://de1.api.radio-browser.info', 'https://de2.api.radio-browser.info']

    def stations_from_search(self, query: str) -> list["Station"]:
        for server in self.SERVERS:
            try:
                url = server + '/json/stations/search?name=' + query
                response = requests.get(url, headers={'User-Agent':'cliradio/0.0.1'})
                data = response.json()
                print(type(data))
                print(data)
                return [Station.construct_from_json(item) for item in data] 
            except requests.RequestException:
                continue
        print("Unable to reach radio-browser servers.")
        return []




class Station:
    def __init__(self, name: str, country: str, url: str, quality: str) -> None:
        self.name = name
        self.country = country
        self.url = url
        self.quality = quality

    def __str__(self) -> str:
        name = self.name if len(self.name) <= 55 else self.name[:55] + "..."
        return name


    @staticmethod
    def construct_from_json(data: dict[str, Any]) -> "Station" :
        return Station(
            data.get('name', ""),
            data.get('country', ""),
            data.get('url_resolved', ""),
            f"{str(data.get('bitrate', ""))} {data.get('codec', "")}"
        )





