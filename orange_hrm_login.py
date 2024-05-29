import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys('admin123')
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(5)
driver.close()
