import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tarda 50min
# Configurar el navegador y otras variables
driver = webdriver.Firefox()
id_sucursal = '&IdSucursal=23'
enlaces = [
    'https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=1',
    'https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=44',
    'https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=2','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=3','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=6','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=8','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=9','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=12','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=13','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=58','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=62','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=7','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=5','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=15','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=19','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=64','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=25','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=38','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=39','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=63','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=32','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=49','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=14','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=52','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=10','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=11','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=4','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=57','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=1&IdCategoria=60','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=1','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=14','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=7','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=4','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=3','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=10','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=2','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=2&IdCategoria=15','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=9','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=8','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=22','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=6','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=11','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=29','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=30','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=3','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=13','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=1','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=4','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=5','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=10','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=33','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=18','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=2','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=3&IdCategoria=12','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=34','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=10','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=12','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=14','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=8','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=11','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=29','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=46','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=26','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=19','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=5','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=28','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=1','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=6','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=16','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=9','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=30','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=4&IdCategoria=18','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=9','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=11','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=1','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=20','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=12','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=17','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=13','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=5','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=22','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=2','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=23','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=3','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=24','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=16','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=15','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=6&IdCategoria=21','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=6','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=1','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=12','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=2','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=5','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=3','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=16','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=15','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=10','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=13','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=4','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=9','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=8','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=7&IdCategoria=7','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=21&IdCategoria=4','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=21&IdCategoria=5','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=21&IdCategoria=6','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=21&IdCategoria=2','https://shop.yaguar.com.ar/frontendSP/asp/iframe_ListadoDeProductos.asp?IdDepto=21&IdCategoria=1'
]
paginacion = [2,3,2,1,4,1,3,2,4,1,2,2,3,1,4,1,1,3,2,3,4,1,2,2,4,2,2,2,4,1,2,2,1,3,1,3,2,14,2,1,1,1,5,1,4,2,6,2,3,5,1,1,1,2,1,2,3,15,4,7,1,1,2,6,5,1,3,3,6,1,6,1,4,1,4,1,1,1,1,2,2,1,1,1,2,3,1,5,2,4,1,1,4,1,9,4,1,1,3,1,1,1,5,3,2,3,10]
productos = []

def scrap_current_page(productos, enlace):
    try:
        # Esperar a que los elementos estén presentes antes de intentar obtenerlos
        prods = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'PRODTITULOA')))

        prices = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'PRODPRECIOA')))
        all_images = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'img')))
        images = [imagen for imagen in all_images if imagen.get_attribute('width') == '90']

        # Recolectar la información de los productos en la página actual
        cadena = 'Yaguar'
        for prod, price, img in zip(prods, prices, images):
            nombre = prod.text.lower()
            precio = price.text.replace('.', '').replace(',', '.')
            producto = {
                'nombre': nombre.capitalize(),
                'precio': float(precio),
                'imagen': img.get_attribute('src'),
                'cadena': cadena,
                'enlace': enlace
            }
            productos.append(producto)
    except:
        print('No existen productos')

# Iterar sobre los enlaces y la paginación
for enlace, pag in zip(enlaces, paginacion):
    driver.get(enlace + id_sucursal)
    scrap_current_page(productos, enlace)
    # Realizar el scraping de cada página para el enlace actual
    for i in range(2, pag+1):       
        try:         
            # Ejecutar JavaScript para navegar a la siguiente página
            main_window = driver.current_window_handle
            script = f"navegar({20 * (i-1)});"
            driver.execute_script(script)
                       
            time.sleep(3)            
            all_windows = driver.window_handles 
            new_window = [window for window in all_windows if window != main_window][0]
            driver.switch_to.window(new_window)
            # Realizar el scraping en la nueva pestaña
            scrap_current_page(productos,enlace)
            time.sleep(1)
            
            # Cerrar la nueva pestaña después de completar el scraping
            driver.close()
            driver.switch_to.window(main_window)
        except Exception as e:
            print(f"Error en la paginación: {e}")
            print(enlace)
            break

# Guardar los productos obtenidos en un archivo JSON
with open('productosYaguar.json', 'w', encoding='utf-8') as f:
    json.dump(productos, f, indent=4, ensure_ascii=False)

# Cerrar el navegador al finalizar el scraping
driver.quit()
