from mineral import Mineral
import pandas as pd
import matplotlib.pyplot as plt

class ExpansionTermicaMineral(Mineral):
    def __init__(self, csv, nombre, dureza, rompimiento,color,composicion,lustre,gravedad,sistema):
        
        super().__init__(nombre, dureza, lustre, rompimiento,color,composicion,sistema, gravedad,)
        self.temperatura = pd.read_csv(csv)['celsius_temperature'].to_numpy()
        self.volumen = pd.read_csv(csv)['volume_cc'].to_numpy()
        
    def coef_expansionter(self):
        '''Calcula la expansion termica'''
        V = self.volumen.copy()
        T = self.temperatura.copy()
        derivada= []
        for i in range(1,len(V)-1):
          derivada.append((V[i+1]-V[i-1])/(T[i+1]-T[i-1]))
        
        alfa = (1/V[1:-1])*derivada
        
        fig, axs = plt.subplots(1,2,figsize =(15,10))

        axs[0].scatter(T,V)
        axs[0].set_ylabel(r'Volume ($m^3$)')
        axs[0].set_xlabel('Temperature (C°)')
        axs[0].set_title(f'{self.nombre} Volume vs Temperature')

        axs[1].scatter(T[1:-1],alfa)
        axs[1].set_ylabel(r'Expansion Termica  $\alpha = \frac{1}{V}\cdot\frac{dV}{dT}$')
        axs[1].set_xlabel('Temperature (C°)')
        axs[1].set_title('Expansion termica vs Temperature')

        fig.suptitle(f'{self.nombre}',fontsize=16)

        plt.savefig(f"{self.nombre}_exptermica_volume.jpg")
        
        return alfa,fig
        



