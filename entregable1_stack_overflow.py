# Selenium: librería que facilita el uso de un Webdriver, el cual se utiliza para simular acciones de un ser humano
# en una web, tales como un clic.

# @author: joaquinjoanaazuara

import traceback
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement

# WebdriverWait permite una espera hasta que se producen determinadas condiciones o hasta que se alcanza
# el tiempo límite establecido antes de que se lance una excepción (se conoce como ExplicitWait).
# La excepción lanzada es: 'selenium.common.exceptions.TimeoutException'.
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

# El método logger.exception() devuelve un mensaje de error y la traza del registro, que incluye detalles como
# el número de línea de código en el que se ha producido la excepción.
import logging
logger = logging.getLogger()

# Excepciones controladas en este programa.
from selenium.common.exceptions import (
    ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException,
    TimeoutException, WebDriverException, WebDriverException)

# Librerías varias
import time
import os
import requests

# Librerías para manejo de datos
import pandas as pd
import numpy as np
import random
import re
import csv

# Función que da acceso a login
def login():
    try:
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "nav[class='h100 ml-auto overflow-x-auto pr12']")))
        login_button = browser.find_element(By.CSS_SELECTOR, "a[data-gps-track='login.click']")
        login_button.click()
    except (NoSuchElementException, TimeoutException) as ex:
        print("Excepción al hacer login stack overflow: ", type(ex))
        browser.quit()

# Función que selecciona la opción: 'permitir el uso de cookies de stack overflow en mi navegador'
def accept_cookies_stackoverflow():
    try:
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,
                                                     "button[class='flex--item s-btn s-btn__primary js-accept-cookies js-consent-banner-hide']")))
        cookies_button = browser.find_element(By.CSS_SELECTOR,
                                              "button[class='flex--item s-btn s-btn__primary js-accept-cookies js-consent-banner-hide']")
        cookies_button.click()
    except (NoSuchElementException, TimeoutException) as ex:
        print("Excepción al aceptar cookies de stack overflow: ", type(ex))
        browser.quit()

# Función que permite realizar login en stack overflow con username y password.
def acceso_cuenta():
    try:
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[id='email']")))
        username = browser.find_element(By.CSS_SELECTOR, "input[id='email']")
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[id='password']")))
        password = browser.find_element(By.CSS_SELECTOR, "input[id='password']")
        username.clear()
        password.clear()
        username.send_keys(usuario)
        password.send_keys(clave)
        wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "button[id='submit-button']")))
        login_button = browser.find_element(By.CSS_SELECTOR, "button[id='submit-button']")
        login_button.click()
    except (NoSuchElementException, TimeoutException) as ex:
        print("Excepción al intentar acceder a mi cuenta de stack overflow: ", type(ex))
        browser.quit()

def get_SOS_help(command):
    try:
        exec(command)
    except Exception as e:
        time.sleep(2)
        box_error = browser.find_element(By.CSS_SELECTOR, "input[role='combobox']")
        box_error.send_keys(str(e))
        box_error.send_keys(Keys.RETURN)
        time.sleep(2)
        more_button = browser.find_element(By.CSS_SELECTOR,
                                 "button[class='s-btn s-btn__muted s-btn__outlined s-btn__dropdown blr0 brr-sm js-dropdown-toggle']")
        more_button.click()
        time.sleep(2)
        score_button = browser.find_element(By.CSS_SELECTOR, "a[title='Highest scored search results']")
        score_button.click()

        time.sleep(3)
        lista_soluciones = browser.find_elements(By.CSS_SELECTOR, "a[href]")
        solucion_seleccionada = lista_soluciones[55]
        solucion_seleccionada.send_keys(Keys.RETURN)

        #obtener
        lista_html = browser.find_elements(By.CSS_SELECTOR, "div[class='s-prose js-post-body']")
        soup = BeautifulSoup(str(lista_html[1].text), 'html.parser')
        print(soup)

# Inicio del programa
# Inicialización variables del programa
path_chromedriver = "C:/Users/.................."
usuario = "........@gmail.com"
clave = "..........."

# Crear una instancia del navegador en modo incognito
s = Service(path_chromedriver)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
browser = webdriver.Chrome(service=s, options=chrome_options)
wait = WebDriverWait(browser, 10)

# Abro Stack Overflow
browser.get("https://stackoverflow.com/")
login()
accept_cookies_stackoverflow()
actual_site = acceso_cuenta()

mycode='''
product = {"item": "iPhone","price": 1599,"qty_available": 40}
print("We have total " + product["qty_available"] + " quantities of Product " + product["item"])
'''

get_SOS_help(mycode)

time.sleep(300)



