import csv

class AllResultSaver:
    _path = 'pliki/cala_lista.csv'
    _f = None
    writer = None

    def __init__(self):
        self._f = open(self._path, 'w', newline='', encoding='UTF8')
        self.writer = csv.writer(self._f, delimiter=';')

        row = ['COMPANY NAME', 'COMPANY LINK', 'TOTAL OFFERS','LIST NUMBER', 'OFFER LINK','LIST NUMBER', 'OFFER LINK','LIST NUMBER', 'OFFER LINK','LIST NUMBER', 'OFFER LINK','LIST NUMBER', 'OFFER LINK','LIST NUMBER', 'OFFER LINK','LIST NUMBER', 'OFFER LINK']
        self.writer.writerow(row)

    def saveLine(self, line):
        self.writer.writerow(line)

    def __del__(self):
        self._f.close()