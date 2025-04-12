from selenium.webdriver.common.by import By
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os



def accept_cookies(driver):
    try:
        # Esperar hasta que aparezca el botón de cookies (ajusta el selector según el sitio)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "cookiesAcceptAll"))
        ).click()
        print("Cookies aceptadas.")
    except Exception as e:
        print(f"No se encontró el formulario de cookies o hubo un error: {e}")