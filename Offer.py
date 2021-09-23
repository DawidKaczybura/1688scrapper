class Offer:
    def __init__(self, companyName, companyLink, offerLink):
        self.companyName = companyName
        self.companyLink = companyLink
        self.offerLink = offerLink
        self.checked = False
    
    def getRow(self):
        return [self.companyName, self.companyLink, self.offerLink]
