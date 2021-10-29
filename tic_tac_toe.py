#Creado por Jaime Pardo 24.10.2021
#requisito inicial que la maquina coloque la X en el centro del tablero.
#primer git
#C:\Users\jdpm2\OneDrive\Escritorio\Github\tic _tac_toe.py
#Nuevo comentario random
import random
f1 = [1,2,3]
f2 = [4,5,6]
f3 = [7,8,9,]
lt = [f1,f2,f3]
def dibujaTablero():
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",lt[0][0],"  |  ",lt[0][1],"  |  ",lt[0][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",lt[1][0],"  |  ",lt[1][1],"  |  ",lt[1][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|  ",lt[2][0],"  |  ",lt[2][1],"  |  ",lt[2][2],"  |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

def jugadaSkynet(i):
    if i == 0:
        lt[1][1] = "X"
    else:
        for a in range(9):
            a = random.randrange(10)
            if a in f1:
                lt[0][a-1] = "X"
                return True
            elif a in f2:
                lt[1][(a-1)-3] = "X"
                return True
            elif a in f3:
                lt[2][(a-1)-6] = "X"
                return True

def jugadaSara(jug):
    if jug in f1:
        lt[0][jug-1] = "O"
        return True
    elif jug in f2:
        lt[1][(jug-1)-3] = "O"
        return True
    elif jug in f3:
        lt[2][(jug-1)-6] = "O"
        return True
    else:
        return False

def fin():
    if lt[0][0] == "O" and lt[0][1] == "O" and lt[0][2] == "O":
        result = 1
        return result
    if lt[1][0] == "O" and lt[1][1] == "O" and lt[1][2] == "O":
        result = 1
        return result
    if lt[2][0] == "O" and lt[2][1] == "O" and lt[2][2] == "O":
        result = 1
        return result

    if lt[0][0] == "O" and lt[1][0] == "O" and lt[2][0] == "O":
        result = 1
        return result
    if lt[0][1] == "O" and lt[1][1] == "O" and lt[2][1] == "O":
        result = 1
        return result
    if lt[0][2] == "O" and lt[1][2] == "O" and lt[2][2] == "O":
        result = 1
        return result

    if lt[0][0] == "X" and lt[0][1] == "X" and lt[0][2] == "X":
        result = 2
        return result
    if lt[1][0] == "X" and lt[1][1] == "X" and lt[1][2] == "X":
        result = 2
        return result
    if lt[2][0] == "X" and lt[2][1] == "X" and lt[2][2] == "X":
        result = 2
        return result

    if lt[0][0] == "X" and lt[1][0] == "X" and lt[2][0] == "X":
        result = 2
        return result
    if lt[0][1] == "X" and lt[1][1] == "X" and lt[2][1] == "X":
        result = 2
        return result
    if lt[0][2] == "X" and lt[1][2] == "X" and lt[2][2] == "X":
        result = 2
        return result
    if lt[0][0] == "X" and lt[1][1] == "X" and lt[2][2] == "X":
        result = 2
        return result
    if lt[0][2] == "X" and lt[1][1] == "X" and lt[2][0] == "X":
        result = 2
        return result


print("Skynet a hecho su primera jugada, observa (°)(°)")
jugadaSkynet(0)
dibujaTablero()
juego = True
while juego:
    valido = False
    while valido == False:
        O = int(input("Selecciona un numero de casilla para poner tu 'O' :"))
        valido = jugadaSara(O)
        if valido == False:
            print("Casillero ocupado, reintenta")
        dibujaTablero()
    print("Juega Skynet")
    jugadaSkynet(1)
    dibujaTablero()
    re = fin()
    if re == 1:
        print("+----------------------------------------------------------+")
        print("| Has derrotado a Skynet, salvaste al mundo Sara O'Connor. |")
        print("+----------------------------------------------------------+")
        break
    elif re == 2:
        print("+-----------------------------------------------------------------------+")
        print("| Skynet acabo contigo y ahora destruira al mundo, saludame al creador. |")
        print("+-----------------------------------------------------------------------+")
        break
print("fin del juego")
