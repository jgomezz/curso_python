class Auto:
    
    ciudad = "Lima"

    def __init__(self, color1, marca1, anho1) :
        self.color = color1
        self.marca = marca1
        self.anho = anho1
        self.garantia = 1  # Garantia del auto

    def imprimir_info(self):
        print("La marca es " , self.marca , " y el anho es " , self.anho)

    def imprimir(self):
        print("La marca es " , self.marca , ", el anho es " , 
              self.anho , " y  el color ", self.color)

    def obtener_info(self):
        return self.marca +  "|" +  self.color

    def incrementar_garantia(self, extra_garantia):  
        self.garantia += extra_garantia         
        if self.ciudad == "Lima" and self.garantia > 2:  
            self.garantia = 2 
    
    @classmethod
    def modificar_ciudad(cls, nueva_ciudad):
        cls.ciudad =  nueva_ciudad



