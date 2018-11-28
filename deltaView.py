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
activeLayer = 0
activeLvl = ""
activeRotation = 0
activeFlipX = False
activeFlipY = False
activeFileLocation = ""
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
    activeMap = deltaTile.addMapCoord(activeMap,nX,nY,activeKey,activeRotation,activeFlipX,activeFlipY)

    
def program():
    print("Hey. You are using DeltaTile.")
    print("DeltaTile is a free extension for pygame.")
    print("You can use this for your projects under the MIT License.")
    print("DeltaTile is created by SkyanSam. The owner of Skylark Studios.")
    print("Type in the file location you wish to open. [.deltalvl files]")
    
    ans = input("")
    load_file = open(ans, 'r')
    game_data = load_file.read
    load_file.close()
    
    global activeFileLocation
    activeFileLocation = ans
    
    return game_data

def endSave():
    print("Thanks for using DeltaTile!")
    
    global activeFileLocation
    save_file = open(activeFileLocation, 'w')
    save_file.write(game_data)
    save_file.close()    
    
def update():
    pygame.event.get()
    global x
    global y
    global activeKey
    global activeMap
    x3 = x
    y3 = y
    
    print(activeKey)
    
    # BG
    screen.fill((0,0,0))
    
    # Tilemap
    deltaTile.drawLevel(screen,activeLvl,x,y,activeLayer)
    
    # ActiveMap Update
    if activeLayer != "spritemap" and activeLayer != "boundarymap" and activeLayer != "all":
        activeMap = activeLvl.split('|')[activeLayer]
    
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
    if keys[pygame.K_LSHIFT] and keys[pygame.K_a]:
        activeLayer = "all"
    elif keys[pygame.K_a]:
        activeKey = 'A'
    
    if keys[pygame.K_LSHIFT] and keys[pygame.K_b]:
        activeLayer = "boundarymap"
    elif keys[pygame.K_b]:
        activeKey = 'B'
    
    if keys[pygame.K_LSHIFT] and keys[pygame.K_s]:
        activeLayer = "spritemap"
    elif keys[pygame.K_s]:
        activeKey = 'S'
            
    if keys[pygame.K_c]:
        activeKey = 'C'
    if keys[pygame.K_d]:
        activeKey = 'D'
    if keys[pygame.K_e]:
        activeKey = 'E'
    if keys[pygame.K_f]:
        activeKey = 'F'
    if keys[pygame.K_g]:
        activeKey = 'G'
    if keys[pygame.K_h]:
        activeKey = 'H'
    if keys[pygame.K_i]:
        activeKey = 'I'
    if keys[pygame.K_j]:
        activeKey = 'J'
    if keys[pygame.K_k]:
        activeKey = 'K'
    if keys[pygame.K_l]:
        activeKey = 'L'
    if keys[pygame.K_m]:
        activeKey = 'M'
    if keys[pygame.K_n]:
        activeKey = 'N'
    if keys[pygame.K_o]:
        activeKey = 'O'
    if keys[pygame.K_p]:
        activeKey = 'P'
    if keys[pygame.K_q]:
        activeKey = 'Q'
    if keys[pygame.K_r]:
        activeKey = 'R'
    if keys[pygame.K_t]:
        activeKey = 'T'
    if keys[pygame.K_u]:
        activeKey = 'U'
    if keys[pygame.K_v]:
        activeKey = 'V'
    if keys[pygame.K_w]:
        activeKey = 'W'
    if keys[pygame.K_x]:
        activeKey = 'X'
    if keys[pygame.K_y]:
        activeKey = 'Y'
    if keys[pygame.K_z]:
        activeKey = 'Z'    
    
    if keys[pygame.K_1]:
        activeLayer = 0
    if keys[pygame.K_2]:
        activeLayer = 1
    if keys[pygame.K_3]:
        activeLayer = 2
    if keys[pygame.K_4]:
        activeLayer = 3
    if keys[pygame.K_5]:
        activeLayer = 4
    if keys[pygame.K_6]:
        activeLayer = 5
    if keys[pygame.K_7]:
        activeLayer = 6
    if keys[pygame.K_8]:
        activeLayer = 7
    if keys[pygame.K_9]:
        activeLayer = 8
    if keys[pygame.K_0]:
        activeLayer = 9    
      
    print(activeMap)
        
    
    
    
    # Mouse Click
    mse = pygame.mouse.get_pressed()
    if mse[0]:
        clickToPlace()
    
        
    
    
        
            
    

# deltaTile.drawTiles(deltaTile.mapp1,0,0,20,"tilepacks/pfc/")
# pygame.display.update()
# ui.dialouge(screen,"resources/font.ttf",18,"Hey there.&*IMMA EAT YOU ALIVE!!!!&*Looks like it worked! :)")



activeLvl = program()

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

