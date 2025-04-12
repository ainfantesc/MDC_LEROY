#####
#import random
import requests
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#import sku as sku
import acepta_cookies as ac
import re
from bs4 import BeautifulSoup
import os

# Asi podemos setear el user-agent en selenium
opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.6998.178 Safari/537.36")
# Agregar a todos sus scripts de selenium para que no aparezca la ventana de seleccionar navegador por defecto: (desde agosto 2024)
opts.add_argument("--disable-search-engine-choice-screen")
#opts.add_argument("--headless") # cuan estemos en productivo eliminaremos habilitaremos esta linea para no cargar el navegador de Selenium

# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome(options=opts)

# Archivo temporal para sincronización
SYNC_FILE = "sync_done.txt"

# Eliminar archivo de sincronización si existe
if os.path.exists(SYNC_FILE):
    os.remove(SYNC_FILE)

# Crear carpeta para imágenes si no existe
if not os.path.exists("Dataset/imagenes_productos"):
    os.makedirs("Dataset/imagenes_productos")



# Crear archivo LICENSE.txt automáticamente
def crear_license():
    licencia_texto = """
Dataset License: CC BY-NC-SA 4.0

Este dataset se distribuye bajo la licencia Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).

Permite:
    Compartir: copiar y redistribuir el material en cualquier medio o formato.
    Adaptar: remezclar, transformar y construir a partir del material.

Bajo las siguientes condiciones:
    Atribución: Debe dar crédito de manera adecuada, proporcionar un enlace a la licencia e indicar si se han realizado cambios.
    No Comercial: No puede utilizar el material con fines comerciales.
    Compartir Igual: Si remezcla, transforma o construye a partir del material, debe distribuir su contribución bajo la misma licencia que el original.

Más información: https://creativecommons.org/licenses/by-nc-sa/4.0/
"""
    with open("LICENSE.txt", "w", encoding="utf-8") as license_file:

        license_file.write(licencia_texto.strip())

crear_license()
      


# Voy a la pagina que quiero
driver.get('https://www.leroymerlin.es/sitemap-category1.xml')
sleep(10)
ac.accept_cookies(driver)

sleep(3)
page_source=driver.page_source

driver.quit()

# Parsear el contenido con BeautifulSoup usando lxml como parser XML
soup = BeautifulSoup(page_source, 'lxml-xml')

# Buscar todos los elementos <loc> y extraer las URLs
loc_elements = soup.find_all('loc')
urls = [loc.text for loc in loc_elements]

# Imprimir las URLs encontradas
for url in urls:
    print(url)

# Opcional: guardar las URLs en un archivo
with open('urls.txt', 'w') as file:
    for url in urls:
        file.write(url + '\n')
        #sku.proceso_scraping(url)

        # Esperar a que el segundo script termine
        while not os.path.exists(SYNC_FILE):
            sleep(1)  # Espera activa (puedes ajustar el tiempo si es necesario)
        
        # Eliminar archivo de sincronización para la próxima iteración
        os.remove(SYNC_FILE)
        print(f"Procesamiento de {url} completado.")