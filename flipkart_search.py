import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://www.flipkart.com/")
driver.maximize_window()
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("one plus 12 16gb")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"KzDlHZ").click()
windowsOpened = driver.switch_to.new_window('tab')
driver.get("https://www.ebay.com/")
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("oneplus 12")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(5)
driver.close()
