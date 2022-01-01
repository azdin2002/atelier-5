class etudiant:
     def __init__(self,nom , prenom, age , cne , moyenne):

      self.nom= nom  
      self.prenom= prenom 
      self.age= age 
      self.cne= cne 
      self.moyenne= moyenne 
     def __repr__(self):
      return repr((self.nom , self.prenom, self.age , self.cne , self.moyenne))
  
#creation une liste de type étudiant.
listEetudient = []
e1 = etudiant("azzeddine", "salmoun", 20,"E1", 15)
e2 = etudiant("Brahim " , "Adouli" ,24 , "E2", 18)
e4 = etudiant("Fatima", "Ben Nasser", 19 ,"E4", 14)

listEetudient.append(e1) 
listEetudient.append(e2) 
listEetudient.append(e4)

#triee selon l'age 
List_age = sorted(listEetudient, key=lambda etudiant: etudiant.age)   
print("la liste triee selon l'age :",List_age)
#triee selon moyenne
List_moyenne = sorted(listEetudient, key=lambda etudiant: etudiant.moyenne)  
print("la liste triee selon le moyenne:",List_moyenne)
