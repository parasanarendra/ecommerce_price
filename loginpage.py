import time

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

service_obj = Service()

driver = webdriver.Chrome(service=service_obj)

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")
driver.find_element(By.XPATH,"//button[@id='submit']").click()
print("Login Successfully")
driver.maximize_window()
driver.implicitly_wait(10)
# time.sleep(5)
driver.find_element(By.XPATH,"//a[normalize-space()='Log out']").click()
