# %%
# Imports
import time
import random
import pyautogui as pyag
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
def _waitForAlert(driver):
    return WebDriverWait(driver, 5).until(EC.alert_is_present())

# %%
# Inicia driver
driver = webdriver.Edge()
pega = driver.find_element


'''


'''

# %%
# CT_001 Acessa demo
driver.get("https://www.phptravels.com")
element = pega(By.XPATH, '//*[@id="swup"]/div[1]/div/div[1]/div/div[1]/div/div[1]/a')
element.click()

# %%
# CT_002 Preenche demo
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


# %%
# CT_003 Não pode ser automatizado pois é fora do site


# %%
# CT_004 Não pode ser automatizado devido à captcha
'''driver.get("https://phptravels.org/register.php")
element = pega(By.ID, 'inputFirstName')
element.send_keys('Josefino')
element = pega(By.ID, 'inputLastName')
element.send_keys('Almeida')
element = pega(By.ID, 'inputEmail')
element.send_keys('josefinoBusiness@gmail.com')

    element = pega(By.XPATH, '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/ul')
    time.sleep(1)
    element = pega(By.XPATH, '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/ul/li[32]/span[1]')
    element.click()

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
element.click()'''

# %%
# CT_005 Newsletter
driver.get("https://www.phptravels.com")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
element = pega(By.ID, 'address')
element.send_keys('josefinoBusiness@gmail.com')
try:
    alert = _waitForAlert(driver)
    alert.accept()
except: 
    pass

# %%
# CT_006 Velocidade
start = time.time()
driver.get("https://phptravels.com/")
end = time.time()
print(f' Demorou {end-start} ')
time.sleep(5)
start = time.time()
driver.get("https://phptravels.com/")
end = time.time()
print(f' Demorou {end-start} ')


# %%
# CT_007 Troca de tema
driver.get("https://www.phptravels.com")
element = pega(By.XPATH, '/html/body/header/nav/div/button')
element.click()
time.sleep(1)
element = pega(By.XPATH, '//*[@id="mynavbar"]/ul/li[3]/a')
element.click()
time.sleep(2)
element = pega(By.XPATH, '//*[@id="swup"]/div[2]/div/div[2]/div/div[1]/h2/a[1]')
element.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])


# %%
# CT_008 Seleciona pacote de compra
driver.get("https://phptravels.com")
element = pega(By.XPATH, '/html/body/header/nav/div/button')
element.click()
time.sleep(1)
element = pega(By.XPATH, '//*[@id="mynavbar"]/ul/li[2]/a')
element.click()
time.sleep(2)
element = pega(By.XPATH, '//*[@id="swup"]/div[2]/div/div/div[1]/div/div[2]/a')
element.click()


# %%
# CT_009 Verifica obrigatoriedade de acurácia
driver.get("https://phptravels.com/demo")
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
element.send_keys(int(numero1.text)*int(numero2.text))
element = pega(By.ID, 'demo')
element.click()
try:
    alert = _waitForAlert(driver)
    popup = alert.text
    print(popup)
    alert.accept()
except: 
    pass
#copiar o outro caso mas errar a soma ou algum campo assim
# %%
# CT_010 Testa troca de temas
driver.get("https://www.phptravels.com/themes")
element = pega(By.XPATH, '//*[@id="swup"]/div[2]/div/div[2]/div/div[1]/h2/a[1]')
element.click()
time.sleep(2)

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
html = driver.find_element(By.TAG_NAME, 'html')
html.send_keys(Keys.PAGE_DOWN)
element = pega(By.XPATH, '//*[@id="swup"]/div[2]/div/div[4]/div/div[1]/h2/a[1]')
time.sleep(1)
print(element.text)
element.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[2])

