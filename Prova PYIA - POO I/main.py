class Animal:
    def falar(self):
        print("Este animal faz um som genérico.") 

class Cachorro:
    def falar(self):
        print("O cachorro está latindo.") 

class Gato:
    def falar(self):
        print("O gato está miando.") 
        
animal1 = Animal()
cachorro1 = Cachorro()
gato1 = Gato()


animal1.falar()
cachorro1.falar()
gato1.falar()