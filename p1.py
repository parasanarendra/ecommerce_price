from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
radio_button = driver.find_elements(By.CSS_SELECTOR,".radioButton")
radio_button[1].click()
assert radio_button[1].is_selected()
