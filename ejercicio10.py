class Atleta: 

 def __init__(self, nombre, apellido, altura, peso, telefono): 
    self.nombre = nombre
    self.apellido = apellido 
    self.altura = altura 
    self.__peso = peso
    self.__telefono = telefono 

 def get_altura(self): 
    return self.__altura 

 def get_peso(self): 
    return self.__peso 

 def get_telefono(self): 
    return self.__telefono 

 def set_altura(self, altura): 
    self.__altura = altura 

 def set_peso(self, peso): 
    self.__peso = peso 

 def set_telefono(self, telefono): 
    self.__telefono = telefono 

 def __str__(self): 
    return "Atleta: " + self.nombre + " " + self.apellido 
    
                      