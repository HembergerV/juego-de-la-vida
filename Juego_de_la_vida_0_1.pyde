from vida import Vida

game = []
d = False
scl = 20
images = 0

def setup():
    global game, scl
    
    frameRate(6)
    size(1000, 800)
            
    for i in range(width / scl):
        game.append([])
        
        for j in range(height / scl):
            game[i].append(Vida(PVector(i, j)))



def draw():
    global game, scl, d, images
    
    clear()
    background(51)
    
    
                
    for i in range(width / scl):
        for j in range(height / scl):
            game[i][j].change()
            game[i][j].show()
        
    if d:    
        images += 1
        nacerVivir()
        
    
    textMode(CENTER)
    textSize(18)
    fill(100)
    text("Images " + str(images), 15, 20) 
    text("Play/Stop(P)", width - 130, 20) 

def keyPressed():
    global game, d
    
    if key == "p":
        d = not d

                
def nacerVivir():
    global game, scl
    
    juicio = []
    
    for row in range(width / scl):
        for column in range(height / scl): 
            #print("asdad")
            vivas = 0
            muertas = 0
            
            
            
            for x in range(row - 1, row + 2):
                for y in range(column - 1, column + 2):
                    if x < 0 or y < 0:
                        continue
            
                    if x > width / scl - 1 or y > height / scl - 1:
                        continue
                    
                    if x != row or y != column:
                        if game[x][y].vida:
                            vivas += 1
                        else:
                            muertas += 1

            #print vivas,muertas
            if game[row][column].vida:
                if vivas == 3 or vivas == 2:
                    juicio.append(True)
                else:
                    juicio.append(False)
            else:
                if vivas == 3:
                    juicio.append(True)
                else:
                    juicio.append(False)
    

    ind = 0
    for row in range(width / scl):
        for column in range(height / scl):
            game[row][column].vida = juicio[ind]
            ind += 1 
            
def mousePressed():
    global game
    
    for i in range(width / scl):
        for j in range(height / scl):
            if floor(mouseX / scl) == game[i][j].punto.x and floor(mouseY / scl) == game[i][j].punto.y:
                game[i][j].vida = not game[i][j].vida