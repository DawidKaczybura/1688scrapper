from bs4 import BeautifulSoup
from Offer import Offer
from FileSaver import FileSaver

class SoupSaver:
    companies = []
    offers = []

    def save(self, soup, counter):
        self.offers = []
        self.companies = []

        print("Wydobywanie danych...")

        for offer in soup.find_all('div', class_="normalcommon-offer-card"):
            offerLinkSection = offer.find('div', class_="mojar-element-image")
            offerLink = offerLinkSection.a['href']

            companySection = offer.find('div', class_="company-name")
            companyLink = companySection.a['href']
            companyName = companySection.find('div', class_="company-name").text

            offer = Offer(companyName, companyLink, offerLink)
            self._saveOffer(offer)
            
        fileSaver = FileSaver()
        fileSaver.save(self.offers, counter)

    def _saveOffer(self, offer):
        if not offer.companyName in self.companies:
            self.companies.append(offer.companyName)
            self.offers.append(offer)
        else:
            print("Duplikat sprzedawcy")

    