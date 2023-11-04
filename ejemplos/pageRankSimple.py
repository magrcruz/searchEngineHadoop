import networkx as nx

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

# Crear un gráfico dirigido (grafo de enlaces)
G = nx.DiGraph()

# Agregar nodos y enlaces al gráfico
for item in data:
    G.add_node(item["url"])
    for enlace in item["enlaces_salientes"]:
        G.add_edge(item["url"], enlace)

# Calcular el PageRank
pagerank = nx.pagerank(G)
#nx.pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1e-06, nstart=None, weight='weight', dangling=None)

# Imprimir los resultados del PageRank
for url, rank in pagerank.items():
    print(f"{url}: PageRank = {rank:.4f}")
