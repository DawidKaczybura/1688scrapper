from selenium import webdriver
from bs4 import BeautifulSoup
from SoupSaver import SoupSaver
import time

class SiteRetriver:

    def retrieveData(self, link, settings, counter):
        driver = webdriver.Chrome()
        driver.get(link)

        print("\n\n", link)
        print("Czas czekania: ", settings.waitTime, "s")
        time.sleep(settings.waitTime * 2)
        for i in range(settings.scrollsCount):
            print("Scrollowanie: ", i + 1 ," z ", settings.scrollsCount)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(settings.waitTime)
        
        soup = BeautifulSoup(driver.page_source,'html.parser')
        soupSaver = SoupSaver()
        soupSaver.save(soup, counter)

        driver.close()
        