class Ventana:
    __Titulo=None
    __SupxI=None
    __SupYI=None
    __InfxD=None
    __InfYD=None
    def __init__(self,Cadena,Infx=100,InfY=100,Supx=100,SupY=100):
        if(type(Cadena)==str):
            self.__Titulo=Cadena
            self.__InfxD=int(Supx)
            self.__InfYD=int(SupY)
            self.__SupxI=int(Infx)
            self.__SupYI=int(InfY)
        else:
            print("Error al cargar el titulo")

    def mostrar(self):
        print(self.__Titulo,self.__SupxI,self.__SupYI,self.__InfxD,self.__InfYD)

    def getTitulo(self):
        return self.__Titulo

    def alto(self):
        return (self.__SupYI,self.__InfYD)

    def ancho(self):
        return (self.__SupxI,self.__InfxD)

    def moverDerecha(self,Num=1):
        auxI=self.__SupxI+int(Num)
        auxD=self.__InfxD+int(Num)
        if((auxI >=0)&(auxD<=500)&(self.__SupYI<self.__InfYD)&(self.__SupxI<self.__InfxD)):
            self.__SupxI=auxI
            self.__InfxD=auxD
    def moverIzquierda(self,Num=1):
        auxI=self.__SupxI-int(Num)
        auxD=self.__InfxD-int(Num)
        if((auxI >=0)&(auxD<=500)&(self.__SupYI<self.__InfYD)&(self.__SupxI<self.__InfxD)):
            self.__SupxI=auxI
            self.__InfxD=auxD

    def bajar(self, Num=1):
        auxI=self.__SupYI+int(Num)
        auxD=self.__InfYD+int(Num)
        if((auxI >=0)&(auxD<=500)&(self.__SupYI<self.__InfYD)&(self.__SupxI<self.__InfxD)):
            self.__SupYI=auxI
            self.__InfYD=auxD

    def subir(self, Num=1):
        auxI=self.__SupYI-int(Num)
        auxD=self.__InfYD-int(Num)
        if((auxI >=0)&(auxD<=500)&(self.__SupYI<self.__InfYD)&(self.__SupxI<self.__InfxD)):
            self.__SupYI=auxI
            self.__InfYD=auxD
