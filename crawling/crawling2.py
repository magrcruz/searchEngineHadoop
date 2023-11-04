import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import json
import re
import time

# Función para extraer el contenido de los párrafos
def extract_content(soup):
    content_data = []
    for paragraph in soup.find_all('p'):
        text = paragraph.get_text()

        # Eliminar tildes de las letras con tilde y mantener la letra ñ intacta
        text = re.sub(
            r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1",
            normalize("NFD", text), 0, re.I
        )
        text = text.replace("n\u0303", "ñ")  # Restaurar la letra "ñ"

        # Eliminar comandos para fórmulas matemáticas (por ejemplo, {\displaystyle ...})
        text = re.sub(r'{\\[^}]+}', '', text)

        # Eliminar comandos y referencias (por ejemplo, [1], [2], [[Archivo:...])
        text = re.sub(r'\[\d+\]', '', text)  # Eliminar referencias numéricas
        text = re.sub(r'\[\[Archivo:[^\]]+\]\]', '', text)  # Eliminar referencias a archivos
        text = re.sub(r'\[\[[a-zA-Z0-9\s]+\]\]', '', text)  # Eliminar otras referencias en doble corchete

        # Eliminar caracteres no alfabéticos, convertir a minúsculas y eliminar saltos de línea adicionales
        text = re.sub(r'(\s*\n\s*)+', ' ', text).lower()

        content_data.append(text)

    return " ".join(content_data)

# Función para realizar web scraping recursivo
def scrape_wikipedia(url, max_pages, current_depth=0):
    if current_depth >= max_pages:
        return

    start_time = time.time()  # Registrar el tiempo de inicio

    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        soup = BeautifulSoup(page_content, "html.parser")
        
        # Extraer el título de la página
        title = soup.find("h1").text

        # Extraer el contenido de títulos, subtítulos y párrafos
        content = extract_content(soup)
        content_elements = soup.find_all('p')
        # Extraer el snippet (primer párrafo, 200 primeras palabras)
        snippet = " ".join(content_elements[0].text.split()[:200]) if content_elements else ""
        
        # Definir una expresión regular para filtrar los enlaces no deseados
        pattern = re.compile(r"/wiki/.*:|/wiki/Wiki")

        # Extraer los enlaces salientes
        outgoing_links = [a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("/wiki/") and not pattern.match(a["href"])]

        # Imprimir el número de outgoing_links
        print(f'Página: {url}, outgoing_links: {len(outgoing_links)}')

        # Guardar los datos en un diccionario
        page_data = {
            "url": url,
            "titulo": title,
            "contenido": content,
            "snippet": snippet,
            "enlaces_salientes": outgoing_links
        }

        data.append(page_data)

        for link in outgoing_links:
            next_url = f"https://es.wikipedia.org{link}"
            scrape_wikipedia(next_url, max_pages, current_depth + 1)

    end_time = time.time()  # Registrar el tiempo de finalización
    elapsed_time = end_time - start_time
    print(f'Tiempo para la página : {elapsed_time:.2f} segundos')

# URL de la página de Wikipedia a la que deseas iniciar el web scraping
initial_url = "https://es.wikipedia.org/wiki/Algoritmo"

# Máximo número de páginas a recopilar
max_pages = 2

# Crear una lista para almacenar los datos
data = []

# Iniciar el web scraping recursivo
scrape_wikipedia(initial_url, max_pages)

# Guardar el dataset como un archivo JSON
with open('wikipedia_dataset2.json', 'w', encoding='utf-8') as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=4)
