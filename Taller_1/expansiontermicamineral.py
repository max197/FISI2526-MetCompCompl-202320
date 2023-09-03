from mineral import Mineral
import pandas as pd

class ExpansionTermicaMineral(Mineral):
    def __init__(self, csv, nombre, dureza, rompimiento,color,composicion,lustre,gravedad,sistema):
        # Call the constructor of the parent class
        super().__init__(nombre, dureza, rompimiento,color,composicion,lustre,gravedad,sistema)
        self.temperatura = pd.read_csv(csv)['celsius_temperature']
        print(self.temperatura)
        self.volumen = pd.read_csv(csv)['volume_cc']
        print(self.volumen)
        
    def coef_expansionter():
      return None



obj1 = ExpansionTermicaMineral(csv = "olivine_angel_2017.csv",nombre="a",dureza=2, rompimiento=1, color = "dfsgf",composicion="CO",lustre="af", gravedad=9, sistema="sdf")



