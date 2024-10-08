import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re
#TARDA 2 HORA
#URLs de las páginas de Carrefour: 66
#Productos = 8123 == 56863 lineas json
#Ultimo scrap 6056 prods
enlaces = ["https://www.carrefour.com.ar/Almacen/Aceites-y-vinagres","https://www.carrefour.com.ar/Almacen/Pastas-secas","https://www.carrefour.com.ar/Almacen/Arroz-y-legumbres","https://www.carrefour.com.ar/Almacen/Harinas","https://www.carrefour.com.ar/Almacen/Enlatados-y-Conservas","https://www.carrefour.com.ar/Almacen/Sal-aderezos-y-saborizadores","https://www.carrefour.com.ar/Almacen/Caldos-sopas-y-pure","https://www.carrefour.com.ar/Almacen/Reposteria-y-postres","https://www.carrefour.com.ar/Almacen/Snacks","https://www.carrefour.com.ar/Desayuno-y-merienda/Galletitas-bizcochitos-y-tostadas","https://www.carrefour.com.ar/Desayuno-y-merienda/Budines-y-magdalenas","https://www.carrefour.com.ar/Desayuno-y-merienda/Yerba","https://www.carrefour.com.ar/Desayuno-y-merienda/Cafe","https://www.carrefour.com.ar/Desayuno-y-merienda/Infusiones","https://www.carrefour.com.ar/Desayuno-y-merienda/Azucar-y-endulzantes","https://www.carrefour.com.ar/Desayuno-y-merienda/Mermeladas-y-otros-dulces","https://www.carrefour.com.ar/Desayuno-y-merienda/Cereales-y-barritas","https://www.carrefour.com.ar/Desayuno-y-merienda/Golosinas-y-chocolates","https://www.carrefour.com.ar/Bebidas/Cervezas","https://www.carrefour.com.ar/Bebidas/Vinos","https://www.carrefour.com.ar/Bebidas/Fernet-y-aperitivos","https://www.carrefour.com.ar/Bebidas/Bebidas-blancas","https://www.carrefour.com.ar/Bebidas/Gaseosas","https://www.carrefour.com.ar/Bebidas/Aguas","https://www.carrefour.com.ar/Bebidas/Jugos","https://www.carrefour.com.ar/Bebidas/Bebidas-isotonicas","https://www.carrefour.com.ar/Bebidas/Bebidas-energizantes","https://www.carrefour.com.ar/Bebidas/Espumantes-y-sidras","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Leches","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Yogures","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Mantecas-margarinas-y-levaduras","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Dulce-de-leche","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Cremas-de-leche","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Postres","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Huevos","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Tapas-y-pastas-frescas","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Dulce-de-membrillo-y-otros-dulces","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Salchichas","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Quesos","https://www.carrefour.com.ar/Lacteos-y-productos-frescos/Fiambres","https://www.carrefour.com.ar/Carnes-y-Pescados","https://www.carrefour.com.ar/Frutas-y-Verduras","https://www.carrefour.com.ar/Panaderia","https://www.carrefour.com.ar/Congelados","https://www.carrefour.com.ar/Limpieza/Limpieza-de-la-ropa","https://www.carrefour.com.ar/Limpieza/Limpieza-de-pisos-y-muebles","https://www.carrefour.com.ar/Limpieza/Insecticidas","https://www.carrefour.com.ar/Limpieza/Limpieza-de-cocina","https://www.carrefour.com.ar/Limpieza/Lavandinas","https://www.carrefour.com.ar/Limpieza/Rollos-de-cocina-y-servilletas","https://www.carrefour.com.ar/Limpieza/Papeles-higienicos","https://www.carrefour.com.ar/Limpieza/Limpieza-de-bano","https://www.carrefour.com.ar/Limpieza/Desodorantes-de-ambiente","https://www.carrefour.com.ar/Limpieza/Articulos-de-limpieza","https://www.carrefour.com.ar/Perfumeria/Cuidado-del-cabello","https://www.carrefour.com.ar/Perfumeria/Cuidado-dental","https://www.carrefour.com.ar/Perfumeria/Jabones","https://www.carrefour.com.ar/Perfumeria/Proteccion-femenina","https://www.carrefour.com.ar/Perfumeria/Cuidado-de-la-piel","https://www.carrefour.com.ar/Perfumeria/Antitranspirantes-y-desodorantes","https://www.carrefour.com.ar/Perfumeria/Cuidado-corporal","https://www.carrefour.com.ar/Perfumeria/Repelentes","https://www.carrefour.com.ar/Perfumeria/Algodones-e-hisopos","https://www.carrefour.com.ar/Perfumeria/Farmacia","https://www.carrefour.com.ar/Perfumeria/Proteccion-para-adultos","https://www.carrefour.com.ar/Perfumeria/Fragancias-y-maquillaje"]
#['https://www.carrefour.com.ar/Almacen','https://www.carrefour.com.ar/Desayuno-y-merienda','https://www.carrefour.com.ar/Bebidas','https://www.carrefour.com.ar/Lacteos-y-productos-frescos','https://www.carrefour.com.ar/Carnes-y-Pescados','https://www.carrefour.com.ar/Frutas-y-Verduras','https://www.carrefour.com.ar/Panaderia','https://www.carrefour.com.ar/Congelados','https://www.carrefour.com.ar/Limpieza','https://www.carrefour.com.ar/Perfumeria']

driver = webdriver.Firefox()
productos = []

def scroll_slowly():
    # Obtiene la altura total del documento
    total_height = driver.execute_script("return document.body.scrollHeight")
    # Define el incremento de scroll
    scroll_increment = 1500
    for i in range(0, total_height, scroll_increment):
        # Ejecuta el script de scroll
        driver.execute_script(f"window.scrollTo(0, {i});")
        # Espera un poco antes de continuar
        time.sleep(1) # Ajusta el tiempo según sea necesario

def scrap_current_page(productos):
    # Encuentra y extrae los elementos <h2>
    seccions = driver.find_elements(By.CLASS_NAME, 'vtex-product-summary-2-x-container')
    for sec in seccions:
        html = sec.get_attribute('outerHTML')
        soup = BeautifulSoup(html, 'html.parser')
        nombre_tag = soup.find('h3')
        if nombre_tag is None:
            return # Sal del bucle y de la función si no hay más artículos
        nombre = nombre_tag.text.strip().encode().decode('utf-8')
        precio_span = soup.find(class_='valtech-carrefourar-product-price-0-x-currencyContainer')
        if precio_span:
            precio = re.sub(r'[^0-9,.]', '', precio_span.text.strip()).replace('.', '').replace(',', '.')
        else:
            precio = "No disponible"
            break
        href = soup.find(class_="vtex-product-summary-2-x-clearLink").get('href')
        enlace = 'https://www.carrefour.com.ar' + href
        tag_imagen = soup.find('img')
        if tag_imagen:
            imagen = tag_imagen.get('src')
        else:
            imagen = ''
        producto_info = {'nombre': nombre, 'precio': float(precio), 'imagen': imagen, 'cadena':'Carrefour', 'enlace':enlace
        }
        productos.append(producto_info)

for enlace in enlaces:
    i = 1
    prev_num_productos = float('inf') # Inicializamos con infinito para asegurar la primera iteración
    while True: # Bucle infinito hasta que se alcance la última página
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


driver.quit()

with open('productosCarrefour.json', 'w') as archivo_json:
    json.dump(productos, archivo_json, indent=4)

#Tardó 59minutos
#2hs 20m 4/10/24
