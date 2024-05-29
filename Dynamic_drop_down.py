import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service()
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)
countires = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countires))

for country in countires:
    if country.text == "India":
        country.click()
        break
# print(driver.find_element(By.ID, "autosuggest").text)
#print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) #when we update the script , we can extract the text values using get attribute
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"


