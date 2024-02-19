from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
driver.maximize_window()
driver.get("http://ya.ru/")
sleep(5)
driver.save_screenshot('./test.jpg')
driver.quit