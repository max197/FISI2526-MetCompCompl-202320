from expansiontermicamineral import ExpansionTermicaMineral

olivino = ""
grafito = ""

# Open the file and search for lines starting with the specific string
with open("minerales.txt", "r") as file:
    for line in file:
        if line.startswith("olivino"):
            olivino = line.split("\t")
        if line.startswith("grafito"):
            grafito = line.split("\t")

olivino = ExpansionTermicaMineral(
    csv = "olivine_angel_2017.csv",
    nombre=olivino[0],
    dureza =olivino[1],
    rompimiento=olivino[2],
    color = olivino[3],
    composicion= olivino[4],
    lustre = olivino[5],
    gravedad = [6],
    sistema=olivino[7]
    )

olivino.coef_expansionter()

grafito = ExpansionTermicaMineral(
    csv = "graphite_mceligot_2016.csv",
    nombre=grafito[0],
    dureza =grafito[1],
    rompimiento=grafito[2],
    color = grafito[3],
    composicion= grafito[4],
    lustre = grafito[5],
    gravedad = [6],
    sistema=grafito[7]
    )

grafito.coef_expansionter()

