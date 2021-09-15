import csv

class Settings:
    _path = 'pliki/settings.csv'
    _waitTimeString = "czas_czekania"
    _scrollsCountString = "ilosc_scrolli"
    _defaultWaitTime = 5
    _defaultScrollsCount = 3

    waitTime = _defaultWaitTime
    scrollsCount = _defaultScrollsCount

    def __init__(self):

        with open(self._path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            for row in csv_reader:
                if row[0] == self._waitTimeString:
                    self.waitTime = int(row[1])
                elif row[0] == self._scrollsCountString:
                    self.scrollsCount = int(row[1])

# settings = Settings()
# print(settings.waitTime)
# print(settings.scrollsCount)