# -*- coding: utf-8 -*-
import csv
import xmltodict
import os
import re

count = 0
count_global = 0
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

                    if ("NOMEAR" in texto_da_portaria) and ("DAS 1" in texto_da_portaria or "DAS-1" in texto_da_portaria) and (tipo_da_portaria != "Retificação"):
                        for trecho in texto_da_portaria.split("NOMEAR"):
                            count_global += 1
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

                            regex_nomeacao_tipo_2 = re.search(r"nomear\W*\s*\w\s\d\w\s\w+\s(.+?),*\spara\sexercer\s.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_2 and encontrado == False:
                                regex = "regex_nomeacao_tipo_2"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_2.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_2.group(2)

                            regex_nomeacao_tipo_3 = re.search(r"nomear\W*\s*\w\sdelegad[oa]\sde\spolícia\sfederal\s(.+?),*\spara\sexercer\so.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_3 and encontrado == False:
                                regex = "regex_nomeacao_tipo_3"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_3.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_3.group(2)

                            regex_nomeacao_tipo_4 = re.search(r"nomear\W*\s*[oa]*\sservidora*,*\s(.+?),*\Wmatrícula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_4 and encontrado == False:
                                regex = "regex_nomeacao_tipo_4"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_4.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_4.group(2)

                            regex_nomeacao_tipo_5 = re.search(r"nomear\W*\s*[oa]*\sservidora*\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_5 and encontrado == False:
                                regex = "regex_nomeacao_tipo_5"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_5.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_5.group(2)

                            regex_nomeacao_tipo_6 = re.search(r"nomear\W*\s*[oa]*\s.+federal\ssra*\.*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_6 and encontrado == False:
                                regex = "regex_nomeacao_tipo_6"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_6.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_6.group(2)

                            regex_nomeacao_tipo_7 = re.search(r"nomear\W*\s*[ao]\sservidora*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_7 and encontrado == False:
                                regex = "regex_nomeacao_tipo_7"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_7.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_7.group(2)

                            regex_nomeacao_tipo_8 = re.search(r"nomear\s(.+?),\scpf\sn.\s\d+.\d+.\d+.\d+,\sservidor\sdo\squadro.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_8 and encontrado == False:
                                regex = "regex_nomeacao_tipo_8"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_8.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_8.group(2)

                            regex_nomeacao_tipo_9 = re.search(r"nomear\W*\s*(.+?),*\s*agente\sfederal\s.+,\smatrícula:.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_9 and encontrado == False:
                                regex = "regex_nomeacao_tipo_9"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_9.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_9.group(2)

                            regex_nomeacao_tipo_10 = re.search(r"nomear\W*\s*[oa]\sdefensora*\spúblic[ao]\sfederal\sd*r*a*\W*\s(.+?),*\s*para\so\s.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_10 and encontrado == False:
                                regex = "regex_nomeacao_tipo_10"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_10.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_10.group(2)

                            regex_nomeacao_tipo_11 = re.search(r"nomear\W*\s*[oa]*\s.+federal\sdo\sbrasil\saposentada\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_11 and encontrado == False:
                                regex = "regex_nomeacao_tipo_11"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_11.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_11.group(2)

                            regex_nomeacao_tipo_12 = re.search(r"nomear\W*\s*[oa]*\s.+federal\sdo\sbrasil\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_12 and encontrado == False:
                                regex = "regex_nomeacao_tipo_12"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_12.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_12.group(2)

                            regex_nomeacao_tipo_13 = re.search(r"nomear\W*\s*[oa]*\s.+federal\sdra*\W*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_13 and encontrado == False:
                                regex = "regex_nomeacao_tipo_13"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_13.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_13.group(2)

                            regex_nomeacao_tipo_14 = re.search(r"nomear\W*\s*[oa]*\s.+federal\sdo\sbrasil,*\s(.+?),*\smatrícula.+\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_14 and encontrado == False:
                                regex = "regex_nomeacao_tipo_14"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_14.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_14.group(2)

                            regex_nomeacao_tipo_15 = re.search(r"nomear\W*\s*(.+?)\W*\sauditora*-*fiscal\sda\sreceita\sfederal\sdo.+matrícula.+matrícula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_15 and encontrado == False:
                                regex = "regex_nomeacao_tipo_15"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_15.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_15.group(2)

                            regex_nomeacao_tipo_16 = re.search(r"nomear\W*\s*[oa]*\s.+federal\ss*r*a*\.*\s(.+?),*\spara\so\s.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_16 and encontrado == False:
                                regex = "regex_nomeacao_tipo_16"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_16.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_16.group(2)

                            regex_nomeacao_tipo_17 = re.search(r"nomear\W*\s*[oa]*\s.+federal\ss*r*a*\.*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_17 and encontrado == False:
                                regex = "regex_nomeacao_tipo_17"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_17.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_17.group(2)

                            regex_nomeacao_tipo_18 = re.search(r"nomear\W*\s*(.+?),*\sagente\sfederal.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_18 and encontrado == False:
                                regex = "regex_nomeacao_tipo_18"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_18.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_18.group(2)

                            regex_nomeacao_tipo_19 = re.search(r"nomear\W*\s*[oa]*\s.+federal\s(.+?),*\spara\so\s.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_19 and encontrado == False:
                                regex = "regex_nomeacao_tipo_19"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_19.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_19.group(2)

                            regex_nomeacao_tipo_20 = re.search(r"nomear\W*\s*(.+?)\s\(nr\sord\s\d+\),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_20 and encontrado == False:
                                regex = "regex_nomeacao_tipo_20"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_20.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_20.group(2)

                            regex_nomeacao_tipo_21 = re.search(r"nomear\W*\s*(.+?),*\sportador[ao]\sdo\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_21 and encontrado == False:
                                regex = "regex_nomeacao_tipo_21"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_21.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_21.group(2)

                            regex_nomeacao_tipo_22 = re.search(r"nomear\W*\s*[oa]*\ssenhora*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_22 and encontrado == False:
                                regex = "regex_nomeacao_tipo_22"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_22.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_22.group(2)

                            regex_nomeacao_tipo_23 = re.search(r"nomear\W*\s*[oa]*\ssenhora*\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_23 and encontrado == False:
                                regex = "regex_nomeacao_tipo_23"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_23.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_23.group(2)

                            regex_nomeacao_tipo_24 = re.search(r"nomear\W*\s*[oa]*\sprofessora*\sdo\smagistério\ssuperior,*\smatrícula\ssiape\s\d+,*\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_24 and encontrado == False:
                                regex = "regex_nomeacao_tipo_24"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_24.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_24.group(2)

                            regex_nomeacao_tipo_25 = re.search(r"nomear\W*\s*a\spartir\sde\s\d+\sde\s\w+\sde\s\d+\W*(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_25 and encontrado == False:
                                regex = "regex_nomeacao_tipo_25"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_25.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_25.group(2)

                            regex_nomeacao_tipo_26 = re.search(r"nomear\W*\s*a\spartir\sde\s\d+\sde\s\w+\sde\s\d+\W*\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_26 and encontrado == False:
                                regex = "regex_nomeacao_tipo_26"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_26.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_26.group(2)

                            regex_nomeacao_tipo_27 = re.search(r"nomear\W*\s*a\spartir\sde\s\d+\sde\s\w+\W*\s(.+?)\W*\smatrícula\ssiape.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_27 and encontrado == False:
                                regex = "regex_nomeacao_tipo_27"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_27.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_27.group(2)

                            regex_nomeacao_tipo_28 = re.search(r"nomear\W*\s*a\spartir\sde\s\d.\sde\s\w+\sde\s\d+,\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_28 and encontrado == False:
                                regex = "regex_nomeacao_tipo_28"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_28.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_28.group(2)

                            regex_nomeacao_tipo_29 = re.search(r"nomear\W*\s*[oa]*\stécnic[oa]\sem\sassuntos\seducacionais,*\s\d+.\d+.\d+,\smatrícula\ssiape\s\d+,\s(.+?),*\scpf\s.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_29 and encontrado == False:
                                regex = "regex_nomeacao_tipo_29"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_29.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_29.group(2)

                            regex_nomeacao_tipo_30 = re.search(r"nomear\W*\s*[oa]*\stécnico\sem\sassuntos\seducacionais\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_30 and encontrado == False:
                                regex = "regex_nomeacao_tipo_30"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_30.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_30.group(2)

                            regex_nomeacao_tipo_31 = re.search(r"nomear\W*\s*[oa]*\sagente\sadministrativo,*\s\d+.\d+.\d+,*\smatrícula\ssiape\s\d+,*\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_31 and encontrado == False:
                                regex = "regex_nomeacao_tipo_31"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_31.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_31.group(2)

                            regex_nomeacao_tipo_32 = re.search(r"nomear\W*\s*[oa]*\sprocuradora*\sfederal\s(.+?),*\s*matrícula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_32 and encontrado == False:
                                regex = "regex_nomeacao_tipo_32"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_32.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_32.group(2)

                            regex_nomeacao_tipo_33 = re.search(r"nomear\W*\s*a\s\w+,\s\d+.\d+.\d+,\smatrícula\ssiape\s\d+,\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_33 and encontrado == False:
                                regex = "regex_nomeacao_tipo_33"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_33.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_33.group(2)

                            regex_nomeacao_tipo_34 = re.search(r"nomear\W*\s*[oa]*\ssra*.\s(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_34 and encontrado == False:
                                regex = "regex_nomeacao_tipo_34"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_34.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_34.group(2)

                            regex_nomeacao_tipo_35 = re.search(r"nomear\W*\s*(.+?),*\scpf.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_35 and encontrado == False:
                                regex = "regex_nomeacao_tipo_35"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_35.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_35.group(2)

                            regex_nomeacao_tipo_36 = re.search(r"nomear\W*\s*[oa]*\sanalista\sdo\sseguro\ssocial\s(.+?),*\s*matrícula\ssiape.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_36 and encontrado == False:
                                regex = "regex_nomeacao_tipo_36"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_36.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_36.group(2)

                            regex_nomeacao_tipo_37 = re.search(r"nomear\W*\s*[oa]*\sarquitet[oa]\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_37 and encontrado == False:
                                regex = "regex_nomeacao_tipo_37"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_37.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_37.group(2)

                            regex_nomeacao_tipo_38 = re.search(r"nomear\W*\s*[oa]*\sassistente\stécnic[ao]-*administr*ativo\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_38 and encontrado == False:
                                regex = "regex_nomeacao_tipo_38"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_38.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_38.group(2)

                            regex_nomeacao_tipo_39 = re.search(r"nomear\W*\s*[oa]*\sanalista\stécnic[oa]-*\s*administrativo\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_39 and encontrado == False:
                                regex = "regex_nomeacao_tipo_39"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_39.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_39.group(2)

                            regex_nomeacao_tipo_40 = re.search(r"nomear\W*\s*[oa]*\stécnic[oa]\sdo\sseguro\ssocial\s(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_40 and encontrado == False:
                                regex = "regex_nomeacao_tipo_40"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_40.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_40.group(2)

                            regex_nomeacao_tipo_41 = re.search(r"nomear\W*\s*(.+?),*\smatr[íi]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_41 and encontrado == False:
                                regex = "regex_nomeacao_tipo_41"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_41.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_41.group(2)

                            regex_nomeacao_tipo_42 = re.search(r"nomear\W*\s*(.+?),*\smatr[ií]cula.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_42 and encontrado == False:
                                regex = "regex_nomeacao_tipo_42"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_42.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_42.group(2)

                            regex_nomeacao_tipo_43 = re.search(r"nomear\W*\s*o\scmg\s\(im\)\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_43 and encontrado == False:
                                regex = "regex_nomeacao_tipo_43"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_43.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_43.group(2)

                            regex_nomeacao_tipo_44 = re.search(r"nomear\W*\s*\ba contar de \d+ de \w+ de \d+\b,\s[oa]*\s\w+\s\w+\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_44 and encontrado == False:
                                regex = "regex_nomeacao_tipo_44"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_44.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_44.group(2)

                            regex_nomeacao_tipo_45 = re.search(r"nomear\W*\s*[oa]*\scel\sinf*t*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_45 and encontrado == False:
                                regex = "regex_nomeacao_tipo_45"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_45.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_45.group(2)

                            regex_nomeacao_tipo_46 = re.search(r"nomear\W*\s*[oa]*\sservidora*\s(.+?),*\ssiape.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_46 and encontrado == False:
                                regex = "regex_nomeacao_tipo_46"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_46.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_46.group(2)

                            regex_nomeacao_tipo_47 = re.search(r"nomear\W*\s*[oa]*\ssoldad[oa]\s\(fab\)\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_47 and encontrado == False:
                                regex = "regex_nomeacao_tipo_47"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_47.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_47.group(2)

                            regex_nomeacao_tipo_48 = re.search(r"nomear\W*\s*[oa]*\stenente-coronel\saviador\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_48 and encontrado == False:
                                regex = "regex_nomeacao_tipo_48"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_48.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_48.group(2)

                            regex_nomeacao_tipo_49 = re.search(r"nomear\W*\s*(.+?),*\s\(nr\sord\s.+para\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_49 and encontrado == False:
                                regex = "regex_nomeacao_tipo_49"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_49.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_49.group(2)

                            regex_nomeacao_tipo_50 = re.search(r"nomear\W*\s*[oa]*\scontra\salmirante\s\(im\)\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_50 and encontrado == False:
                                regex = "regex_nomeacao_tipo_50"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_50.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_50.group(2)

                            regex_nomeacao_tipo_51 = re.search(r"nomear\W*\s*[oa]*\sso-av-[mc]v\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_51 and encontrado == False:
                                regex = "regex_nomeacao_tipo_51"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_51.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_51.group(2)

                            regex_nomeacao_tipo_52 = re.search(r"nomear\W*\s*[oa]*\scoronel\saviador\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_52 and encontrado == False:
                                regex = "regex_nomeacao_tipo_52"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_52.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_52.group(2)

                            regex_nomeacao_tipo_53 = re.search(r"nomear\W*\s*[oa]*\sbrigadeiro\sdo\sar\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_53 and encontrado == False:
                                regex = "regex_nomeacao_tipo_53"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_53.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_53.group(2)

                            regex_nomeacao_tipo_54 = re.search(r"nomear\W*\s*[oa]*\scoronel\sqmb\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_54 and encontrado == False:
                                regex = "regex_nomeacao_tipo_54"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_54.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_54.group(2)

                            regex_nomeacao_tipo_55 = re.search(r"nomear\W*\s*[oa]*\scapitã[oa]\sde\smar\se\sguerra\s\(im\)\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_55 and encontrado == False:
                                regex = "regex_nomeacao_tipo_55"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_55.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_55.group(2)

                            regex_nomeacao_tipo_56 = re.search(r"nomear\W*\s*[oa]*\spolicial\s\w+\sfederal\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_56 and encontrado == False:
                                regex = "regex_nomeacao_tipo_56"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_56.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_56.group(2)

                            regex_nomeacao_tipo_57 = re.search(r"nomear\W*\s*[oa]\sperit[oa]*\s\w+\sfederal\s(.+?),*\s*para\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_57 and encontrado == False:
                                regex = "regex_nomeacao_tipo_57"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_57.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_57.group(2)

                            regex_nomeacao_tipo_58 = re.search(r"nomear\W*\s*[oa]*\s\d.\ssg-*el\s(.+?),*\s*para\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_58 and encontrado == False:
                                regex = "regex_nomeacao_tipo_58"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_58.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_58.group(2)

                            regex_nomeacao_tipo_59 = re.search(r"nomear\W*\s*[oa]*\s\d.\ssgt\sqe\s(.+?),*\s*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_59 and encontrado == False:
                                regex = "regex_nomeacao_tipo_59"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_59.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_59.group(2)

                            regex_nomeacao_tipo_60 = re.search(r"nomear\W*\s*[oa]\scapitão*\sq*a*o*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_60 and encontrado == False:
                                regex = "regex_nomeacao_tipo_60"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_60.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_60.group(2)

                            regex_nomeacao_tipo_61 = re.search(r"nomear\W*\s*[oa]\scabo\s\(fab\)\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_61 and encontrado == False:
                                regex = "regex_nomeacao_tipo_61"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_61.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_61.group(2)

                            regex_nomeacao_tipo_62 = re.search(r"nomear\W*\s*[oa]*\scel\sa*r*t*\s(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_62 and encontrado == False:
                                regex = "regex_nomeacao_tipo_62"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_62.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_62.group(2)

                            regex_nomeacao_tipo_63 = re.search(r"nomear\W*\s*(.+?),*\spara\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_63 and encontrado == False:
                                regex = "regex_nomeacao_tipo_63"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_63.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_63.group(2)

                            regex_nomeacao_tipo_64 = re.search(r"nomear\W*\s*[oa]*\sagente\sadministrativo\s(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_64 and encontrado == False:
                                regex = "regex_nomeacao_tipo_64"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_64.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_64.group(2)

                            regex_nomeacao_tipo_65 = re.search(r"nomear\W*\s*[oa]*\sagente\sde\stelecomunicação\se\seletricidade\s(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_65 and encontrado == False:
                                regex = "regex_nomeacao_tipo_65"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_65.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_65.group(2)

                            regex_nomeacao_tipo_66 = re.search(r"nomear\W*\s*[oa]*\scontador\s(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_66 and encontrado == False:
                                regex = "regex_nomeacao_tipo_66"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_66.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_66.group(2)

                            regex_nomeacao_tipo_67 = re.search(r"nomear\W*\s*para\so\scargo\s.+\scódigo\sdas[\s-](\d+.\d+),\s[oa]*\ssra*\.\s(.+?),\scpf\s", trecho)

                            if regex_nomeacao_tipo_67 and encontrado == False:
                                regex = "regex_nomeacao_tipo_67"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_67.group(2).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_67.group(1)

                            # Não ta pegando
                            regex_nomeacao_tipo_68 = re.search(r"nomear\W*\s*para\so\scargo\s.+\scódigo\sdas[\s-](\d+.\d+),\s.+de\snavegação,\s\d+.\d+.\d+\s(.+?),\scpf\s.+", trecho)

                            if regex_nomeacao_tipo_68 and encontrado == False:
                                regex = "regex_nomeacao_tipo_68"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_68.group(2).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_68.group(1)

                            regex_nomeacao_tipo_69 = re.search(r"nomear\W*\s*(.+?),*para\so\scargo.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_69 and encontrado == False:
                                regex = "regex_nomeacao_tipo_69"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_69.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_69.group(2)

                            regex_nomeacao_tipo_70 = re.search(r"nomear\W*\s*(.+?),*\s[nd]o\scargo.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_70 and encontrado == False:
                                regex = "regex_nomeacao_tipo_70"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_70.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_70.group(2)

                            # parece que não pega nada
                            regex_nomeacao_tipo_71 = re.search(r"nomear\W*\s*(.+?),*\s*para,*\sexercer.+das[\s-](\d+.\d+)", trecho)

                            if regex_nomeacao_tipo_71 and encontrado == False:
                                regex = "regex_nomeacao_tipo_71"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_71.group(1).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_71.group(2)

                            regex_nomeacao_tipo_72 = re.search(r"código\sdas[\s-](\d+.\d+)\se\snomear\s(.+?)\spara\s[te]", trecho)

                            if regex_nomeacao_tipo_72 and encontrado == False:
                                regex = "regex_nomeacao_tipo_72"
                                encontrado = True
                                nome_do_servidor = regex_nomeacao_tipo_72.group(2).split(",")[0]
                                cargo_simbolo = regex_nomeacao_tipo_72.group(1)

                            if encontrado:
                                count += 1

                            if regex == "":
                                print(str(index) + " - " + regex + " - " + endereco_do_arquivo + ": " + nome_do_servidor)

                            #writer.writerow([nome_do_servidor, cargo_simbolo, titulo_da_portaria, data_da_portaria, link_da_portaria])

    print("Quantidade: " + str(count))
    print("Quantidade Global: " + str(count_global))
    arquivo_de_saida.close()
