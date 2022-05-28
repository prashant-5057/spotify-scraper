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
        BASE_URL = "https://open.spotify.com"
        self.driver.get(BASE_URL)
    
    def search_song(self, text):
        search_btn = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(Locators.SEARCH_BTN))
        search_btn.click()
        search_bar = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(Locators.SEARCH_BAR))
        search_bar.send_keys(text)
        time.sleep(5) 
        self.get_the_artists(self.driver)

    def get_the_artists(self, driver):
        # all_artists = WebDriverWait(self.driver,10).until(ec.visibility_of_element_located(Locators.ARTISTS))
        all_artists = []
    
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # page = etree.HTML(str(soup))
        # all_artists = page.xpath("//*[@id='searchPage']/div/div/section[2]/div[2]/div/div/div/div[2]")
        # all_artists = soup.find_all('div', attrs={'role': 'row'})
        spans = soup.find_all("span", {"class": "Type__TypeElement-goli3j-0 hHrtFe rq2VQ5mb9SDAFWbBIUIn standalone-ellipsis-one-line"})
        for span in spans:
            for link in span.find_all('a'):
                # print(link.text,"  ",link['href'])
                # print(link.text)
                # if link.text not in all_artists:
                #     all_artists.append({link.text:link['href']})
                # print(any(i for i,d in enumerate(all_artists) if link.text in d.keys()))
                if not any(i for i,d in enumerate(all_artists) if link.text in d.keys()):
                    all_artists.append({link.text:link['href']})

    def get_artist_details(self, all_artists):
        
        
        print(all_artists)


obj = SporifyScrapper()
obj.search_song("bhool")
# obj.get_the_artists()
