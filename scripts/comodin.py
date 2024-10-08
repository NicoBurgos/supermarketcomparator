import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# TARDA 15 MINS
# Configura el driver de Selenium para Firefox
driver = webdriver.Firefox()
# Inicializa las listas
enlaces = ['https://www.comodinencasa.com.ar/frescos/pastas-frescas-y-tapas','https://www.comodinencasa.com.ar/frescos/carniceria', 'https://www.comodinencasa.com.ar/frescos/dulces-solidos', 'https://www.comodinencasa.com.ar/frescos/fiambres-y-embutidos', 'https://www.comodinencasa.com.ar/frescos/verduleria', 'https://www.comodinencasa.com.ar/frescos/levaduras-y-grasas', 'https://www.comodinencasa.com.ar/frescos/huevos', 'https://www.comodinencasa.com.ar/congelados/congelados-de-pescados', 'https://www.comodinencasa.com.ar/congelados/congelados-de-verduras', 'https://www.comodinencasa.com.ar/congelados/helados', 'https://www.comodinencasa.com.ar/almacen/arroz-legumbres-y-semolas', 'https://www.comodinencasa.com.ar/almacen/pastas-secas-y-salsas', 'https://www.comodinencasa.com.ar/almacen/caldos-sopas-y-pures', 'https://www.comodinencasa.com.ar/almacen/aceitunas-y-encurtidos', 'https://www.comodinencasa.com.ar/almacen/azucar-y-endulzantes', 'https://www.comodinencasa.com.ar/almacen/conservas', 'https://www.comodinencasa.com.ar/almacen/desayuno-y-merienda', 'https://www.comodinencasa.com.ar/almacen/reposteria', 'https://www.comodinencasa.com.ar/almacen/harinas-y-feculas', 'https://www.comodinencasa.com.ar/almacen/leches-en-polvo', 'https://www.comodinencasa.com.ar/almacen/aceites', 'https://www.comodinencasa.com.ar/almacen/aderezos', 'https://www.comodinencasa.com.ar/almacen/acetos-vinagres-sales-y-especias', 'https://www.comodinencasa.com.ar/almacen/pastas-sin-tacc', 'https://www.comodinencasa.com.ar/bebidas/aguas', 'https://www.comodinencasa.com.ar/bebidas/gaseosas', 'https://www.comodinencasa.com.ar/bebidas/jugos', 'https://www.comodinencasa.com.ar/bebidas/aperitivos', 'https://www.comodinencasa.com.ar/bebidas/bebidas-blancas-y-licores', 'https://www.comodinencasa.com.ar/bebidas/cervezas', 'https://www.comodinencasa.com.ar/bebidas/vinos-y-espumantes', 'https://www.comodinencasa.com.ar/bebidas/bebidas-hidratantes-y-energizantes', 'https://www.comodinencasa.com.ar/panaderia/elaboracion-propia', 'https://www.comodinencasa.com.ar/panaderia/para-tus-comidas', 'https://www.comodinencasa.com.ar/panaderia/pan-lactal', 'https://www.comodinencasa.com.ar/panaderia/pan-rallado-y-rebozadores', 'https://www.comodinencasa.com.ar/perfumeria/cuidado-personal', 'https://www.comodinencasa.com.ar/perfumeria/cuidado--capilar', 'https://www.comodinencasa.com.ar/perfumeria/cuidado-facial', 'https://www.comodinencasa.com.ar/perfumeria/cuidado-bucal', 'https://www.comodinencasa.com.ar/perfumeria/farmacia', 'https://www.comodinencasa.com.ar/perfumeria/proteccion-femenina', 'https://www.comodinencasa.com.ar/limpieza/accesorios-de-limpieza', 'https://www.comodinencasa.com.ar/limpieza/desodorante-de-ambientes', 'https://www.comodinencasa.com.ar/limpieza/insecticidas', 'https://www.comodinencasa.com.ar/limpieza/lavandinas', 'https://www.comodinencasa.com.ar/limpieza/limpieza-de-bano', 'https://www.comodinencasa.com.ar/limpieza/limpieza-de-calzado', 'https://www.comodinencasa.com.ar/limpieza/limpieza-de-cocina', 'https://www.comodinencasa.com.ar/limpieza/limpieza-de-ropa', 'https://www.comodinencasa.com.ar/limpieza/limpieza-piso-y-muebles', 'https://www.comodinencasa.com.ar/limpieza/papeles'
]
productos = []

# Abre la página web
def scrap_pages (page):
    driver.get(page)

    # Espera a que el botón de cierre esté presente y haz clic en él
    try:
        wait = WebDriverWait(driver, 10)
        close_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "styles__CloseButton-sc-sinqit-2")))
        close_button.click()
    except Exception as e:
        print("No se encontró el botón de cierre o ocurrió un error:", e)

    def scrap_current_page(productos):
        # Encuentra y extrae los elementos <h2>
        products = driver.find_elements(By.CLASS_NAME, "styles__Title-sc-z5d33k-6")
        prices = driver.find_elements(By.CLASS_NAME, "styles__BestPrice-sc-z5d33k-12")
        images = driver.find_elements(By.CLASS_NAME, 'styles__Image-sc-z5d33k-3')
        links = driver.find_elements(By.CLASS_NAME,'styles__TitleWrapper-sc-z5d33k-4')
       
        
        for product, price, image,link in zip(products, prices, images,links):
            nombre = product.text.encode().decode('utf-8')
            precio = price.text.replace('$', '').replace('.', '').replace(',', '.')
            imagen = image.get_attribute('src')
            enlace = link.get_attribute('href')
            producto_info = {'nombre': nombre, 'precio': float(precio), 'imagen': imagen, 'cadena': 'Comodin', "enlace":enlace}
            productos.append(producto_info)

    # Función para ir a la página especificada
    def go_to_page(page_number):
        try:
            # Encuentra el contenedor de la paginación
            pagination_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "styles__Container-sc-1wayfnq-2.bjrhvv")))
            # Encuentra todos los botones dentro del contenedor de la paginación
            page_buttons = pagination_container.find_elements(By.CLASS_NAME, "styles__PageButton-sc-1wayfnq-3")
            
            # Haz clic en el botón correspondiente al número de página
            for button in page_buttons:
                if button.text == str(page_number):
                    button.click()
                    # Espera un poco para que la nueva página se cargue
                    time.sleep(2)  # Ajusta este tiempo según sea necesario
                    return

        except Exception as e:
            print(f"No se encontró la página {page_number} o ocurrió un error:")

    # Encuentra el número total de páginas
    def get_total_pages():
        try:
            pagination = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "styles__Container-sc-1wayfnq-2.bjrhvv")))
            page_buttons = pagination.find_elements(By.CLASS_NAME, "styles__PageButton-sc-1wayfnq-3")
            total_pages = max([int(button.text) for button in page_buttons if button.text.isdigit()])
            return total_pages
        except Exception as e:
            print(f"No se pudo determinar el número total de páginas: {e}")
            return 1

    # Obtener el número total de páginas
    total_pages = get_total_pages()

    # Recorre todas las páginas
    for page_number in range(1, total_pages + 1):
        go_to_page(page_number)
        scrap_current_page(productos)


for enlace in enlaces:
    scrap_pages(enlace)

# Cierra el navegador
driver.quit()

#Tardó 10 minutos
with open('productosComodin.json', 'w') as f:
    json.dump(productos, f, indent=4)