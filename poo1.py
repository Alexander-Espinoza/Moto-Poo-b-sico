class Coche():

    def __init__(self):
        self.__argoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar (self,arrParo=True,gasolina="ok",aceite="ok",puertas="cerradas"):
        self.gasolina=gasolina
        self.aceite=aceite
        self.puertas=puertas
        self.__enmarcha=arrParo
        if self.__enmarcha:
            self.chequeo=self.__chequeoInterno()
            print("El coche está encendido")
        else:
            print("El coche está apagado")
            
        self.estado()
    
    def estado(self):
        if (self.__enmarcha and self.chequeo):
            print("Se realizó el chequeo. OK!")
            print("El coche está en marcha")
        elif (self.__enmarcha and self.chequeo==False):
            print("No podemos arrancar, testeo fallido")
        
    
    def caracteristicas(self):
        print("El coche tiene {} ruedas".format(self.__ruedas))

    def __chequeoInterno(self):

        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True

        else:
            return False

miCoche=Coche()
miCoche.arrancar(True,'ok','ok','abiertas')

print("HOLA GIT")
print("-------------------------------------------------")
miCoche2=Coche()
miCoche2.arrancar()

