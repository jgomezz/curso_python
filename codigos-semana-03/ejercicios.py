
class Auto:
    
    def __init__(self, color1, marca1, anho1) :
        self.color = color1
        self.marca = marca1
        self.anho = anho1
        self.garantia = 1  # Garantia del auto

    """
    Crear un metodo que me imprima la marca y el anho del auto
    """
    def imprimir_info(self):

        print("La marca es " , self.marca , " y el anho es " , self.anho)


    """
    Crear un metodo imprimir() que me imprima los 3 atributos de la clase
    """
    def imprimir(self):
        print("La marca es " , self.marca , ", el anho es " , 
              self.anho , " y  el color ", self.color)


    """
    Crear un metodo obtener_info() que obtenga el marca y la color del auto
    """
    def obtener_info(self):
        return self.marca +  "|" +  self.color



auto_toyota =  Auto("Blanco","Toyota",2020)

print(auto_toyota.color)
print(auto_toyota.marca)
print(auto_toyota.anho)
auto_toyota.imprimir_info()
auto_toyota.imprimir()

r = auto_toyota.obtener_info()
print(r)


auto_nissan =  Auto("Negro","Nissan",2021)
print(auto_nissan.color)
print(auto_nissan.marca)
print(auto_nissan.anho)
auto_nissan.imprimir_info() 
auto_nissan.imprimir()

r = auto_nissan.obtener_info()
print(r)



"""
Crear un objeto llamado auto_mazda  y le agregas la marca, el color y el anho

"""


"""
Crear un metodo para incrementar la garantia de un auto, se pasara la canitdad de amhos a incrementar

auto_nissan.incrementar_garantia(2)

"""



exit(-1)

"""
Agregar el color y la marca en la clae Auto, y pasarselo por el constructor.

"""