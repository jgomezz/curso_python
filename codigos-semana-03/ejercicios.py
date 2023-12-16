
class Auto:
    
    def __init__(self, color1, marca1, anho1) :
        self.color = color1
        self.marca = marca1
        self.anho = anho1

    """
    Crear un metodo que me imprima la marca y el anho del auto
    """
    def imprimir_info(self):

        print("La marca es " , self.marca , " y el anho es " , self.anho)


    """
    Crear un metodo imprimir() que me imprima los 3 atributos de la clase
    """


auto_toyota =  Auto("Blanco","Toyota",2020)

print(auto_toyota.color)
print(auto_toyota.marca)
print(auto_toyota.anho)

print(auto_toyota.imprimir_info())



auto_nissan =  Auto("Negro","Nissan",2021)

print(auto_nissan.color)
print(auto_nissan.marca)
print(auto_nissan.anho)

print(auto_nissan.imprimir_info()) 


exit(-1)

"""
Agregar el color y la marca en la clae Auto, y pasarselo por el constructor.

"""