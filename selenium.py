# %%
# Imports
import time
import pyautogui as pyag
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# %%
# Inicia driver
driver = webdriver.Edge()
pega = driver.find_element


'''
print('abriu')
driver.get("https://www.phptravels.com")

element = pega(By.XPATH, '/html/body/header/nav/div/button')
element.click()
time.sleep(0.5)
element = pega(By.XPATH, '//*[@id="mynavbar"]/ul/li[3]/a')
element.click()
time.sleep(5)

'''

# %%
# CT_001
driver.get("https://www.phptravels.com")
element = pega(By.XPATH, '//*[@id="swup"]/div[1]/div/div[1]/div/div[1]/div/div[1]/a')
element.click()
time.sleep(15)

# %%
# CT_002
driver.get("https://www.phptravels.com/demo")
element = pega(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div/input')
element.send_keys("Josefino")
element = pega(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/div/input')
element.send_keys('Almeida')
element = pega(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/input')
element.send_keys('JF Inc.')
element = pega(By.XPATH, '//*[@id="swup"]/section[1]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div[3]/input')
element.send_keys('josefinoBusiness@gmail.com')
numero1 = pega(By.ID, 'numb1')
numero2 = pega(By.ID, 'numb2')
element = pega(By.ID, 'number')
element.send_keys(int(numero1.text)+int(numero2.text))
element = pega(By.ID, 'demo')
element.click()
time.sleep(5)


# %%
# CT_003
driver.get("https://phptravels.org/register.php")
element = pega(By.ID, 'inputFirstName')
element.send_keys('Josefino')
element = pega(By.ID, 'inputLastName')
element.send_keys('Almeida')
element = pega(By.ID, 'inputEmail')
element.send_keys('josefinoBusiness@gmail.com')
'''element = pega(By.XPATH, '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/ul')
time.sleep(1)
element = pega(By.XPATH, '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/ul/li[32]/span[1]')
element.click()'''
element = pega(By.ID, 'inputPhone')
element.send_keys('+5598932323232')
element = pega(By.ID, 'inputAddress1')
element.send_keys('4ª Travessa Tome de Sousa')
element = pega(By.ID, 'inputAddress2')
element.send_keys('625')
element = pega(By.ID, 'inputCountry')
element.click()
element = pega(By.XPATH, '//*[@id="inputCountry"]/option[30]')
element.click()
element = pega(By.ID, 'inputCity')
element.send_keys('Sao Luis')
element = pega(By.ID, 'stateselect')
element.click()
element = pega(By.XPATH, '//*[@id="stateselect"]/option[11]')
element.click()
element = pega(By.ID, 'inputPostcode')
element.send_keys('65037052')
element = pega(By.ID, 'customfield2')
element.send_keys('+5598932222222')
element = pega(By.ID, 'inputNewPassword1')
element.send_keys('SenhaDoJosefino')
element = pega(By.ID, 'inputNewPassword2')
element.send_keys('SenhaDoJosefino')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
pyag.moveTo(450, 490)
pyag.click()
time.sleep(15)
element = pega(By.XPATH, '//*[@id="frmCheckout"]/p/input')
element.click()



# %%
