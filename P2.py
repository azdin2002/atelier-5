class Vecteur2D:

    def __init__(self, x0=0, y0=0):  #Constructeur avec parametres par defaut.
       
    
        self.x = x0 # initialisation de x et y, attributs d'instance
        self.y = y0
    def __add__(self, autre):
    
        return Vecteur2D(self.x+autre.x, self.y+autre.y)
    def __str__(self):
   
       return "Vecteur({:g}, {:g})".format(self.x, self.y)
   
   
v1, v2 = Vecteur2D(4.5, 2), Vecteur2D(1, 4.5)
print(v1)
print(v2)
print(v1 + v2)




