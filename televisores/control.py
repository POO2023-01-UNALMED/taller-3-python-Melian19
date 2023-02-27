class Control:

    def __init__(self):
        self.__tv = None

    def getTv(self):
        return self.__tv
    
    def setTv(self, television):
        self.__tv = television

    def turnOn(self):
        self.__tv.turnOn()

    def turnOff(self):
        self.__tv.turnOff()

    def canalUp(self):
        self.__tv.canalUp()
    
    def canalDown(self):
        self.__tv.canalDown()
    
    def volumenUp(self):
        self.__tv.volumenUp()
    
    def volumenDown(self):
        self.__tv.volumenDown()
    
    def setCanal(self, number):
        self.__tv.setCanal(number)
    
    def enlazar(self, television):
        self.__tv.setControl(self)
        self.__tv = television


        
