import matplotlib.pyplot as plt 
import numpy as np
import os

################
#  PUNTO 1.3   #
################

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
    
################
#  PUNTO 1.4   #
################
fig, axs = plt.subplots(nrows=1,ncols=2,figsize=(18,4.5))

file_name = "Kapton"
kapton = get_longitud_refraccion(f"Taller_1\Plásticos Comerciales\{file_name}.yml")
x1 = np.array([e[0] for e in kapton ])
y1 = np.array([e[1] for e in kapton ])
mu1 = round(np.mean(y1),3)
std1 = round(np.std(y1),3)
axs[0].scatter(x1,y1)
axs[0].set_ylabel('Refraccion (n)')
axs[0].set_xlabel('Longitud onda (lambda)')
axs[0].set_title(f'{file_name} \n mean = {mu1}\n std = {std1}')

file_name = "NOA1348"
NOA1348 = get_longitud_refraccion(f"Taller_1\Adhesivos Ópticos\{file_name}.yml")
x2 = np.array([e[0] for e in NOA1348 ])
y2 = np.array([e[1] for e in NOA1348 ])
mu2 = round(np.mean(y2),3)
std2 = round(np.std(y2),3)
axs[1].scatter(x2,y2)
axs[1].set_ylabel('Refraccion (n)')
axs[1].set_xlabel('Longitud Onda (lambda) ')
axs[1].set_title(f'{file_name} \n mean = {mu2}\n std = {std2}')
plt.show()

################
#  PUNTO 1.5   #
################
def graficar(path):
     fig, axs = plt.subplots(nrows=1,ncols=1,figsize=(10,8))
     data = get_longitud_refraccion(path)
     x = np.array([e[0] for e in data ])
     y = np.array([e[1] for e in data ])
     mu = round(np.mean(y),3)
     std = round(np.std(y),3)
     elemento = path.split("\\")[-1].replace("yml","")
     axs.scatter(x,y)
     axs.set_ylabel('Refraccion (n)')
     axs.set_xlabel('Longitud onda (lambda)')
     axs.set_title(f'Material {elemento} \n mean = {mu} \n std = {std}') 

     save_to = path.replace("yml","jpg")
     plt.savefig(save_to)

#ITERAR PARA CADA UNA DE LAS CARPETAS
carpetas = ["Adhesivos Ópticos",
 "Combustible",
 "Exotico",
 "Materia Inorgánica",
 "Materia Orgánica",
 "Mezclas",
 "Plásticos Comerciales",
 "Vidrio"
]

for carpeta in carpetas:
    archivos_yml = os.listdir(f"Taller_1/{carpeta}/")
    for archivo in archivos_yml:
         graficar(f'Taller_1\{carpeta}\{archivo}')
