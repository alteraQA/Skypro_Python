from time import sleep 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManage

def make_screenshot(browser):
    
    browser.maximize_window()
    browser.get("http://ya.ru/")
    sleep(3)
    browser.save_screenshot('./test.png + driver.name')
    browser.quit()

Edge = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
Firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
Chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

make_screenshot(Chrome)
make_screenshot(Firefox)
make_screenshot (Edge)