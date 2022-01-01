#Classe avec constructeur.

class Vecteur2D:
       
        def __init__(self, x0=0, y0=0):
            #  Constructeur avec parametres par defaut.
                self.x = x0 # initialisation de x et y, attributs d'instance
                self.y = y0
               
        def affiche(self):
                return "x = %d, y = %d" % (self.x,self.y)
              

if __name__ == '__main__':
        print(" une instance par defaut ".center(50, '-'))
        v1 =  Vecteur2D()
        print ("x = %g, y = %g" % (v1.x, v1.y))
        #--
        print(" une instance initialisee ".center(50, '-'))
        v2=Vecteur2D(-5.2, 4.1)
        v2.affiche()
        print ("x = %g, y = %g" % (v2.x, v2.y))