# %%
# CT_011 Teste de tema "não automatizável"
driver.get("https://www.phptravels.com")
element = pega(By.XPATH, '/html/body/header/nav/div/button')
element.click()
time.sleep(1)
element = pega(By.XPATH, '//*[@id="mynavbar"]/ul/li[3]/a')
element.click()
time.sleep(2)
element = pega(By.XPATH, '//*[@id="swup"]/div[2]/div/div[2]/div/div[1]/h2/a[1]')
element.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# %%
# CT_012 Verificar funcionamento da aba "Sucess Stories"
driver.get("https://www.phptravels.com")
element = pega(By.XPATH, '//*[@id="swup"]/strong/div[7]/div/div[1]/div')
driver.execute_script("arguments[0].scrollIntoView();", element)
decisao = random.randint(1,2)
if decisao == 1:
    element = pega(By.XPATH, '//*[@id="swup"]/strong/div[7]/div/div[4]/span[2]')
    element.click()
    time.sleep(0.5)
    element = pega(By.ID, 'client2')
    element.click()
    time.sleep(5)
if decisao == 2:
    element = pega(By.XPATH, '//*[@id="swup"]/strong/div[7]/div/div[4]/span[1]')
    element.click()
    time.sleep(0.5)
    element = pega(By.ID, 'client3')
    element.click()
    time.sleep(5)

element = pega(By.XPATH, '//*[@id="swup"]/strong/div[7]/div/div[2]/div/div[2]/div/div[2]/a[2]')
element.click()
driver.switch_to.window(driver.window_handles[1])

# %%
# CT_013 Não pode ser automatizado

# %%
# CT_014 Teste WhatsApp
driver.get("https://www.phptravels.com")
element = pega(By.XPATH, '/html/body/strong/a/div')
element.click()
driver.switch_to.window(driver.window_handles[1])

# %%
# CT_015 Teste chat não pode ser automatizado devidamente
driver.get("https://www.phptravels.com")
element = pega(By.XPATH, '//*[@id="button-body"]')
element.click()
time.sleep(1)
element = pega(By.XPATH, '//*[@id="new-message-textarea"]')
element.send_keys('Teste 123')
time.sleep(1)
element = pega(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/form/div[2]/div[1]/input')
element.send_keys('josefinoBusiness@gmail.com')
element = pega(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/form/div[2]/div[2]/input')
element.send_keys('+5598932323232')
element = pega(By.XPATH, '/html/body/div/div/div/div[1]/div[1]/div[1]/form/button')
element.click()

# %%
# CT_016 Teste About us
driver.get("https://phptravels.com/about-us/")
element = pega(By.XPATH, '//*[@id="swup"]/div[1]/div/div')
print(element.text)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)


# %%
# CT_017 Teste Email ocorre fora do site
driver.get("https://phptravels.com")
element = pega(By.XPATH, '//*[@id="swup"]/strong/div[4]/div[2]/div/div[2]/div/div[1]/a')
element.click()

# %%
# CT_018 Teste de formas de pagamento
driver.get("https://www.phptravels.com/pricing")
element = pega(By.XPATH, '//*[@id="firstname"]')
element.send_keys('Josefino')
element = pega(By.XPATH, '//*[@id="lastname"]')
element.send_keys('Almeida')
element = pega(By.XPATH, '//*[@id="email"]')
element.send_keys('josefinoBusiness@gmail.com')
element = pega(By.XPATH, '//*[@id="address"]')
element.send_keys('')
'''
pegar: 
    //*[@id="streetnumber"]
    //*[@id="city"]
    //*[@id="zip"]
    //*[@id="select2-drop"] ou //*[@id="select2-chosen-211"]
enviar: 
    Maranhão
    Enter
pegar:
    //*[@id="fiscal-personal"]
    //*[@id="phone"]
    //*[@id="select2-chosen-94"]
    //*[@id="cardnum"]
    //*[@id="select2-chosen-216"]
    //*[@id="s2id_ed_year"]/a
    //*[@id="secnum"]
    //*[@id="checkout-step-1"]/div/div[3]/div/div[2]/div[3]/button[1]

'''


# %%
# CT_019 Verificar Blog
driver.get("https://phptravels.com")
element = pega(By.XPATH, '/html/body/header/nav/div/button')
element.click()
time.sleep(2)
element = pega(By.XPATH, '//*[@id="mynavbar"]/ul/li[6]/a')
element.click()
time.sleep(1)
element = pega(By.XPATH, '//*[@id="mynavbar"]/ul/li[6]/ul/li[3]/a')
element.click()
driver.switch_to.window(driver.window_handles[1])

# %%
# CT_020 não pode ser automatizado pois ocorre fora do site
