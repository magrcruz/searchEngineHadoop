import requests
import re
from bs4 import BeautifulSoup

# URL de la página de Wikipedia a la que deseas hacer web scraping
url = "https://es.wikipedia.org/wiki/Algoritmo"

# Realizar una solicitud HTTP para obtener el contenido de la página
response = requests.get(url)

if response.status_code == 200:
    page_content = response.text
    soup = BeautifulSoup(page_content, "html.parser")

    # Extraer el título de la página
    title = soup.find("h1").text

    # Extraer el contenido del artículo (puede variar según la estructura de la página)
    content = ""

    # Definir una expresión regular para filtrar los enlaces no deseados
    pattern = re.compile(r"/wiki/.*:|/wiki/Wiki")

    # Extraer los enlaces salientes que cumplan con la expresión regular
    outgoing_links = [a["href"] for a in soup.find_all("a", href=True) if a["href"].startswith("/wiki/") and not pattern.match(a["href"])]

    # Imprimir o almacenar los datos
    print("Título:", title)
    print("Contenido:\n", content)
    for link in outgoing_links:
        print(link)

else:
    print("No se pudo obtener la página")