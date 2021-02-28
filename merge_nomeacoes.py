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
            tipo_da_portaria = ato["xml"]["article"]["@artType"]
            subtitulo_da_portaria = ato["xml"]["article"]["body"]["SubTitulo"]
            texto_da_portaria = ato["xml"]["article"]["body"]["Texto"].lower()

            for trecho in texto_da_portaria.split("</p>"):
                if ("nomear" in trecho) and ("das 1" in trecho or "das-1" in trecho) and (tipo_da_portaria != "Retificação"):
                    encontrado = False
                    nome_do_servidor = ""
                    index += 1
                    regex = ""

                    regex_nomeacao_tipo_1 = re.search(r"nomear\W*\s*\w\s\d\w\s\w+\s\w+\s\w+\s(.+?),*\spara\sexercer\so\scargo\sde\sassistente\snesta.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_1 and encontrado == False:
                        regex = "regex_nomeacao_tipo_1"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_1.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_1.group(2)

                    regex_nomeacao_tipo_2 = re.search(r"nomear\W*\s*\w\s\d\w\s\w+\s(.+),*\spara\sexercer\s.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_2 and encontrado == False:
                        regex = "regex_nomeacao_tipo_2"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_2.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_2.group(2)

                    regex_nomeacao_tipo_3 = re.search(r"nomear\W*\s*\w\sdelegad[oa]\sde\spolícia\sfederal\s(.+),*\spara\sexercer\so.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_3 and encontrado == False:
                        regex = "regex_nomeacao_tipo_3"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_3.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_3.group(2)

                    regex_nomeacao_tipo_4 = re.search(r"nomear\W*\s*[oa]\sservidora*\s(.+),*\Wmatrícula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_4 and encontrado == False:
                        regex = "regex_nomeacao_tipo_4"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_4.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_4.group(2)

                    regex_nomeacao_tipo_5 = re.search(r"nomear\W*\s*[oa]\sservidora*\s(.+),*\scpf.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_5 and encontrado == False:
                        regex = "regex_nomeacao_tipo_5"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_5.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_5.group(2)

                    regex_nomeacao_tipo_6 = re.search(r"nomear\W*\s*[oa]\s.+federal\sdo\sbrasil\s(.+),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_6 and encontrado == False:
                        regex = "regex_nomeacao_tipo_6"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_6.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_6.group(2)

                    regex_nomeacao_tipo_7 = re.search(r"nomear\W*\s*[oa]\s.+federal\sdra*\W*\s(.+),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_7 and encontrado == False:
                        regex = "regex_nomeacao_tipo_7"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_7.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_7.group(2)

                    regex_nomeacao_tipo_8 = re.search(r"nomear\W*\s*[oa]\s.+federal\ssra*\.*\s(.+),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_8 and encontrado == False:
                        regex = "regex_nomeacao_tipo_8"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_8.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_8.group(2)

                    regex_nomeacao_tipo_9 = re.search(r"nomear\W*\s*[oa]\s.+federal\s(.+),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_9 and encontrado == False:
                        regex = "regex_nomeacao_tipo_9"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_9.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_9.group(2)

                    regex_nomeacao_tipo_10 = re.search(r"nomear\W*\s*[oa]\s.+federal\s(.+),*\spara\so\s.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_10 and encontrado == False:
                        regex = "regex_nomeacao_tipo_10"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_10.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_10.group(2)

                    regex_nomeacao_tipo_11 = re.search(r"nomear\W*\s*(.+)\s\(nr\sord\s\d+\),*\scpf.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_11 and encontrado == False:
                        regex = "regex_nomeacao_tipo_11"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_11.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_11.group(2)

                    regex_nomeacao_tipo_12 = re.search(r"nomear\W*\s*(.+),*\sportador[ao]\sdo\scpf.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_12 and encontrado == False:
                        regex = "regex_nomeacao_tipo_12"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_12.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_12.group(2)

                    regex_nomeacao_tipo_13 = re.search(r"nomear\W*\s*[oa]\ssenhora*\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_13 and encontrado == False:
                        regex = "regex_nomeacao_tipo_13"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_13.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_13.group(2)

                    regex_nomeacao_tipo_14 = re.search(r"nomear\W*\s*(.+),*\scpf.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_14 and encontrado == False:
                        regex = "regex_nomeacao_tipo_14"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_14.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_14.group(2)

                    regex_nomeacao_tipo_15 = re.search(r"nomear\W*\s*[oa]\sarquitet[oa]\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_15 and encontrado == False:
                        regex = "regex_nomeacao_tipo_15"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_15.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_15.group(2)

                    regex_nomeacao_tipo_16 = re.search(r"nomear\W*\s*[oa]\sassistente\stécnico-administrativo\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_16 and encontrado == False:
                        regex = "regex_nomeacao_tipo_16"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_16.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_16.group(2)

                    regex_nomeacao_tipo_17 = re.search(r"nomear\W*\s*[oa]\sanalista\stécnico-administrativo\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_17 and encontrado == False:
                        regex = "regex_nomeacao_tipo_17"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_17.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_17.group(2)

                    regex_nomeacao_tipo_18 = re.search(r"nomear\W*\s*(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_18 and encontrado == False:
                        regex = "regex_nomeacao_tipo_18"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_18.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_18.group(2)

                    regex_nomeacao_tipo_19 = re.search(r"nomear\W*\s*(.+),*\smatr[ií]cula.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_19 and encontrado == False:
                        regex = "regex_nomeacao_tipo_19"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_19.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_19.group(2)

                    regex_nomeacao_tipo_20 = re.search(r"nomear\W*\s*o\scmg\s\(im\)\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_20 and encontrado == False:
                        regex = "regex_nomeacao_tipo_20"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_20.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_20.group(2)

                    regex_nomeacao_tipo_21 = re.search(r"nomear\W*\s*\ba contar de \d+ de \w+ de \d+\b,\s[oa]\s\w+\s\w+\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_21 and encontrado == False:
                        regex = "regex_nomeacao_tipo_21"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_21.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_21.group(2)

                    regex_nomeacao_tipo_22 = re.search(r"nomear\W*\s*[oa]\scel\sinf\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_22 and encontrado == False:
                        regex = "regex_nomeacao_tipo_22"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_22.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_22.group(2)

                    regex_nomeacao_tipo_23 = re.search(r"nomear\W*\s*[oa]\sservidora*\s(.+?),*\ssiape.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_23 and encontrado == False:
                        regex = "regex_nomeacao_tipo_23"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_23.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_23.group(2)

                    regex_nomeacao_tipo_24 = re.search(r"nomear\W*\s*[oa]\ssoldad[oa]\s\(fab\)\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_24 and encontrado == False:
                        regex = "regex_nomeacao_tipo_24"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_24.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_24.group(2)

                    regex_nomeacao_tipo_25 = re.search(r"nomear\W*\s*[oa]\stenente-coronel\saviador\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_25 and encontrado == False:
                        regex = "regex_nomeacao_tipo_25"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_25.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_25.group(2)

                    regex_nomeacao_tipo_26 = re.search(r"nomear\W*\s*(.+?),*\s\(nr\sord\s.+para\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_26 and encontrado == False:
                        regex = "regex_nomeacao_tipo_26"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_26.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_26.group(2)

                    regex_nomeacao_tipo_27 = re.search(r"nomear\W*\s*[oa]\sso-av-cv\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_27 and encontrado == False:
                        regex = "regex_nomeacao_tipo_27"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_27.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_27.group(2)

                    regex_nomeacao_tipo_28 = re.search(r"nomear\W*\s*(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_28 and encontrado == False:
                        regex = "regex_nomeacao_tipo_28"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_28.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_28.group(2)

                    regex_nomeacao_tipo_29 = re.search(r"nomear\W*\s*[oa]\sagente\sadministrativo\s(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_29 and encontrado == False:
                        regex = "regex_nomeacao_tipo_29"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_29.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_29.group(2)

                    regex_nomeacao_tipo_30 = re.search(r"nomear\W*\s*[oa]\scontador\s(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_30 and encontrado == False:
                        regex = "regex_nomeacao_tipo_30"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_30.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_30.group(2)

                    regex_nomeacao_tipo_31 = re.search(r"nomear\W*\s*para\so\scargo\s.+\scódigo\sdas-*(\d+.\d+),\s[oa]\ssra*\.\s(.+),\scpf\s", trecho)

                    if regex_nomeacao_tipo_31 and encontrado == False:
                        regex = "regex_nomeacao_tipo_31"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_31.group(2).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_31.group(1)

                    regex_nomeacao_tipo_32 = re.search(r"nomear\W*\s*para\so\scargo\s.+\scódigo\sdas-*(\d+.\d+),\s.+de\snavegação,\s\d+.\d+.\d+\s(.+),\scpf\s.+", trecho)

                    if regex_nomeacao_tipo_32 and encontrado == False:
                        regex = "regex_nomeacao_tipo_32"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_32.group(2).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_32.group(1)

                    regex_nomeacao_tipo_33 = re.search(r"nomear\W*\s*(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_33 and encontrado == False:
                        regex = "regex_nomeacao_tipo_33"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_33.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_33.group(2)

                    regex_nomeacao_tipo_34 = re.search(r"nomear\W*\s*(.+),*\s[nd]o\scargo.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_34 and encontrado == False:
                        regex = "regex_nomeacao_tipo_34"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_34.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_34.group(2)

                    # parece que não pega nada
                    regex_nomeacao_tipo_35 = re.search(r"nomear\W*\s*(.+?),*\s*para,*\sexercer.+das[\s-](\d+.\d+)", trecho)

                    if regex_nomeacao_tipo_35 and encontrado == False:
                        regex = "regex_nomeacao_tipo_35"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_35.group(1).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_35.group(2)

                    regex_nomeacao_tipo_36 = re.search(r"código\sdas[\s=](\d+.\d+)\se\snomear\s(.+)\spara\s[te]", trecho)

                    if regex_nomeacao_tipo_36 and encontrado == False:
                        regex = "regex_nomeacao_tipo_36"
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_36.group(2).split(",")[0]
                        cargo_simbolo = regex_nomeacao_tipo_36.group(1)

                    if encontrado:
                        count += 1

                    if nome_do_servidor != "":# and regex=="regex_nomeacao_tipo_26":
                        print(str(index) + " - " + regex + " - " + filepath + ": " + nome_do_servidor)

                    #print(str(index) + " - " + regex + " - " + filepath + ": " + nome_do_servidor)

print("Quantidade: " + str(count))
