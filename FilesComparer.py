import csv
import os.path
from Links import Links
from ListReader import ListReader
from AllResultSaver import AllResultSaver

class FilesComparer:

    def compare(self):
        listReader = ListReader()
        allLists = []
        allCompanyNames = []
        finished = False
        counter = 0
        while not finished:
            path = 'pliki/lista' + str(counter+1) + ".csv"
            if os.path.exists(path):
                offers, companyNames = listReader.read(path)
                allLists.append(offers)
                allCompanyNames.append(companyNames)
                counter += 1
            else:
                finished = True
        

        allresultSaver = AllResultSaver()
        result = []
        constAllCompanyNames = allCompanyNames[:]
        for i in range(len(allCompanyNames)-1):
            print("sprawdzam liste: ", i+1)
            companyIndex = 0
            for company in allCompanyNames[i]:
                counter = 1
                companyInfo = []
                companyInfo.append(company)
                companyInfo.append(allLists[i][companyIndex].companyLink)
                companyInfo.append(str(i))
                companyInfo.append(allLists[i][companyIndex].offerLink)
                for j in range(i+1, len(allCompanyNames)):
                    if company in allCompanyNames[j]:
                        counter += 1
                        index = constAllCompanyNames[j].index(company)
                        allCompanyNames[j].remove(company)
                        companyInfo.append(str(j+1))
                        companyInfo.append(allLists[j][index].offerLink)
                companyInfo.insert(2, str(counter))
                allresultSaver.saveLine(companyInfo)
                companyIndex += 1
                        #print("lol jest", i, " ", j, " ", company, " ", index)