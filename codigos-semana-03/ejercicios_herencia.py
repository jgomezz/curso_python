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
        if self.ciudad == "Lima" and self.garantia > 2  :  
            self.garantia = 2 

# Crear clase hija
            
class SUV (Auto) :

    def __init__(self, color, marca, anho, ciudad, capacidad) :
        super().__init__(color, marca, anho, ciudad)
        self.capacidad = capacidad

    def imprimir_info(self):
        print("La marca es " , self.marca , 
              " , el anho es " , self.anho, 
              " , el color es " , self.color,
              " y tiene una capacidad de " , self.capacidad , " personas")

class SEDAN (Auto) :
    pass

class VAN (Auto) :
    def __init__(self, color, marca, anho, ciudad, propietario):
        super().__init__(color, marca, anho, ciudad)
        self.propietario = propietario

    def imprimir_info(self):
        print("La marca es " , self.marca , 
              " , el anho es " , self.anho, 
              " , el color es " , self.color,
              " y el propietario es  " ,self.propietario)


auto_hyundai = Auto("Blanco","Hyundai","2022","Lima" )

auto_hyundai.imprimir_info()


suv_hyundai = SUV("Negro","Hyundai","2023","Arequipa",6)

suv_hyundai.imprimir_info()


sedan_hyundai = SEDAN("Negro","Hyundai","2023","Nazca" )

sedan_hyundai.imprimir_info()


van_hyundai = VAN("Negro","Hyundai","2023","Arequipa", "Jaime GOmez" )

van_hyundai.imprimir_info()


""" 
Modificar la clase SUV, SEDAN o VAN para que me imprime  
marca , anho y color al momento de usar el metodo imprimir_info()

"""

