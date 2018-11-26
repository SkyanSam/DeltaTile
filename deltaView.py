import pygame
import pygame_functions
import deltaBase as deltaTile
import deltaXtras as ui
import os
from array import *

def clr():    
    os.system('cls' if os.name == 'nt' else 'clear')

""" Make it so that there is rotation options. FIX DELTATILES.DRAWTILES to work with 0.0.0 and also
have access and key shortcuts to layers.. and add more keys for active keys"""
fontt = "resources/font.ttf"
activeKey = 'A'
activeMap = ""
activeLvl = ""
fps = 60
x = 0
y = 0
size = 50
speed = 1
run = False

class col:
    white = (255,255,255)
    black = (0,0,0)
    gray = (100,100,100)

def clickToPlace():
    global x
    global y
    global activeMap
    global activeKey
    
    pygame.event.get()
    pos = pygame.mouse.get_pos()
    nX = round((pos[0]/size)+x)
    nY = round((pos[1]/size)+y)
    global activeMap
    activeMap = deltaTile.addMapCoord(activeMap,nX,nY,activeKey)

    
def program():
    print("Hey. You are using DeltaTile.")
    print("DeltaTile is a free extension for pygame.")
    print("You can use this for your projects under the MIT License.")
    print("DeltaTile is created by SkyanSam. The owner of Skylark Studios.")
    print("Type in the file location you wish to open. [.deltalvl files]")
    
    ans = input("")
    load_file = open(ans + ".deltalvl", 'r')
    game_data = load_file.read
    load_file.close()    
    
    
    
def update():
    pygame.event.get()
    global x
    global y
    global activeKey
    x3 = x
    y3 = y
    
    print(activeKey)
    
    # BG
    screen.fill((0,0,0))
    
    # Tilemap
    if deltaTile.mapType == "spritemap":
        deltaTile.drawTiles(screen,activeMap,x3,y,size,deltaTile.tileLoc)
    elif deltaTile.mapType == "boundarymap":
        deltaTile.drawTilesBound(screen,activeMap,x3,y,size,deltaTile.tileLoc)
    
    # Selector
    pos = pygame.mouse.get_pos()
    nX = round((pos[0]/size)+x3)*size
    nY = round((pos[1]/size)+y3)*size    
    pygame.draw.rect(screen,col.white,(nX,nY,size,size),1)
    
    # Events
    
    keys = pygame.key.get_pressed()
    
    # Movement
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_UP]:
        y -= speed
    
    # Active Keys
    if keys[pygame.K_a]:
        activeKey = 'A'
    if keys[pygame.K_b]:
        activeKey = 'B'
    if keys[pygame.K_c]:
        activeKey = 'C'
    
    print(activeMap)
        
    
    
    
    # Mouse Click
    mse = pygame.mouse.get_pressed()
    if mse[0]:
        clickToPlace()
    
        
    
    
        
            
    

# deltaTile.drawTiles(deltaTile.mapp1,0,0,20,"tilepacks/pfc/")
# pygame.display.update()
# ui.dialouge(screen,"resources/font.ttf",18,"Hey there.&*IMMA EAT YOU ALIVE!!!!&*Looks like it worked! :)")



programStart2()

pygame.init()
pygame.display.set_caption("DeltaTile Editor")
screen = pygame.display.set_mode((800,600))

pygame.display.update() 
run = True
while run:
    update()
    pygame.time.delay(round(1000 / fps))
    # update()
    # draw.main()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
    
    # Quit Key
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT] and keys[pygame.K_q]:
        pygame.quit()
        endSave()    

