# -*- coding: utf-8 -*-
import csv
import xmltodict
import os
import re

count = 0
index = 0

with open("nomeacoes1.csv", "w", encoding="utf-8", newline="") as arquivo_de_saida:

    writer = csv.writer(arquivo_de_saida)

    writer.writerow(["NOME", "SIMBOLO_NOMEACAO", "TITULO_PORTARIA", "DATA_PORTARIA", "LINK_PORTARIA"])

    for pasta_ano in os.listdir("nomeacoes"):
        for pasta_mes in os.listdir("nomeacoes/" + pasta_ano):
            for arquivo_ato in os.listdir("nomeacoes/" + pasta_ano + "/" + pasta_mes):

                endereco_do_arquivo = "nomeacoes/" + pasta_ano + "/" + pasta_mes + "/" + arquivo_ato

                with open(endereco_do_arquivo, encoding='utf-8') as ato_xml:

                    ato = xmltodict.parse(ato_xml.read())

                    titulo_da_portaria = ""
                    data_da_portaria = ""
                    orgao_da_portaria = ""
                    link_da_portaria = ""
                    subtitulo_da_portaria = ""
                    texto_da_portaria = ""
                    nome_do_servidor = ""
                    cargo_titulo = ""
                    cargo_lotacao = ""
                    cargo_simbolo = ""
                    encontrado = False

                    titulo_da_portaria = ato["xml"]["article"]["body"]["Identifica"]
                    data_da_portaria = ato["xml"]["article"]["@pubDate"]
                    orgao_da_portaria = ato["xml"]["article"]["@artCategory"]
                    link_da_portaria = ato["xml"]["article"]["@pdfPage"]
                    tipo_da_portaria = ato["xml"]["article"]["@artType"]
                    subtitulo_da_portaria = ato["xml"]["article"]["body"]["SubTitulo"]
                    texto_da_portaria = ato["xml"]["article"]["body"]["Texto"].lower()

                    for trecho in texto_da_portaria.split("</p>"):
                        if ("ADRIANA RAMOS SILVA" in trecho):
                            print(endereco_do_arquivo)
                            
    arquivo_de_saida.close()
