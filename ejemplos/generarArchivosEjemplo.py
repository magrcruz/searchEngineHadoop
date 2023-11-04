import json

# Datos de prueba
data = [
    {
        "url": "/",
        "titulo": "Título de Example.com",
        "contenido": "Este es el contenido de Example.com.",
        "snipet":"snipet",
        "enlaces_salientes": ["/wiki/link1", "/wiki/link2"]
    },
    {
        "url": "/wiki/link1",
        "titulo": "Título de Link 1",
        "contenido": "Este es el contenido del primer enlace.",
        "snipet":"snipet",
        "enlaces_salientes": ["/wiki/link3"]
    },
    {
        "url": "/wiki/link2",
        "titulo": "Título de Link 2",
        "contenido": "Este es el contenido del segundo enlace.",
        "snipet":"snipet",
        "enlaces_salientes": ["/wiki/link4"]
    },
    {
        "url": "/wiki/link3",
        "titulo": "Título de Link 3",
        "contenido": "Este es el contenido del tercer enlace.",
        "snipet":"snipet",
        "enlaces_salientes": ["/wiki/link1", "/", "link2"]
    },
    {
        "url": "/wiki/link4",
        "titulo": "Título de Link 4",
        "contenido": "Este es el contenido del cuarto enlace.",
        "snipet":"snipet",
        "enlaces_salientes": []
    }
]

# Crear archivos JSON
for item in data:
    file_name = "out/paginas/" + item["url"].replace("https://", "").replace("/", "-")+".json"
    with open(file_name, "w") as json_file:
        json.dump(item, json_file, indent=4)

print("Archivos JSON de prueba generados.")
