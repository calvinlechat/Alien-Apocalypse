import pyxel
from random import randint

class Soin:
    def __init__(self):
        
        self.x = randint(0,112)
        self.y = randint(0,112)
        

    def update(self):
        
        pass

    def draw(self):
        pyxel.blt(self.x,self.y,0,41,81,7,5)
        
    
        
class Vaisseau:
    def __init__(self):
        self.vitesse = 1.5
        self.x = 57
        self.y = 80
        self.tirs = []
        self.cooldown = True
        

    def update(self):
        if pyxel.btn(pyxel.KEY_D) and not(self.x >= 112): 
            self.x += self.vitesse
         
        if pyxel.btn(pyxel.KEY_S) and not(self.y >= 114):
            self.y += self.vitesse
            
        if pyxel.btn(pyxel.KEY_Q) and not(self.x <= 0):
            self.x -= self.vitesse
           
        if pyxel.btn(pyxel.KEY_Z) and not(self.y <= -2):
            self.y -= self.vitesse
           
        if self.cooldown == True :
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
                self.tirs.append([self.x + 7 , self.y])
                if len(self.tirs) > 1:
                    del(self.tirs[0])
                self.cooldown = False
        if pyxel.frame_count % 20 == 0 :
            self.cooldown = True
        for x in range(len(self.tirs)):
            if self.tirs[x][1] <= 3:
                del(self.tirs[x])
                break
        for x in range(len(self.tirs)):
            self.tirs[x][1] = (self.tirs[x][1] - 2) % pyxel.height
            

    def draw(self):
        pyxel.blt(self.x, self.y , 0 ,16, 8, 16, 16, 5)
        for tir in range(len(self.tirs)) :
            pyxel.blt(self.tirs[tir][0] - 7, self.tirs[tir][1] - 12, 0, 32, 120, 16 , 16 , 5)  
        

class App:
    def __init__(self):
        pyxel.init(128,128, title="ndc",quit_key = pyxel.KEY_P)
        pyxel.load("1.pyxres")
        self.aliens = []
        self.compteur_mechants = 0
        self.score = 0
        self.tirs = []
        self.vaisseau = Vaisseau()
        self.mode = 1
        self.cooldown_monstre = True
        self.PV = 10
        self.PV_Terre = 20
        self.Etat_vie = True
        self.cooldown_soin = True
        self.soin = Soin()
        pyxel.run(self.update, self.draw)
       


    def update(self):
        if pyxel.frame_count % (120 / self.mode) == 0 :
            self.aliens.append([randint(0, 112), 0])
            self.compteur_mechants += 1
            if self.score >= 10 :
                self.mode = 2
            if self.score >= 25 :
                self.mode = 3
            if self.score >= 50 : 
                self.mode = 4
            if self.score >= 100 :
                self.mode = 5
        if pyxel.frame_count % 400 == 0 :
            self.cooldown_soin = True
            self.soin.x = randint(0,112)
            self.soin.y = randint(0,112)
        if pyxel.frame_count % 80 == 0 :
            self.cooldown_monstre = True
        
        for x in range(self.compteur_mechants):
            
            if self.cooldown_monstre == True:
                if ((self.aliens[x][1] - self.vaisseau.y < 10) and (self.aliens[x][1] - self.vaisseau.y > -10)) and ((self.aliens[x][0] - self.vaisseau.x < 10) and (self.aliens[x][0] - self.vaisseau.x > -10)): 
                    self.PV = self.PV - 1
                    self.cooldown_monstre = False
            if self.aliens[x][1] == 124 :
                del(self.aliens[x])
                self.compteur_mechants -= 1
                self.PV_Terre -= 1 
                break
            self.aliens[x][1] = (self.aliens[x][1] + 1) % pyxel.height
        for x in range(len(self.aliens)):
            for tir in range(len(self.vaisseau.tirs)):
                if (self.aliens[x][0] <= self.vaisseau.tirs[tir][0] and self.aliens[x][0] + 12 >= self.vaisseau.tirs[tir][0] and self.aliens[x][1] <= self.vaisseau.tirs[tir][1] and self.aliens[x][1] + 12 >= self.vaisseau.tirs[tir][1]) :
                    del(self.aliens[x])
                    del(self.vaisseau.tirs[tir])
                    self.compteur_mechants -= 1
                    self.score  += 1
                    break
                
      
        if self.cooldown_soin == True:
            if ((self.soin.x - self.vaisseau.x < 10) and (self.soin.x - self.vaisseau.x > -10)) and ((self.soin.y - self.vaisseau.y < 10) and (self.soin.y - self.vaisseau.y > -10)):
                self.PV = self.PV + 1
                self.cooldown_soin = False
                
                
        if self.cooldown_soin == False:
                self.soin.x = 1000
                self.soin.y = 1000
        
        if self.PV < 1 or self.PV_Terre < 1:
            self.Etat_vie = False
            self.score_final = self.score
        
        # vaisseau
        self.vaisseau.update()

                
        
    
            

    def draw(self):
        if self.Etat_vie == True:
            pyxel.bltm(0,0,0,0,0,128,128,6)
            for x in range(self.compteur_mechants):
                if self.mode == 1 :
                    pyxel.blt(self.aliens[x][0], self.aliens[x][1], 0, 0, 40, 16, 16, 5)
                elif self.mode == 2 :
                    pyxel.blt(self.aliens[x][0], self.aliens[x][1], 0, 16, 40, 16, 16, 5)
                elif self.mode == 3 :
                    pyxel.blt(self.aliens[x][0], self.aliens[x][1], 0, 32, 40, 16, 16, 5)
                elif self.mode == 4 :
                    pyxel.blt(self.aliens[x][0], self.aliens[x][1], 0, 0, 56, 16, 16, 5)
                elif self.mode == 5 :
                    pyxel.blt(self.aliens[x][0], self.aliens[x][1], 0, 16, 56, 16, 16, 5)
                
            pyxel.text(104, 3, "Score:\n" + str(self.score), 7)
            pyxel.text(3,3, "PV:" + str(self.PV),7)
            pyxel.text(3,10, "PV TERRE:" + str(self.PV_Terre),7)
            self.vaisseau.draw()
            self.soin.draw()
        else:
            pyxel.cls(0)
            pyxel.text(45,50,"GAME OVER",7)
            pyxel.text(35,65,"Score final : " + str(self.score_final),7)
       
        
App()