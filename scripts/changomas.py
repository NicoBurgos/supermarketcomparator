import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

# TARDA 100 min
# Configura el driver de Selenium para Firefox
driver = webdriver.Firefox()
productos = []
# 9107 productos == 63751 lineas json
#enlaces = ['https://www.masonline.com.ar/desayunos-y-meriendas/cafe']
enlaces = ['https://www.masonline.com.ar/aceites-vinagres-y-aderezos','https://www.masonline.com.ar/arroz-legumbres-y-pastas','https://www.masonline.com.ar/caldos-sopas-y-pure','https://www.masonline.com.ar/condimentos-y-especias','https://www.masonline.com.ar/conservas-y-enlatados','https://www.masonline.com.ar/harinas','https://www.masonline.com.ar/kiosco','https://www.masonline.com.ar/panaderia','https://www.masonline.com.ar/panificados','https://www.masonline.com.ar/reposteria','https://www.masonline.com.ar/snacks','https://www.masonline.com.ar/desayunos-y-meriendas/bizcochos','https://www.masonline.com.ar/desayunos-y-meriendas/budines-magdalenas-y-otros','https://www.masonline.com.ar/desayunos-y-meriendas/cacao','https://www.masonline.com.ar/desayunos-y-meriendas/cafe','https://www.masonline.com.ar/desayunos-y-meriendas/cereales','https://www.masonline.com.ar/desayunos-y-meriendas/endulzantes','https://www.masonline.com.ar/desayunos-y-meriendas/frutas-secas-disecadas-y-mas','https://www.masonline.com.ar/desayunos-y-meriendas/galletas-de-arroz','https://www.masonline.com.ar/desayunos-y-meriendas/galletitas-dulces','https://www.masonline.com.ar/desayunos-y-meriendas/galletitas-saladas','https://www.masonline.com.ar/desayunos-y-meriendas/leches-y-chocolatadas','https://www.masonline.com.ar/desayunos-y-meriendas/te','https://www.masonline.com.ar/desayunos-y-meriendas/tostadas-grisines-y-marineras','https://www.masonline.com.ar/desayunos-y-meriendas/mermeladas-y-untables','https://www.masonline.com.ar/desayunos-y-meriendas/yerbas','https://www.masonline.com.ar/carniceria','https://www.masonline.com.ar/pescaderia','https://www.masonline.com.ar/verduras','https://www.masonline.com.ar/frutas','https://www.masonline.com.ar/lacteos','https://www.masonline.com.ar/quesos','https://www.masonline.com.ar/fiambres-y-embutidos','https://www.masonline.com.ar/congelados','https://www.masonline.com.ar/huevos','https://www.masonline.com.ar/pastas-y-tapas','https://www.masonline.com.ar/panificados','https://www.masonline.com.ar/panaderia','https://www.masonline.com.ar/cervezas','https://www.masonline.com.ar/vinos-y-espumantes','https://www.masonline.com.ar/fernet-y-aperitivos','https://www.masonline.com.ar/bebidas-blancas-licores-y-whiskys','https://www.masonline.com.ar/gaseosas','https://www.masonline.com.ar/aguas','https://www.masonline.com.ar/jugos','https://www.masonline.com.ar/bebidas-isotonicas-y-energizantes','https://www.masonline.com.ar/a-base-de-hierbas','https://www.masonline.com.ar/cuidado-de-la-piel','https://www.masonline.com.ar/cuidado-del-adulto','https://www.masonline.com.ar/pa%C3%B1ales-e-higiene','https://www.masonline.com.ar/cuidado-del-cabello','https://www.masonline.com.ar/cuidado-oral','https://www.masonline.com.ar/cuidado-personal','https://www.masonline.com.ar/nutricion','https://www.masonline.com.ar/farmacia','https://www.masonline.com.ar/proteccion-femenina','https://www.masonline.com.ar/accesorios-de-limpieza','https://www.masonline.com.ar/ba%C3%B1o','https://www.masonline.com.ar/calzado','https://www.masonline.com.ar/cocina','https://www.masonline.com.ar/desodorante-de-ambientes','https://www.masonline.com.ar/insecticidas','https://www.masonline.com.ar/lavandinas','https://www.masonline.com.ar/papeles-bolsas-y-films','https://www.masonline.com.ar/pisos-y-muebles','https://www.masonline.com.ar/ropa']

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
    seccions = driver.find_elements(By.CLASS_NAME, 'vtex-product-summary-2-x-container')          
    for sec in seccions:
        html = sec.get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        nombre_tag = soup.find('h3')
        if nombre_tag is None:
            return  # Sal del bucle y de la función si no hay más artículos
        nombre = nombre_tag.text.strip().encode().decode('utf-8')
        precio_span = soup.find(class_='valtech-gdn-dynamic-product-0-x-dynamicProductPrice')
        if precio_span:
            precio = re.sub(r'[^0-9,.]', '', precio_span.text.strip()).replace('.', '').replace(',', '.')
        else:
            precio = "No disponible"
            break
        href = soup.find(class_="vtex-product-summary-2-x-clearLink").get('href')    
        enlace = 'https://www.masonline.com.ar' + href   
        tag_imagen = soup.find('img')
        if tag_imagen:
            imagen = tag_imagen.get('src')
        else:
            imagen = ''
        producto_info = {'nombre': nombre, 'precio': float(precio), 'imagen': imagen, 'cadena':'ChangoMas', 'enlace':enlace}
        productos.append(producto_info) 

# Abre cada página y extrae los productos
for enlace in enlaces:
    i = 1
    prev_num_productos = float('inf')  # Inicializamos con infinito para asegurar la primera iteración
    while True:  # Bucle infinito hasta que se alcance la última página
        # Construye la URL con el número de página
        url = f"{enlace}?page={i}"
        
        # Abre la página web
        driver.get(url)
        
        # Espera a que la página se cargue completamente
        try:
            WebDriverWait(driver, 8).until(
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
            print("Se alcanzó la última página.")
            break  # Sal del bucle si no hay cambios en el número de productos
        
        # Actualiza el número de productos de la página anterior
        prev_num_productos = num_productos
        
        # Incrementa el número de página para continuar con la siguiente
        i += 1

# Cierra el navegador
driver.quit()

with open('productosChangoMas.json', 'w') as archivo_json:
    json.dump(productos, archivo_json, indent=4)

#Tardó 59minutos