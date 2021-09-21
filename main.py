from Links import Links
from Settings import Settings
from SiteRetriver import SiteRetriver
from FilesComparer import FilesComparer

def main():
    settings = Settings()
    links = Links()
    menuLoop(links, settings)

def menuLoop(links, settings):
    finished = False
    while not finished:
        print("1 - Pobieranie danych i porównywanie")
        print("2 - Tylko pobieranie")
        print("3 - Tylko porównywanie")
        print("9 - Nic. Koniec na dziś")
        selected = input("Co chcesz zrobić: ")

        if selected == '1':
            processLinks(links, settings)
            processDownloadedData()
        elif selected == '2':
            processLinks(links, settings)
        elif selected == '3':
            processDownloadedData()
        elif selected == '9':
            print("konczymy")
            finished = True
        else:
            print("Wybrana opcja nie pasuje. Wybierz prawidłową opcję")
            


def processDownloadedData():
    filesComparer = FilesComparer()
    filesComparer.compare()

def processLinks(links, settings):
    retriever = SiteRetriver()

    number = 0
    for link in links.links:
        if(link[0] != number):
            number = link[0]
        counter = link[0]
        retriever.retrieveData(link[1], settings, counter)

if __name__ == "__main__":
    main()