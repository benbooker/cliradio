import api_fetcher

if __name__ == "__main__":
    fetcher = api_fetcher.StationFetcher()
    query = input('Search for radio station : ')
    search_results = fetcher.stations_from_search(query)

    for station in search_results:
        print(station)
