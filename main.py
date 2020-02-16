# Numero de dias vividos 8023

"""def practica(i):
    switcher={
        0: 'Buscaminas\n',
        1: 'Gato Dummy\n',
        2: 'Memoria\n'
    }
    return switcher.get(i,"no hay ejercicio asignado\n")
dias=8023 #dias vividos
print ("Toca realizar el ejercicio ",dias%3,": ", practica(dias%3))  """


# REALIZAR GATO DUMMY
#CREANDO MATRIZ
def matrizP():
    filas=["1","2","3"];
    columnas=["A","B","C"];
    alto = len(filas) + 1
    largo=len(columnas)+1;
    matriz=[]
    for i in range(alto):  # ALTO
        matriz.append([])
        for j in range(largo):  # LARGO
            matriz[i].append(" ")
    """alto = n
    largo = n
    matriz = []
    for i in range(alto):  # ALTO
        matriz.append([])
        for j in range(largo):  # LARGO
            matriz[i].append(" ")"""
    return generarMatrizInicial(matriz,filas,columnas)

#GENERAR LINEAS DEL PRIMER CUADRANTE
def generarMatrizInicial(matriz,filas,columnas):
    print("alto=", len(matriz))
    print("largo=", len(matriz[0]))
    for i in range(len(matriz)):  # ALTO
        for j in range(len(matriz[0])):  # LARGO
            if i is 0:
                if j is 0:
                    matriz[i][j]=" "
                else:
                    matriz[i][j] = columnas[j-1]
            else:
                if j is 0:
                    matriz[i][j]=filas[i-1]
                else:
                    matriz[i][j]="-"
    return matriz
    """"" alto=len(matriz)
    largo=len(matriz[0])
    for i in range(alto):  # ALTO
        for j in range(largo):  # LARGO
            if j is 0:
                matriz[i][j] = chr(65 + i)
            else:
                for j in range(largo):  # LARGO
                    matriz[i][j] = "-"" """


def verMatriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):  # LARGO
            print(matriz[i][j],"\n")

matriz=matrizP()
verMatriz(matriz)