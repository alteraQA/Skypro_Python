from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 



driver.get("http://ya.ru/")
driver.maximize_window()
driver.set_window_size(1024, 768)
sleep(5)