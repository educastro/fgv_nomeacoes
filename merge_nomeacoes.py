import csv
import xmltodict
from os import listdir, walk

for (dirpath, dirnames, filenames) in walk("nomeacoes/"):
    print(filenames)
    #for file in filenames:
