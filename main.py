'''Ejercicio Nº2:
Realizar un programa que simule el juego de las torres de Hanoi.
El juego de las tres torres de Hanoi consiste en una configuración de tres pilas numeradas como 1, 2 y 3, con
‘n’ discos de tamaño creciente. Los discos se representarán mediante enteros. Los discos más grandes utilizarán valores mayores y los discos más pequeños valores menores.
El objetivo del juego es trasladar los discos de la pila 1, a la pila 3, usando la pila 2 como auxiliar. Para realizar este traslado se deben cumplir siempre los siguientes requisitos:
a) Sólo se puede mover una pieza cada vez; y para tomar una segunda pieza se debe dejar primero la anterior en alguna torre.
b) Sólo puede apilar una pieza encima de una más grande.
Se deberá ingresar el número de discos con el que se va a jugar y mostrar por pantalla el estado inicial del juego (todas las piezas colocadas en la pila 1 y las pilas 2 y 3 vacías).
A partir de ahí, pedirá sucesivamente pares de números indicando la pila origen desde la que tomará la pieza y la pila destino a la que se quiere realizar el movimiento. El programa 
analizará si la jugada es factible. Si el resultado del análisis es positivo moverá la ficha de una pila a otra. Si no lo es indicará que es una jugada imposible, indicando el por qué 
y pedirá un nuevo movimiento.
El juego terminará cuando las pilas 1 y 2 estén vacías y todos los discos se encuentren en la pila 3, mostrando el número de jugadas realizadas y el número mínimo de jugadas (2n–1) en el 
que se podría haber realizado.
                    MÉTODO CON PILA ENCADENADA
'''

import math

import os

from clasePilaEncadenada import PilaEncadenada

def hanoi(pila1,pila2,pila3):
    continuar=True
    origen=-1
    movimientos=0
    while continuar and origen!=0:
        os.system ('cls')
        print('\t\tTORRES DE HANÓI:\n')
        print(f'Movimientos: {movimientos}.')
        mostrarPilas(pila1,pila2,pila3)
        origen=input('Pila Origen (1,2,3, 0 para salir): ')
        try:
            origen=int(origen)
            if 1<=origen<=3:
                destino=input('Pila Destino (1,2,3): ')
                try:
                    destino=int(destino)
                    if origen == destino:
                        print('No se puede elegir la misma pila de origen y destino.')
                    elif 1<=destino<=3:
                        movimientos+=1
                        if origen==1:
                            if pila1.getCantidad()==0: # verificamos que la pila está vacía. Si es -1, está vacía
                                print(f'No tiene discos la PILA {origen}.')
                            else:
                                disco=pila1.suprimir()
                                if destino == 3:
                                    if pila3.esMenor(disco):
                                        pila3.insertar(disco)
                                    else:
                                        pila1.insertar(disco)
                                        print('Sólo puede apilar una pieza encima de una más grande.')
                                else:
                                    if pila2.esMenor(disco):
                                        pila2.insertar(disco)
                                    else:
                                        pila1.insertar(disco)
                                        print('Sólo puede apilar una pieza encima de una más grande.')
                        elif origen==2:
                            if pila2.getCantidad()==0:
                                print(f'No tiene discos la PILA {origen}.')
                            else:
                                disco=pila2.suprimir()
                                if destino == 3:
                                    if pila3.esMenor(disco):
                                        pila3.insertar(disco)
                                        if pila1.getCantidad()==0 and pila2.getCantidad()==0:
                                            continuar=False
                                    else:
                                        pila2.insertar(disco)
                                        print('Sólo puede apilar una pieza encima de una más grande.')
                                else:
                                    if pila1.esMenor(disco):
                                        pila1.insertar(disco)
                                    else:
                                        pila2.insertar(disco)
                                        print('Sólo puede apilar una pieza encima de una más grande.')
                        else:
                            if pila3.getCantidad()==0:
                                print(f'No tiene discos la PILA {origen}.')
                            else:
                                disco=pila3.suprimir()
                                if destino == 1:
                                    if pila1.esMenor(disco):
                                        pila1.insertar(disco)
                                    else:
                                        pila3.insertar(disco)
                                        print('Sólo puede apilar una pieza encima de una más grande.')
                                else:
                                    if pila2.esMenor(disco):
                                        pila2.insertar(disco)
                                    else:
                                        pila3.insertar(disco)
                                        print('Sólo puede apilar una pieza encima de una más grande.')
                        if pila1.getCantidad()==0 and pila2.getCantidad()==0: # verificamos si se terminó el juego
                            continuar=False
                    else:
                        print('No ingresó un número del 1 al 3.')
                    input ('Presiona ENTER para continuar...')
                except ValueError:
                    print('No ingresó un número.')
            elif origen==0: # cuando sale
                os.system ('cls')
                print('Hasta la próxima!!')
            else:
                print('No ingresó un número del 1 al 3.')
        except ValueError:
            print('No ingresó un número.')
    if origen != 0: # cuando ganó
        os.system ('cls')
        print('\t\tTORRES DE HANÓI:\n')
        print('FELICITACIONES HAS COMPLETADO EL JUEGO!!\n')
        mov_minimos=math.pow(2,num)-1
        print(f'Movimientos: {movimientos}. Fuiste: {100-(movimientos*100/mov_minimos)+100:.2f}% eficiente. Movimientos mínimos: {int(mov_minimos)}.')
        mostrarPilas(pila1,pila2,pila3)
        input ('Presiona ENTER para continuar...')
    
def mostrarPilas(pila1,pila2,pila3):
    for i in range(3):
        s=''
        s=f'Pila {i+1}: '
        if i==0:
            s+=pila1.mostrarDatos()
        elif i==1:
            s+=pila2.mostrarDatos()
        else:
            s+=pila3.mostrarDatos()
        print(s)
    print('------------------------------------------')

if __name__ == '__main__':
    '''pila=PilaEncadenada()
    pila.crear()
    pila.inicializar(5)

    print(pila.mostrarDatos())

    for i in range(5):
        print(pila.suprimir)
'''

    continuar=True
    while continuar:
        os.system('cls')
        print('\t\tTORRES DE HANÓI:\n')
        num=input('Ingrese la cantidad de discos: ')
        try:
            num=int(num)
            if num > 0:
                pila1=PilaEncadenada() # num es la dimensión de la pila
                pila1.crear()
                pila2=PilaEncadenada()
                pila2.crear()
                pila3=PilaEncadenada()
                pila3.crear()
                pila1.inicializar(num)
                hanoi(pila1,pila2,pila3)
                continuar=False
            else:
                print('\nTiene que tener al menos 1 disco.')
                input ('Presiona ENTER para continuar...')
        except ValueError:
            print('No ingresó un número.')