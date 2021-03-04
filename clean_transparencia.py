import csv
import os
import unidecode
import unicodedata

for pasta_transparencia in os.listdir("transparencia"):
    for arquivos in os.listdir("transparencia/" + pasta_transparencia):

        print("Iniciando " + arquivos)

        tabela_entrada = open("transparencia/" + pasta_transparencia + "/" + arquivos, encoding="latin-1")#ISO-8859-1")
        tabela_saida = open("transparencia_limpo/" + arquivos[:-4] + "_filtro_das.csv", "w", encoding="utf-8", newline='')

        reader = csv.DictReader(tabela_entrada, delimiter=";")
        writer = csv.writer(tabela_saida)

        writer.writerow(["NOME", "CPF",	"SIGLA_FUNCAO",	"NIVEL_FUNCAO",	"FUNCAO", "ATIVIDADE", "UORG_LOTACAO", "ORG_LOTACAO", "ORGSUP_LOTACAO",	"UORG_EXERCICIO", "ORG_EXERCICIO", "ORGSUP_EXERCICIO", "SITUACAO_VINCULO", "DATA_INGRESSO_CARGOFUNCAO",	"DATA_INGRESSO_ORGAO", "DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO", "UF_EXERCICIO"])

        for linha in reader:
            if linha["SIGLA_FUNCAO"] == "DAS":
                writer.writerow([linha["NOME"], linha["CPF"], linha["SIGLA_FUNCAO"], linha["NIVEL_FUNCAO"], linha["FUNCAO"], linha["ATIVIDADE"], linha["UORG_LOTACAO"], linha["ORG_LOTACAO"], linha["ORGSUP_LOTACAO"],	linha["UORG_EXERCICIO"], linha["ORG_EXERCICIO"], linha["ORGSUP_EXERCICIO"], linha["SITUACAO_VINCULO"], linha["DATA_INGRESSO_CARGOFUNCAO"],	linha["DATA_INGRESSO_ORGAO"], linha["DATA_DIPLOMA_INGRESSO_SERVICOPUBLICO"], linha["UF_EXERCICIO"]])

        tabela_entrada.close()
        tabela_saida.close()

        print("Finalizando " + arquivos)
