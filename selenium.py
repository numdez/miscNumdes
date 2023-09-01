import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

print('abriu')
driver.get("https://www.phptravels.com")
print('esperando')
driver.implicitly_wait(7)
print('esperou')

print('procurando')
element = driver.find_element(By.XPATH, '//*[@id="mynavbar"]/ul/li[3]/a')
print('achou')
time.sleep(2)
element.click()
time.sleep(15)