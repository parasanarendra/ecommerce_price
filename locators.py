from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys("john")
driver.find_element(By.NAME, "email").send_keys("abc@123.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("abcd123")
driver.find_element(By.ID, "exampleCheck1").click()
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "/input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("helloagain") # to select specific path
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()