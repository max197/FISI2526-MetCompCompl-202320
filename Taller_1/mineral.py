
import matplotlib.pyplot as plt
import matplotlib.patches as patches


class Mineral:
    
    def __init__(self,nombre, dureza,lustre,rompimiento_por_fractura,color, composicion, sistema_cristalino,specific_gravity):
        self.nombre = nombre
        self.dureza = dureza
        self.lustre = lustre
        self.rompimiento_por_fractura = rompimiento_por_fractura
        self.color = color
        self.composicion = composicion
        self.sistema_cristalino = sistema_cristalino
        self.specific_gravity = specific_gravity

    def es_silicato(self):
        if "Si" in self.composicion and "O" in self.composicion:
            return True
        return False
    
    def calcular_densidad(self):
        return float(self.specific_gravity)*997
   
    def visualizar_material(self):
        # Create a figure and axis
        fig, ax = plt.subplots()

        rect = patches.Rectangle((0.1, 0.1), 0.6, 0.6, color=self.color)
        ax.add_patch(rect)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        plt.show()
    
    def print_cualidades(self):
        print(f"Dureza: {self.dureza}\n Rompimiento: {self.rompimiento_por_fractura}\n Sistema Cristalino: {self.sistema_cristalino}")


        
    
