import csv
import xmltodict
import os
import re

count = 0
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
            texto_da_portaria = ato["xml"]["article"]["body"]["Texto"]

            quantidade_de_nomeacoes = texto_da_portaria.upper().count("NOMEAR")
            cargo_em_comissao = texto_da_portaria.upper().find("DAS 1") or texto_da_portaria.upper().find("DAS-1")

            if quantidade_de_nomeacoes == 1 and cargo_em_comissao > 0:

                for trecho in texto_da_portaria.split("</p>"):

                    regex_nomeacao_tipo_1 = re.search(r"NOMEAR\<\/strong\>\<\/p\>\<p\>(.+)\spara\sexercer\so\scargo\sde\s(.+)\W\scódigo\s(.+)\W\s\w+\s(.+)\W\<\/p\>\<p\s", texto_da_portaria)

                    if regex_nomeacao_tipo_1:
                        #count += 1
                        encontrado = True
                        nome_do_servidor = regex_nomeacao_tipo_1.group(1)
                        cargo_titulo = regex_nomeacao_tipo_1.group(2)
                        cargo_simbolo = regex_nomeacao_tipo_1.group(3)
                        cargo_lotacao = regex_nomeacao_tipo_1.group(4)

                    regex_nomeacao_tipo_2 = re.search(r"NOMEAR\<\/strong\>\<\/p\>\<p\>(.+),\s.+\W\smatrícula\sSiape\snº\s\d+,\spara\sexercer\so\scargo\sem\scomissão\sde\s(.+),\scódigo\s(.+)\(\d+\),\sda\s(.+),\sficando", texto_da_portaria)

                    if regex_nomeacao_tipo_2 and encontrado == False:
                        encontado = True
                        #count += 1
                        nome_do_servidor = regex_nomeacao_tipo_2.group(1)
                        cargo_titulo = regex_nomeacao_tipo_2.group(2)
                        cargo_simbolo = regex_nomeacao_tipo_2.group(3)
                        cargo_lotacao = regex_nomeacao_tipo_2.group(4)

                    regex_nomeacao_tipo_3 = re.search(r"Nomear\s(.+)\W\smatrícula\sn\W\s.+\W\sCPF\s.+\W\spara\sexercer\so\scargo\sem\scomissão\sde\s(.+)\W\scódigo\s(.+)\W\sda\s(.+)\W\<\/p\>", texto_da_portaria)

                    if regex_nomeacao_tipo_3 and encontrado == False:
                        encontado = True
                        #count += 1
                        nome_do_servidor = regex_nomeacao_tipo_3.group(1)
                        cargo_titulo = regex_nomeacao_tipo_3.group(2)
                        cargo_simbolo = regex_nomeacao_tipo_3.group(3)
                        cargo_lotacao = regex_nomeacao_tipo_3.group(4)

                if encontrado:
                    count += 1
                print(filepath + ": " + nome_do_servidor)

print("Quantidade: " + str(count))
