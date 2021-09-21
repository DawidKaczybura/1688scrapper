import csv
from Offer import Offer

class ListReader:

    def read(self, path):
        with open(path, encoding='UTF8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')

            allOffers = []
            companyNames = []
            counter = 0
            for row in csv_reader:
                #if not counter == 0:
                offer = Offer(row[0], row[1], row[2])
                allOffers.append(offer)
                companyNames.append(row[0])
                counter += 1

            return allOffers, companyNames