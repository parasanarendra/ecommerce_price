from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)
time.sleep(2)
driver.get("https://rahulshettyacademy.com/loginpagePractise/")