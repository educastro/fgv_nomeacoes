import os

outputfile = open("todos_os_filiados_do_brasil.csv","w")
count = 1

for filename in os.listdir(r"C:\Users\eduar\Downloads\partidos"):

# first file:
    if count == 1:
        print("iniciando " + filename)

        secondaryfile = open("partidos/" + filename)

        for line in secondaryfile:
             outputfile.write(line)
        secondaryfile.close() # not really needed

        print("finalizando " + filename)
    else:
        print("iniciando " + filename)

        secondaryfile = open("partidos/" + filename)
        next(secondaryfile) # skip the header
        for line in secondaryfile:
             outputfile.write(line)
        secondaryfile.close() # not really needed

        print("finalizando " + filename)

    count += 1

outputfile.close()
