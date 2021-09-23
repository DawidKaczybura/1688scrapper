import csv
import os.path
from Links import Links
from ListReader import ListReader
from AllResultSaver import AllResultSaver

class FilesComparer:

    def compare(self):
        listReader = ListReader()
        allLists = []
        finished = False
        counter = 0
        while not finished:
            path = 'pliki/lista' + str(counter+1) + ".csv"
            if os.path.exists(path):
                offers = listReader.read(path)
                allLists.append(offers)
                counter += 1
            else:
                finished = True
        

        allresultSaver = AllResultSaver()
        result = []
        for i in range(len(allLists)-1):
            print("sprawdzam liste: ", i+1)
            companyIndex = 0
            for currentOffer in allLists[i]:
                if currentOffer.checked:
                    break
                counter = 1
                companyInfo = []
                companyInfo.append(allLists[i][companyIndex].companyName)
                companyInfo.append(allLists[i][companyIndex].companyLink)
                companyInfo.append(str(i+1))
                companyInfo.append(allLists[i][companyIndex].offerLink)

                company = allLists[i][companyIndex].companyName
                for j in range(i+1, len(allLists)):
                    found = False
                    for offer in allLists[j]:
                        if company == offer.companyName and not offer.checked:
                            counter += 1
                            found = True
                            offer.checked = True
                            companyInfo.append(str(j+1))
                            companyInfo.append(offer.offerLink)
                    if not found:
                        companyInfo.append("")
                        companyInfo.append("")
                companyInfo.insert(2, str(counter))
                allresultSaver.saveLine(companyInfo)
                companyIndex += 1
                        #print("lol jest", i, " ", j, " ", company, " ", index)