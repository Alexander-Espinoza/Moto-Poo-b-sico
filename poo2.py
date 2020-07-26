class Moto():
    def __init__(self):
        self.__ruedas=2
        self.__timon=1
        self.largo=10
        self.ancho=0.2
    
    def arrancar(self,encendida,casco,gasolina):
        
        if encendida:
            
            self.encender()
            resultadoTest=self.__testing(casco,gasolina)
            if resultadoTest:
                print("Testing completado. OK!")
            else:
                print("Testing fallido")
        
        else:
            print("Moto apagada")
            print("No se realizará el test")
        
    def encender(self):
        print("Moto encendida")
        return True

    def __testing(self,casco=True,gasolina=False):
        self.casco=casco
        self.gasolina=gasolina

        if(self.casco and self.gasolina):
            return True
        else:
            return False

miMoto=Moto()
miMoto.arrancar(False,False,True)