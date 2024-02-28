from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 

driver.get("http://ya.ru/")
element = driver.find_element(By.CSS_SELECTOR, '#text')
element.send_keys("test skypro")
sleep (10)
element.clear ()
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
sleep (10)
driver.quit ()