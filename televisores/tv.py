class TV:
    __numTv = 0

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__estado = estado
        self.__volumen = 1
        self.__control = None
        
        TV.__numTv += 1

    #get & set methods

    def getMarca(self):
        return self.__marca
    
    def setMarca(self, name):
        self.__marca = name
    
    def getControl(self):
        return self.__control
    
    def setControl(self, newControl):
        self.__control = newControl
    
    def getPrecio(self):
        return self.__precio
    
    def setPrecio(self, price):
        self.__precio = price

    def getVolumen(self):
        return self.__volumen
    
    def setVolumen(self, newVolumen):
        if newVolumen >= 0 and newVolumen<=7 and self.__estado==True:
            self.__volumen = newVolumen
    
    def getCanal(self):
        return self.__canal
    

    def setCanal(self, channel):
        if channel >= 1 and channel <= 120 and self.__estado==True:
            self.__canal = channel

    @classmethod
    def getNumTV(cls):
        return cls.__numTv
    
    @classmethod
    def setNumTV(cls, cantidad):
        cls.__numTv = cantidad

    def turnOn(self):
        self.__estado = True
    
    def turnOff(self):
        self.__estado = False

    def getEstado(self):
        return self.__estado
    
    def canalUp(self):
        if self.__estado==True and self.__canal<120:
            self.__canal += 1
    
    def canalDown(self):
        if self.__estado==True and self.__canal>1:
            self.__canal -= 1
    
    def volumenUp(self):
        if self.__estado==True and self.__volumen<7:
            self.__volumen += 1
    
    def volumenDown(self):
        if self.__estado==True and self.__volumen>0:
            self.__volumen -= 1