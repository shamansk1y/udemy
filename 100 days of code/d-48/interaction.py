from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_driver_path = 'D:\development prog\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://en.wikipedia.org/wiki/Main_Page')
q = driver.find_element('css selector', '#articlecount a')
print(q.text)