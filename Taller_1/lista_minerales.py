import matplotlib.pyplot as plt
import matplotlib.patches as patches
from mineral import Mineral
import numpy as np

def crear_minerales(archivo):
    minerales = []
    
    with open(archivo,"r",encoding=None) as file:
        lines = file.readlines()[1:]
        for line in lines:
          text = line.strip( ).split("\t")
          nombre = text[0]
          dureza = float(text[1])
          rompimiento = text[2]
          color = text[3]
          composicion = text[4]
          lustre = text[5]
          gravedad = float(text[6])
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

#Arreglo con los 17 minerales en minerales.txt
minerales = crear_minerales("minerales.txt")

def cantidad_silicatos(minerales):
  #print([mineral.es_silicato() for mineral in minerales])
  return sum([mineral.es_silicato() for mineral in minerales])

def densidad_promedio(minerales):
  densidades= [mineral.calcular_densidad() for mineral in minerales]
  return round(sum(densidades)/len(densidades),3)


  
        
