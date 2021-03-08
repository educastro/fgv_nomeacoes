import csv
import pandas as pd
import unidecode

with open("todos_os_filiados_do_brasil_limpo_v2.csv", "r", encoding='utf-8') as inputfile:
    reader = csv.DictReader(inputfile, delimiter=";")
    with open("todos_os_filiados_do_brasil_limpo_v3.csv", "w", encoding='utf-8', newline='') as outputfile, open("todos_os_filiados_do_brasil_limpo_v3_excluidos.csv", "w", encoding='utf-8', newline='') as outputfile2:

        writer = csv.writer(outputfile, delimiter=";")
        writer2 = csv.writer(outputfile2, delimiter=";")

        writer.writerow(['NOME DO FILIADO', 'SIGLA DO PARTIDO', 'UF', 'SITUACAO DO REGISTRO', 'DATA DA DESFILIACAO', 'DATA DO CANCELAMENTO'])
        writer2.writerow(['NOME DO FILIADO', 'SIGLA DO PARTIDO', 'UF', 'SITUACAO DO REGISTRO', 'DATA DA DESFILIACAO', 'DATA DO CANCELAMENTO'])

        for row in reader:
            print(row["SIGLA DO PARTIDO"])

            if row["SITUACAO DO REGISTRO"] == "REGULAR":
                writer.writerow([unidecode.unidecode(row["NOME DO FILIADO"]).strip(), row["SIGLA DO PARTIDO"], row["UF"], row["SITUACAO DO REGISTRO"], row["DATA DA DESFILIACAO"], row["DATA DO CANCELAMENTO"]])
            else:
                writer2.writerow([unidecode.unidecode(row["NOME DO FILIADO"]).strip(), row["SIGLA DO PARTIDO"], row["UF"], row["SITUACAO DO REGISTRO"], row["DATA DA DESFILIACAO"], row["DATA DO CANCELAMENTO"]])


outputfile.close()
inputfile.close()
