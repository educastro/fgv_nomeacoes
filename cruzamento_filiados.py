import csv
import pandas as pd
import unidecode

with open("todos_os_filiados_do_brasil_limpo_v2.csv", "r", encoding='utf-8') as inputfile_filiados, open("nomeacoes.csv", "r", encoding='utf-8') as inputfile_nomeacoes:
    reader = csv.DictReader(inputfile_filiados, delimiter=",")
    with open("todos_os_filiados_do_brasil_limpo_v2.csv", "w", encoding='utf-8', newline='') as outputfile:

        writer = csv.writer(outputfile, delimiter=";")

        writer.writerow(['NOME DO FILIADO', 'SIGLA DO PARTIDO', 'UF', 'SITUACAO DO REGISTRO', 'DATA DA DESFILIACAO', 'DATA DO CANCELAMENTO'])

        for row in reader:
            writer.writerow([unidecode.unidecode(row["NOME DO FILIADO"]).strip(), row["SIGLA DO PARTIDO"], row["UF"], row["SITUACAO DO REGISTRO"], row["DATA DA DESFILIACAO"], row["DATA DO CANCELAMENTO"]])
            print(row["SIGLA DO PARTIDO"])

outputfile.close()
inputfile.close()
