import csv
from os import dup
import os.path
from Offer import Offer
from FileSaver import FileSaver

class ListSingler:

    def makeSingle(self, counter):
        path = 'pliki/lista' + str(counter) + ".csv"
        if os.path.exists(path):
            offers = self._readData(path)
            self._saveData(counter, offers)
        else:
            print("plik: " + path + " nie istnieje")
        
    def _saveData(self, counter, offers):
        print("zapisywanie do pliku.. \n")
        saver = FileSaver()
        saver.reset(counter)
        saver.save(offers, counter)

    def _readData(self, path):
        print("usuwanie duplikatów...")
        with open(path, encoding='UTF8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            offers = []
            companies = []
            duplicates = 0
            for row in csv_reader:
                if row[0] not in companies:
                    companies.append(row[0])
                    offer = Offer(row[0], row[1], row[2])
                    offers.append(offer)
                else:
                    duplicates += 1
            print("Usunięto " + str(duplicates) + " duplikatów")
            return offers