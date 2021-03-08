from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

main_web = 'https://siata.gov.co/descarga_siata/index.php/index2/calidad_aire_anual/'

driver = webdriver.Chrome(executable_path=r'/Users/PutosHackers/Downloads/chromedriver')

driver.get(main_web)

sleep(1)


username = driver.find_element_by_name("usuario")
password = driver.find_element_by_name("contrasena")

username.send_keys('Lauforero32')
password.send_keys('Datos1234', Keys.ENTER)

sign_in = driver.find_element_by_id("Ingresar")

sign_in.click()

sleep(1)

driver.get('https://siata.gov.co/descarga_siata/index.php/index2/calidad_aire/')


text = 'Estudiar la calidad del aire en la ciudad de medellín y el valle.'
fecha_1 = '2000-01-24 00:00:50'
fecha_2 = '2021-01-24 00:00:50'

sleep(1)

motivo_descarga = driver.find_element_by_id("motivo_descarga")
motivo_descarga.send_keys(text, Keys.ENTER)

sleep(1)

datetimepicker = driver.find_element_by_id('datetimepicker')
datetimepicker.send_keys(fecha_1, Keys.ENTER)

sleep(1)

datetimepicker2 = driver.find_element_by_id('datetimepicker2')
datetimepicker2.send_keys(fecha_2, Keys.ENTER)

sleep(1)

select_all = driver.find_element_by_id("selectall")
select_all.click()

sleep(1)

consulta = driver.find_element_by_id("realizarConsulta")
consulta.click()

sleep(1)

import numpy as np

buttons = driver.find_elements_by_css_selector('.btn.btn-info')

a = np.size(buttons)
print('------------------------------------------')
print(a)
print('------------------------------------------')

i = 0

for btn in buttons:
    i += 1
    print(i)
    btn.click()
    print('------------------------------------------')
