import networkx as nx

# Nuevos datos de enlaces salientes
enlaces_salientes = {
    "link1": ["link3", "link4"],
    "link2": ["link4", "link5"],
    "link3": ["link1", "link2", "link5"],
    "link4": [],
    "link5": []
}

# Crear un gráfico dirigido (grafo de enlaces)
G = nx.DiGraph()

# Agregar nodos y enlaces al gráfico basados en los nuevos datos
for url, enlaces in enlaces_salientes.items():
    G.add_node(url)
    for enlace in enlaces:
        G.add_edge(url, enlace)

# Calcular el PageRank
pagerank = nx.pagerank(G)

# Imprimir los resultados del PageRank
for url, rank in pagerank.items():
    print(f"{url}: PageRank = {rank:.4f}")
