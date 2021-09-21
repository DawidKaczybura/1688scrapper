import csv

class FileSaver:
    separator = ';'

    def save(self, offers, counter):
        path = 'pliki/lista' + str(counter) + ".csv"
        f = open(path, 'a+', newline='', encoding='UTF8')
        writer = csv.writer(f, delimiter=';')
        #row = ['COMPANY NAME', 'COMPANY LINK', 'OFFER LINK']
        #writer.writerow(row)

        for offer in offers:
            writer.writerow(offer.getRow())
        
        f.close()
