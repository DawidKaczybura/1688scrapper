class Offer:
    def __init__(self, companyName, companyLink, offerLink):
        self.companyName = companyName
        self.companyLink = companyLink
        self.offerLink = offerLink
    
    def getRow(self):
        return [self.companyName, self.companyLink, self.offerLink]
