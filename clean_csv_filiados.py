import csv
import pandas as pd

with open("todos_os_filiados_do_brasil.csv", "r") as inputfile:
    reader = csv.DictReader(inputfile, delimiter=";")
    with open("todos_os_filiados_do_brasil_limpo.csv", "w", encoding='utf-8', newline='') as outputfile:

        writer = csv.writer(outputfile)

        writer.writerow(['NOME DO FILIADO', 'SIGLA DO PARTIDO', 'UF', 'SITUACAO DO REGISTRO', 'DATA DA DESFILIACAO', 'DATA DO CANCELAMENTO'])

        for row in reader:
            writer.writerow([row["NOME DO FILIADO"], row["SIGLA DO PARTIDO"], row["UF"], row["SITUACAO DO REGISTRO"], row["DATA DA DESFILIACAO"], row["DATA DO CANCELAMENTO"]])
            print(row["SIGLA DO PARTIDO"])

outputfile.close()
inputfile.close()
