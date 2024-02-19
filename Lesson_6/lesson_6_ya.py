from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager

webdriver_service = service.Service(OperaDriverManager().install())
webdriver_service.start()

driver = webdriver.Remote(webdriver_service.service_url, webdriver.DesiredCapabilities.OPERA)

##driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

##driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

driver.maximize_window()
driver.get("http://ya.ru/")
driver.save_screenshot('./test.png')
driver.quit()