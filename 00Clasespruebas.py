#utilizar la clase 00ClasesEspeciales.py
import os 
os.system('cls' if os.name == 'nt' else 'clear')

# importar la clase 
from Clasesespeciales import Libro 
libro = Libro("Stephen King","It", 1032)
print (len(libro))
