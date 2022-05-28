from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time
options = Options()

# options.headless = True
class Locators():
    # --- Home Page Locators ---
    SEARCH_BTN = (By.XPATH, "//*[@id='main']/div/div[2]/nav/div[1]/ul/li[2]")
    SEARCH_BAR = (By.XPATH, "//*[@id='main']/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    # ARTISTS = (By.XPATH, "//*[@id='searchPage']/div/div/section[2]/div[2]") 
    ARTISTS = (By.XPATH, "//*[@id='searchPage']/div/div/section[2]/div[2]/div/div/div/div[2]") 


class SporifyScrapper():
    def __init__(self):
        CHROME_EXECUTABLE_PATH="/home/prashant/Documents/Projects/Python/chromedriver"    
        self.driver = webdriver.Chrome("chromedriver_linux64/chromedriver", options=options)
        BASE_URL = "https://open.spotify.com/playlist/7tvfjPMPrM1RqNTakcONLt"
        self.driver.get(BASE_URL)

    def get_the_artists(self):
        time.sleep(5)
        all_artists = []
        all_artists = []
        all_artists = []
        all_artists = []
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        spans = soup.find_all("span", {"class": "Type__TypeElement-goli3j-0 hHrtFe rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line"})
        for span in spans:
            for link in span.find_all('a'):
                # if link.text not in all_artists:
                #     all_artists.append({link.text:link['href']})
                # print(any(i for i,d in enumerate(all_artists) if link.text in d.keys()))git fetch --all
                if not any(i for i,d in enumerate(all_artists) if link.text in d.keys()):
                    all_artists.append({link.text:link['href']})

    def get_artist_details(self, all_artists):
        print(all_artists)
        print(all_artists)
        print(all_artists)
        print(all_artists)
        print(all_artists)
        print(all_artists)
        print(all_artists)
        print(all_artists)



obj = SporifyScrapper()
obj.search_song("bhool")
