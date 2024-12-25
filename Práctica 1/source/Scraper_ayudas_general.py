from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Configuración del WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Ruta al WebDriver de Chrome
webdriver_service = Service(executable_path=r'C:\Users\pedro\OneDrive\Escritorio\Pedro\Universidad\Master\5to Semestre\Tipología y ciclo de vida de datos\PR 1\chromedriver.exe')

# Inicializa el navegador
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# URL base
base_url = 'https://planderecuperacion.gob.es/como-acceder-a-los-fondos/convocatorias'
num_paginas = 50
datos_convocatorias = []

def extraer_datos_convocatoria(url_convocatoria):
    driver.get(url_convocatoria)
    wait = WebDriverWait(driver, 10)

    # Función auxiliar para obtener texto de un elemento si existe
    def obtener_texto(xpath):
        try:
            return driver.find_element(By.XPATH, xpath).text
        except Exception as e:
            print(f"Error en obtener_texto({xpath}): {e}")
            return None

    # Función auxiliar para obtener un enlace de un elemento si existe
    def obtener_enlace(xpath):
        try:
            return driver.find_element(By.XPATH, xpath).get_attribute('href')
        except Exception as e:
            print(f"Error en obtener_enlace({xpath}): {e}")
            return None

    # Extraer datos específicos
    tipo_convocatoria = obtener_texto('.//p[@class="c-convocatoriasResult__type"]')
    titulo = obtener_texto('.//h1[@class="c-convocatoriasResult__title"]')
    organo_convocante = obtener_texto('.//p[contains(@class,"cabeza--convocante")]/following-sibling::p[1]')
    localizacion = obtener_texto('.//p[contains(@class,"cabeza--ejecucion") and contains(text(),"Localización")]/following-sibling::p[1]')
    importe = obtener_texto('.//p[contains(@class,"cabeza--ejecucion") and contains(text(),"Importe")]/following-sibling::p[1]')
    procedimiento = obtener_texto('.//p[contains(@class,"cabeza--ejecucion") and contains(text(),"Procedimiento")]/following-sibling::p[1]')
    actividad = obtener_texto('.//p[contains(@class,"cabeza--ejecucion") and contains(text(),"Actividad")]/following-sibling::p[1]')
    enlace_convocatoria = obtener_enlace('.//a[contains(@class,"btn-link")]')

    return {
        'Tipo de convocatoria' : tipo_convocatoria,
        'Título': titulo,
        'Órgano convocante': organo_convocante,
        'Localización': localizacion,
        'Importe': importe,
        'Procedimiento': procedimiento,
        'Actividad': actividad,
        'Enlace al detalle de la convocatoria': enlace_convocatoria,
        'Enlace original': url_convocatoria
    }

try:
    for pagina in range(1, num_paginas + 1):
        # Navega a la página principal con la lista de convocatorias
        url_pagina = f'{base_url}?page={pagina}'
        driver.get(url_pagina)

        # Espera explícita para que los elementos carguen
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "c-convocatoriasResult")))

        # Recolecta las URLs de todas las convocatorias en la página actual
        urls_convocatorias = []
        convocatorias = driver.find_elements(By.CLASS_NAME, "c-convocatoriasResult")
        for convocatoria in convocatorias:
            try:
                enlace = convocatoria.find_element(By.TAG_NAME, 'a')
                urls_convocatorias.append(enlace.get_attribute('href'))
            except Exception as e:
                print(f"Error al obtener URL de convocatoria: {e}")
                continue

        # Procesa cada convocatoria por su URL
        for url_convocatoria in urls_convocatorias:
            try:
                datos = extraer_datos_convocatoria(url_convocatoria)
                datos_convocatorias.append(datos)
            except Exception as e:
                print(f"Error al extraer datos de la convocatoria: {e}")
                continue

finally:
    driver.quit()

# Guardar los datos en un DataFrame de pandas y exportarlos a CSV
df_convocatorias = pd.DataFrame(datos_convocatorias)
df_convocatorias.to_csv(r'C:\Users\pedro\OneDrive\Escritorio\Pedro\Universidad\Master\5to Semestre\Tipología y ciclo de vida de datos\PR 1\convocatorias.csv', index=False, encoding='utf-8-sig')

print("Scraping completado. Datos guardados en convocatorias.csv")
