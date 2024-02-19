from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

driver.maximize_window()
driver.get("http://ya.ru/")
current_title = driver.title
print(current_title)
driver.quit ()