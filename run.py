# Get this code from tutorial in https://www.scrapingbee.com/blog/selenium-python/

from selenium import webdriver

DRIVER_PATH = '/home/eraldds/Learning and Self-Project/web_scraping/chromedriver'

link = "https://hasilun.puspendik.kemdikbud.go.id/#2019!smp!capaian!01&01&999!T&T&T&T&1&!3!&"
# Composed link "https://hasilun.puspendik.kemdikbud.go.id/#{tahun}!{jenjang}!capaian!{provinsi}&{kota/kabupaten}&999!T&T&T&T&1&!3!&"

# 1. Aku pengen crawl per tahun, tahun 2015-2019

# 2. Setelah set tahun, set