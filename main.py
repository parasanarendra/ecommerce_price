from selenium import webdriver
from selenium.webdriver.chrome.service import Service
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://www.gmail.com/")
print(driver.title)
print(driver.current_url)
driver.get("https://www.linkedin.com/feed/")
driver.back()
driver.refresh()
driver.forward()
driver.minimize_window()
driver.close()

