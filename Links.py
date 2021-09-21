import csv

class Links:
    _path = 'pliki/links.csv'

    links = []

    def __init__(self):
        with open(self._path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            for row in csv_reader:
                self.links.append(row)

# links = Links()
# print(links.links)