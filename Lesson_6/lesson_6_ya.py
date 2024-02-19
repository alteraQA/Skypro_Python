from time import sleep 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

def make_screenshot(browser):
    browser.maximize_window()
    browser.get("http://ya.ru/")
    sleep(3)
    browser.save_screenshot('./ya'+browser.name +'.png')
    browser.quit()

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
ff = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

make_screenshot(chrome)
make_screenshot(ff)
