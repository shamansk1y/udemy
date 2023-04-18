from selenium import webdriver
from selenium.webdriver.chrome.service import Service


chrome_driver_path = 'D:\development prog\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# driver.get('https://www.copa.com.ua/shorty-futbolnye-joma-nobel-100053100.html')
# price = driver.find_element('css selector', '.price').text
# print(price)

driver.get('https://www.python.org/')
event_times = driver.find_elements('css selector', '.event-widget time')
event_names = driver.find_elements('css selector', '.event-widget li a')
events = {}
for n in range(len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text,
    }

print(events)

driver.close()
driver.quit()