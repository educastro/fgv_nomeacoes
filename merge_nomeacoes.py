import csv
import xmltodict
import os
import re

count = 0
index = 0
for foldername in os.listdir("nomeacoes"):
    for filename in os.listdir("nomeacoes/" + foldername):

        filepath = "nomeacoes/" + foldername + "/" + filename

        with open(filepath, encoding='utf-8') as ato_xml:

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
            subtitulo_da_portaria = ato["xml"]["article"]["body"]["SubTitulo"]
            texto_da_portaria = ato["xml"]["article"]["body"]["Texto"].lower()

            for trecho in texto_da_portaria.split("</p>"):
                if ("nomear" in trecho) and ("das 1" in trecho or "das-1" in trecho):
                    encontrado = False
                    nome_do_servidor = ""
                    index += 1

                    regex_nomeacao_tipo_1 = re.search(r"nomear\W*\s*\w\s\d\w\s\w+\s(.+),*\spara\sexercer\s.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_1 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_1.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_1.group(2)

                    regex_nomeacao_tipo_2 = re.search(r"nomear\W*\s*\w\s\d\w\s\w+\s\w+\s\w+\s(.+),*\spara\sexercer\s.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_2 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_2.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_2.group(2)

                    regex_nomeacao_tipo_3 = re.search(r"nomear\W*\s*\w\sdelegad[oa]\sde\spolícia\sfederal\s(.+),*\spara\sexercer\so.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_3 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_3.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_3.group(2)

                    regex_nomeacao_tipo_4 = re.search(r"nomear\W*\s*[oa]\sservidora*\s(.+),*\Wmatrícula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_4 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_4.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_4.group(2)

                    regex_nomeacao_tipo_5 = re.search(r"nomear\W*\s*[oa]\s.+federal\s(.+),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_5 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_5.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_5.group(2)

                    regex_nomeacao_tipo_6 = re.search(r"nomear\W*\s*[oa]\s.+federal\s(.+),*\spara\so\s.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_6 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_6.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_6.group(2)

                    regex_nomeacao_tipo_7 = re.search(r"nomear\W*\s*(.+),*\scpf.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_7 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_7.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_7.group(2)

                    regex_nomeacao_tipo_8 = re.search(r"nomear\W*\s*(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_8 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_8.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_8.group(2)

                    regex_nomeacao_tipo_9 = re.search(r"nomear\W*\s*(.+),*\smatr[ií]cula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_9 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_9.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_9.group(2)

                    regex_nomeacao_tipo_10 = re.search(r"nomear\W*\s*(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_10 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_10.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_10.group(2)

                    regex_nomeacao_tipo_11 = re.search(r"nomear\W*\s*(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_11 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_11.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_11.group(2)

                    regex_nomeacao_tipo_12 = re.search(r"nomear\W*\s*(.+),*\s[nd]o.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_12 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_12.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_12.group(2)

                    regex_nomeacao_tipo_13 = re.search(r"nomear\W*\s*(.+?),*.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_13 and encontrado == False:
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_13.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_13.group(2)

                    if encontrado:
                        count += 1

                    # if nome_do_servidor == "":
                    #     print(str(index) + " - " + filepath + ": " + nome_do_servidor)

                    print(str(index) + " - " + filepath + ": " + cargo_simbolo)

print("Quantidade: " + str(count))
