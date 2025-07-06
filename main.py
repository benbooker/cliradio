import api_fetcher

if __name__ == "__main__":
    fetcher = api_fetcher.StationFetcher()
    query = input('Search for radio station : ')
    for station in fetcher.fetch_by_name(query):
        print(station)
