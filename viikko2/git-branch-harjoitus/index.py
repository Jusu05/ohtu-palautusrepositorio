from logger import logger
from osamaara import osamaaara
from summa import summa
from erotus import erotus
from tulo import tulo

logger("aloitetaan ohjelma")

x = int(input("luku 1: "))
y = int(input("luku 2: "))
print(f"{x} + {y} = {summa(x, y)}") 
print(f"{x} - {y} = {erotus(x, y)}") 
print(f"{x} * {y} = {tulo(x, y)}") 
print(f"{x} * {y} = {osamaaara(x, y)}") 

logger("lopetetaan")
print("goodbye!")