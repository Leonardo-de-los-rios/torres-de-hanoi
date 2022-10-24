from claseNodo import Nodo

class PilaEncadenada:
    __tope=None
    __cantidad=0

    def __init__(self):
        self.__tope=None

    def crear(self):
        self.__cantidad=0

    def inicializar(self,cantidad): # inicializo de mayor a menor, p ej. [3,2,1]
        aux=cantidad
        for i in range(cantidad):
            self.insertar(aux)
            aux-=1

    def insertar(self,elemento):
        nodo=Nodo(elemento)
        nodo.setSiguiente(self.__tope)
        self.__tope=nodo
        self.__cantidad+=1

    def suprimir(self):
        if self.esVacia():
            print('La pila está vacía.')
        else:
            aux=self.__tope.getDato()
            self.__tope=self.__tope.getSiguiente()
            self.__cantidad-=1
            return aux

    def esVacia(self):
        return self.__cantidad == 0

    def esMenor(self, num):
        if self.__cantidad == 0 or (num < self.getNumero()): # verifico si la pila está vacía o el numero es menor que el ultimo que tiene en la pila
            return True
        else:
            return False

    def mostrarDatos(self):
        s=''
        if self.esVacia() == False:
            lista=[]
            aux=self.__tope
            while aux != None:
                lista.insert(0,aux.getDato()) # colocar los números de forma decreciente
                aux=aux.getSiguiente()
            for i in range(len(lista)):
                s+=f'{lista[i]} '
        return s

    def getCantidad(self):
        return self.__cantidad

    def getNumero(self):
        aux=self.__tope
        while aux!=None:
            ant=aux
            aux=aux.getSiguiente()
        return ant.getDato()