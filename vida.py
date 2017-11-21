#-*- coding: utf-8 -*-

class Vida(object):
    """Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva).
    Una célula viva con 2 ó 3 células vecinas vivas sigue viva, en otro caso muere o permanece muerta (por "soledad" o "superpoblación")."""
    
    def __init__(self, p):
        self.punto = p
        self.vida = False
        #print(self.punto)
       
         
    def nacerMorir(self):
        pass
                    
    
    def change(self):
        pass 
    
    def select():
        pass    
    
    
    def show(self):
        scl = 20
        noStroke()
        if self.vida:
            fill(255)
        else:
            fill(0)

        rect(self.punto.x * scl, self.punto.y * scl, scl, scl)