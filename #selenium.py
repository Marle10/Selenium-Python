from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()  # Asegúrate de tener ChromeDriver en tu PATH


url = "https://www.youtube.com"
driver.get(url)


expected_title = "YouTube"
actual_title = driver.title

if expected_title in actual_title:
    print("La prueba pasó: El título de la página es correcto.")
else:
    print(f"La prueba falló: Se esperaba que el título contenga '{expected_title}', pero se obtuvo '{actual_title}'")

try:
    # Esperar hasta que aparezca la barra de búsqueda
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "search_query"))
    )
    
    # Escribir un término y presionar Enter
    search_term = "Selenium Python"
    search_box.send_keys(search_term + Keys.RETURN)

    # Esperar hasta que aparezcan resultados
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "contents"))
    )

    # Verificar que los resultados contienen el término buscado
    results = driver.find_elements(By.ID, "video-title")
    if any(search_term.lower() in r.text.lower() for r in results):
        print(f"La prueba pasó: Se encontraron resultados para '{search_term}'.")
    else:
        print(f"La prueba falló: No se encontraron resultados para '{search_term}'.")

except Exception as e:
    print(f"Error durante la automatización: {e}")


time.sleep(10)


driver.quit()
