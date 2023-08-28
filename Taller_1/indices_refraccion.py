import matplotlib.pyplot as plt 
import numpy as np

def get_longitud_refraccion(archivo):
     with open(archivo,"r") as file:
          result = file.read()
          data = result.split("data: |")[1].split("\n        ")
          lista = []
          for i in range(len(data)):
               tupla = tuple(data[i].split(" "))
               lista.append(tupla)
          lista.pop(0)
          ultimo = (lista[-1][0],lista[-1][1].replace("\n",""))
          lista.pop()
          lista.append(ultimo)

          #Castear los strings de la tupla a floats
          lista = [tuple(float(item) for item in i) for i in lista]
          return lista
        
#print(get_longitud_refraccion("Taller_1\Vidrio\TK20.yml"))

kapton = get_longitud_refraccion("Taller_1\Plásticos Comerciales\French.yml")
x1 = np.array([e[0] for e in kapton ])
y1 = np.array([e[1] for e in kapton ])

fig, axs = plt.subplots(nrows=1,ncols=2,figsize=(18,4.5))
mu1 = np.mean(y1)
std1 = np.std(y1)
axs[0].scatter(x1,y1)
axs[0].set_ylabel('Refraccion')
axs[0].set_xlabel('Longitud onda ')
axs[0].set_title('Longitud onda vs Refraccion')

NOA138 = get_longitud_refraccion("Taller_1\Adhesivos Ópticos\Iezzi.yml.1")
x2 = np.array([e[0] for e in NOA138 ])
y2 = np.array([e[1] for e in NOA138 ])
fig, axs = plt.subplots(nrows=1,ncols=2,figsize=(18,4.5))
mu2 = np.mean(y2)
std2 = np.std(y2)
axs[1].scatter(x2,y2)
axs[1].set_ylabel('Refraccion')
axs[1].set_xlabel('Longitud onda ')
axs[1].set_title('')