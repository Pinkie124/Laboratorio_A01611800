def leerExcel(archivo):
    import csv
    filas = []
    with open(archivo, 'r') as file:
        leer = csv.reader(file)
        for lista in leer:
            filas.append(lista)
    return filas

archivo = "avocado.csv"
filas = leerExcel(archivo)
