class Auto:
    
    def __init__(self, color, marca, anho, ciudad) :
        self.marca = marca
        self.color = color
        self.anho = anho
        self.garantia = 1  # Garantia del auto
        self.ciudad = ciudad

    def imprimir_info(self):
        print("La marca es " , self.marca , " y el anho es " , self.anho)

    def imprimir(self):
        print("La marca es " , self.marca , ", el anho es " , 
              self.anho , " y  el color ", self.color)

    def incrementar_garantia(self, extra_garantia):  
        self.garantia += extra_garantia         
        if self.ciudad == "Lima" and self.garantia > 2:  
            self.garantia = 2 
    
auto_hyundai = Auto("Blanco","Hyundai","2022","Lima" )

auto_hyundai.imprimir_info()