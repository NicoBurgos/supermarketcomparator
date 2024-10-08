import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

# TARDA 50 min
# Configura el driver de Selenium para Firefox
driver = webdriver.Firefox()
productos = []
# 22 enlaces
# 5192 productos == 41538 lineas json
#enlaces = ["https://www.vea.com.ar/Almacen/Aceites-y-Vinagres"]
enlaces = ["https://www.vea.com.ar/Almacen/Aceites-y-Vinagres","https://www.vea.com.ar/Almacen/Aderezos","https://www.vea.com.ar/Almacen/Arroz-y-Legumbres","https://www.vea.com.ar/Almacen/Sal-Pimienta-y-Especias","https://www.vea.com.ar/Almacen/Conservas","https://www.vea.com.ar/Almacen/Desayuno-y-Merienda","https://www.vea.com.ar/Almacen/Golosinas-y-Chocolates","https://www.vea.com.ar/Almacen/harinas","https://www.vea.com.ar/Almacen/panificados","https://www.vea.com.ar/Almacen/caldos-sopas-pure-y-bolsas-para-horno","https://www.vea.com.ar/Almacen/para-preparar","https://www.vea.com.ar/Almacen/pastas-secas-y-salsas","https://www.vea.com.ar/Almacen/snacks","https://www.vea.com.ar/bebidas","https://www.vea.com.ar/carnes","https://www.vea.com.ar/frutas-y-verduras","https://www.vea.com.ar/lacteos","https://www.vea.com.ar/perfumeria","https://www.vea.com.ar/limpieza","https://www.vea.com.ar/quesos-y-fiambres","https://www.vea.com.ar/congelados","https://www.vea.com.ar/panaderia-y-reposteria"]
#["https://www.vea.com.ar/congelados","https://www.vea.com.ar/almacen","https://www.vea.com.ar/bebida","https://www.vea.com.ar/carnes","https://www.vea.com.ar/frutas-y-verduras","https://www.vea.com.ar/lacteos","https://www.vea.com.ar/perfumeria","https://www.vea.com.ar/limpieza","https://www.vea.com.ar/quesos-y-fiambres","https://www.vea.com.ar/panaderia-y-reposteria",]

def scroll_slowly():
    # Obtiene la altura total del documento
    total_height = driver.execute_script("return document.body.scrollHeight")
    # Define el incremento de scroll
    scroll_increment = 1500
    for i in range(0, total_height, scroll_increment):
        # Ejecuta el script de scroll
        driver.execute_script(f"window.scrollTo(0, {i});")
        # Espera un poco antes de continuar
        time.sleep(1)  # Ajusta el tiempo según sea necesario

def scrap_current_page(productos):
    # Encuentra y extrae los elementos <h2>
    seccions = driver.find_elements(By.CLASS_NAME, "vtex-search-result-3-x-galleryItem")
    for sec in seccions:
        html = sec.get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        product = soup.find('h2')
        if product is None:
            continue
        nombre = product.text.strip().encode().decode('utf-8')
        price = soup.find(id='priceContainer')
        if price:
            precio = price.text.replace('$', '').replace('.', '').replace(',', '.')
        else:
            precio = '0'
        image = soup.find('img')
        if image:
            imagen = image.get('src')
        else:
            imagen = ''
        link = soup.find(class_='vtex-product-summary-2-x-clearLink')
        if link:
            enlace = 'https://www.vea.com.ar' + link.get('href')
        else:
            enlace = ''
        producto_info = {'nombre': nombre, 'precio': float(precio), 'imagen': imagen, 'cadena': 'Vea', 'enlace': enlace}
        productos.append(producto_info)

# Abre cada página y extrae los productos
for enlace in enlaces:
    i = 1
    prev_num_productos = -1  # Inicializamos con -1 para asegurar la primera iteración
    while True:  # Bucle infinito hasta que se alcance la última página
        # Construye la URL con el número de página
        url = f"{enlace}?page={i}"
        
        # Abre la página web
        driver.get(url)
        
        # Espera a que la página se cargue completamente
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "vtex-product-summary-2-x-productNameContainer"))
            )
        except:
            print("Error al cargar la página. " + url)
            break
        
        # Hacer scroll hasta el final de la página
        scroll_slowly()
       
        # Extrae los productos de la página actual
        scrap_current_page(productos)
        
        # Obtiene el número de productos en la página actual
        num_productos = len(productos)
        
        # Verifica si hay un cambio en el número de productos
        if num_productos == prev_num_productos:
            print("Se alcanzó la última página en " + enlace)
            break  # Sal del bucle si no hay cambios en el número de productos
        
        # Actualiza el número de productos de la página anterior
        prev_num_productos = num_productos
        
        # Incrementa el número de página para continuar con la siguiente
        i += 1

# Cierra el navegador
driver.quit()

with open('productosVea.json', 'w') as archivo_json:
    json.dump(productos, archivo_json, indent=4)