from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

my_cookie= {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get ('https://www.labirint.ru/')
driver.add_cookie(my_cookie)
driver.refresh()
cookies = driver.get_cookies()
sleep (5)
driver.delete_all_cookies ()
driver.refresh()
sleep (5)
driver.quit ()

