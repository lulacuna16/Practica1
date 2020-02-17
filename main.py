# Numero de dias vividos 8023
from random import randint, uniform,random
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


def matrizP(): #Tablero Principiante
    filas=["1","2","3"];
    columnas=["A","B","C"];
    alto = len(filas) + 1
    largo=len(columnas)+1;
    matriz=[]
    for i in range(alto):  # ALTO
        matriz.append([])
        for j in range(largo):  # LARGO
            matriz[i].append(" ")
    return generarMatrizInicial(matriz,filas,columnas)

def matrizA(): #Tablero avanzado
    filas=["1","2","3","4","5"];
    columnas=["A","B","C","D","E"];
    alto = len(filas) + 1
    largo=len(columnas)+1;
    matriz=[]
    for i in range(alto):  # ALTO
        matriz.append([])
        for j in range(largo):  # LARGO
            matriz[i].append(" ")
    return generarMatrizInicial(matriz,filas,columnas)

def generarMatrizInicial(matriz,filas,columnas):
    #print("alto=", len(matriz))
    #print("largo=", len(matriz[0]))
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


def verMatriz(matriz):
    alto = len(matriz)
    largo = len(matriz[0])
    for i in range(alto):
        for j in range(largo):  # LARGO
            print(matriz[i][j], "\t", end=" ")
        print()
def menu():
    Salir=False
    while  Salir==False :
        print("\tElige una dificultad\t")
        print("1. Principiante")
        print("2. Avanzado")
        print("3. Salir")
        case=int(input("Opcion: "))
        if case == 1:
            matrizp=matrizP()
            verMatriz(matrizp)
            jugar(matrizp)
        if case == 2:
            matriza=matrizA()
            verMatriz(matriza)
            jugar(matriza)
        if case == 3:
            Salir = True

def colocar(matriz,sim):
    cont=0
    while cont==0:
        pos = str(input("Ingrese una coordenada (Ej. 1A,2C): "))
        fila = int(pos[0])
        col = ord(pos[1]) - 64
        #print(fila, ",", col)
        for i in range (len(matriz)):
            if i==fila:
                for j in range (len(matriz[0])):
                    if j==col:
                        if matriz[i][j]=="-":
                            matriz[i][j]=sim
                            cont+=1
                            verMatriz(matriz)
                        else:
                            print("Casilla Ocupada")

                    elif col<=0 or col>=len(matriz[0]):
                        print("Columna Invalida")
                        break;
            elif fila <= 0 or fila >= len(matriz):
                print("Fila Invalida")
                break;
def juegoAuto(matriz,sim):
    cont=0
    while cont==0:
        fila = randint(1,len(matriz)-1)
        col = randint(65,65+(len(matriz)-2))-64#COdigo ascii desde A hasta el tamaño de la matriz
        #print("Elegi Casilla:", fila, ",", col)
        for i in range (len(matriz)):
            if i==fila:
                for j in range (len(matriz[0])):
                    if j==col:
                        if matriz[i][j]=="-":
                            print("Elegi Casilla:",fila,",",col)
                            matriz[i][j]=sim
                            cont+=1
                            verMatriz(matriz)
                        #else:
                            #print("Casilla Ocupada")

                    elif col<=0 or col>=len(matriz[0]):
                        #print("Columna Invalida")
                        break;
            elif fila <= 0 or fila >= len(matriz):
                #print("Fila Invalida")
                break;

def ganarH(matriz,sim):
    cont=0
    for i in range (1,len(matriz)):
        cont=0
        for j in range(1,len(matriz[0])):
            if matriz[i][j]==sim:
                cont+=1
                if cont is (len(matriz)-1):
                    return 1
                    break;
def ganarV(matriz,sim):
    cont=0
    for j in range (1,len(matriz[0])):
        cont=0
        for i in range(1,len(matriz)):
            if matriz[i][j]==sim:
                cont+=1
                if cont is (len(matriz)-1):
                    return 1
                    break;
def jugar(matriz):
    simJ="x"
    simS="o"
    cont=0
    print("Jugador es: ", simJ)
    print("Maquina es: ", simS)
    long=(len(matriz)-1)*(len(matriz)-1)
    while cont<long:
        print("TURNO JUGADOR\n")
        colocar(matriz,simJ)
        if ganarH(matriz,simJ) is 1:
            print("Gano JUGADOR")
            break;
        if ganarV(matriz, simJ) is 1:
            print("Gano JUGADOR")
            break;
        cont+=1;
        if cont>=long:
            print("Juego Terminado: EMPATE")
            break
        print("TURNO MAQUINA\n")
        juegoAuto(matriz,simS)
        if ganarH(matriz,simS) is 1:
            print("Gano MAQUINA")
            break;
        if ganarV(matriz, simS) is 1:
            print("Gano MAQUINA")
            break;
        cont+=1
        if cont>=long:
            print("Juego Terminado: EMPATE")
            break


menu()
   ## return switch.get(case, "Dificultad no establecida\n")


