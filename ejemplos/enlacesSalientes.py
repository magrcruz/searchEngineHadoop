base = "out/enlaces/"

# Define una lista de enlaces salientes para cada archivo
enlaces_salientes = {
    "link1": ["link3", "link4"],
    "link2": ["link4", "link5"],
    "link3": ["link1","link2","link5"],
    "link4": [],
    "link5": []
}

for url, enlaces in enlaces_salientes.items():
    with open(base + url.replace("/", "-") + '.txt', 'w') as file:
        file.write("\n".join(enlaces))
