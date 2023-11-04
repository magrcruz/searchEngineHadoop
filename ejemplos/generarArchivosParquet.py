import pandas as pd

# Datos de prueba
data = [
    {
        "url": "/",
        "titulo": "Título de Example.com",
        "contenido": "Este es el contenido de Example.com.",
        "enlaces_salientes": ["/wiki/link1", "/wiki/link2"]
    },
    {
        "url": "/wiki/link1",
        "titulo": "Título de Link 1",
        "contenido": "Este es el contenido del primer enlace.",
        "enlaces_salientes": ["/wiki/link3"]
    },
    {
        "url": "/wiki/link2",
        "titulo": "Título de Link 2",
        "contenido": "Este es el contenido del segundo enlace.",
        "enlaces_salientes": ["/wiki/link4"]
    },
    {
        "url": "/wiki/link3",
        "titulo": "Título de Link 3",
        "contenido": "Este es el contenido del tercer enlace.",
        "enlaces_salientes": ["/wiki/link1", "/", "link2"]
    },
    {
        "url": "/wiki/link4",
        "titulo": "Título de Link 4",
        "contenido": "Este es el contenido del cuarto enlace.",
        "enlaces_salientes": []
    }
]

# Crear y guardar un archivo Parquet para cada conjunto de datos
for item in data:
    df = pd.DataFrame([item])
    # Limpia la URL para usarla como nombre de archivo
    file_name = "out/paginasParquet/"+item["url"].replace("/", "_").replace(":", "_") + ".parquet"
    df.to_parquet(file_name, index=False)

print("Archivos Parquet separados generados con nombres de archivo basados en la URL.")
