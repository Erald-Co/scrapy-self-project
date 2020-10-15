# Get this code from tutorial in https://www.scrapingbee.com/blog/selenium-python/

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

CHROME_DRIVER_PATH = '/home/eraldds/Learning and Self-Project/web_scraping/chromedriver'

link = "https://hasilun.puspendik.kemdikbud.go.id/#2019!smp!capaian!01&01&999!T&T&T&T&1&!3!&"
# Composed link "https://hasilun.puspendik.kemdikbud.go.id/#{tahun}!{jenjang}!capaian!{provinsi}&{kota/kabupaten}&999!T&T&T&T&1&!3!&"

# TES 1 - CRAWL DARI LINK

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=720*480")

# Create instance
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path=CHROME_DRIVER_PATH)

def download_data(link):
    """ This function will download file from given link. Used to looping"""
    driver.get(link)
    time.sleep(3)
    driver.find_element_by_xpath("//a[@class='btn btn-danger']").click()
    pass

def rename(province_code, city_code):
    os.rename(r'/home/eraldds/Downloads/CAPAIAN NILAI UJIAN NASIONAL SMP TAHUN AJARAN 2018-2019_ .xlsx', r'/home/eraldds/Downloads/{}-{}-smp.xlsx'.format(province_code,city_code))
    pass
    # Name = /home/eraldds/Downloads/CAPAIAN NILAI UJIAN NASIONAL SMP TAHUN AJARAN 2018-2019_ .xlsx
    # os.rename(r'C:\Users\Ron\Desktop\Test\Products.txt',r'C:\Users\Ron\Desktop\Test\Shipped Products.txt')

# Mulai operasi
download_data(link)
time.sleep(10)
rename("01", "01")

