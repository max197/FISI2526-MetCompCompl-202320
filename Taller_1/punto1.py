import yaml as yl
import os 
def repaso_funciones(archivo):
    with open(archivo, 'r') as file:
          yaml_data = yl.safe_load(file)
          info = yaml_data["DATA"][0]["data"]
          print(type(info))
          print(info)

    print(yaml_data)

#repaso_funciones("C:\Users\maxal\Documents\FISI2526-MetCompCompl-202320\Taller_1\hola.yml")
repaso_funciones("Taller_1\hola.yml")

