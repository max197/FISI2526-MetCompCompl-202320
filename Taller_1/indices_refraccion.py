import matplotlib.pyplot as plt 
import numpy as np

#PUNTO 1.3
def get_longitud_refraccion(archivo):
     with open(archivo,"r") as file:
          result = file.read()
          data = result.split('data: |\n')[1].split('\nSPECS')[0].split('  - type')[0].strip().split('\n        ')
          lista = []
          for i in range(0,len(data)):
               tupla = tuple(data[i].split(" "))
               lista.append(tupla)
          ultimo = (lista[-1][0],lista[-1][1].replace("\n",""))
          lista.pop()
          lista.append(ultimo)

          #Castear los strings de la tupla a floats
          lista = [tuple(float(item) for item in i) for i in lista]
          return lista

#PUNTO 1.4

fig, axs = plt.subplots(nrows=1,ncols=2,figsize=(18,4.5))


kapton = get_longitud_refraccion("Taller_1\Plásticos Comerciales\French.yml")
x1 = np.array([e[0] for e in kapton ])
y1 = np.array([e[1] for e in kapton ])
mu1 = np.mean(y1)
std1 = np.std(y1)
axs[0].scatter(x1,y1)
axs[0].set_ylabel('Refraccion')
axs[0].set_xlabel('Longitud onda ')
axs[0].set_title(f'Kapton mean = {mu1}, std = {std1}')
plt.show()


#TO DO: 
# 1. Arreglar las tuplas que tienen el string SPECS

'''
NOA138 = get_longitud_refraccion("Taller_1\Adhesivos Ópticos\Iezzi.yml.1")
x2 = np.array([e[0] for e in NOA138 ])
y2 = np.array([e[1] for e in NOA138 ])
mu2 = np.mean(y2)
std2 = np.std(y2)
axs[1].scatter(x2,y2)
axs[1].set_ylabel('Refraccion')
axs[1].set_xlabel('Longitud onda ')
axs[1].set_title('')
'''
#1.5
def graficar(ruta):
     fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(10,8))
     data = get_longitud_refraccion(ruta)
     x = np.array([e[0] for e in data ])
     y = np.array([e[1] for e in data ])
     mu = np.mean(y)
     std = np.std(y)
     elemento = ruta.split("\\")[-1].replace("yml","")
     axs.scatter(x1,y1)
     axs.set_ylabel('Refraccion')
     axs.set_xlabel('Longitud onda ')
     axs.set_title(f'Material {elemento}. mean = {mu}, std = {std}') 

     save_to = ruta.replace("yml","png")
     plt.savefig(save_to)

#TODO: ITERAR PARA CADA UNA DE LAS CARPETAS
#graficar("Taller_1\Vidrio\BF8.yml")

     

