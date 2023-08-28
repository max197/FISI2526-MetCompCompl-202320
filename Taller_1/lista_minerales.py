import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mineral import Mineral


def crear_minerales(archivo):
    minerales = []
    
    with open(archivo,"r",encoding=None) as file:
        lines = file.readlines()[1:]
        for line in lines:
          text = line.strip( ).split("\t")
          nombre = text[0]
          dureza = text[1]
          rompimiento = text[2]
          color = text[3]
          composicion = text[4]
          lustre = text[5]
          gravedad = text[6]
          sistema = text[7]

          mineral = Mineral(nombre = nombre,
                            dureza= dureza,
                            lustre=lustre,
                            rompimiento_por_fractura=rompimiento,
                            color= color,
                            composicion=composicion,
                            sistema_cristalino= sistema,
                            specific_gravity= gravedad)
          minerales.append(mineral)

    return minerales

minerales = crear_minerales("minerales.txt")
print(len(crear_minerales("minerales.txt")))
print(crear_minerales("minerales.txt")[-1].es_silicato())
minerales[0].visualizar_material()
        
        
