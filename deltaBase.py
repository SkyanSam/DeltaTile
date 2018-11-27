import pygame
pygame.init()
tileLoc = "tilepacks/aqua/"
mapType = "spritemap"

def drawLevel(screenn,level,x,y,action):
    layers = level.split('| ')
    if action == "all":
        i = 0
        while i < len(layers):
            mappSplit = layers[i].split('; ')
            if mappSplit[2] == "spritemap":
                drawTiles(screenn,layers[i],x,y)
            elif mappSplit[2] == "boundarymap":
                drawTilesBound(screen,layers[i],x,y)
            i += 1
    elif action == "spritemap":
        i = 0
        while i < len(layers):
            mappSplit = layers[i].split('; ')
            if mappSplit[2] == "spritemap":
                drawTiles(screenn,layers[i],x,y)
            i += 1
    elif action == "boundarymap":
        i = 0
        while i < len(layers):
            mappSplit = layers[i].split('; ')
            if mappSplit[2] == "boundarymap":
                drawTilesBound(screen,layers[i],x,y)            
            i += 1
    else:
        i = action
        if layers[i].split('; ')[2] == "boundarymap":
            drawTilesBound(screen,layers[i],x,y)
        elif layers[i].split('; ')[2] == "spritemap":
            drawTiles(screen,layers[i],x,y)
        

def drawTiles(screenn,mapp,x,y):
    mappList = getMapList(mapp)
    mappData = getMapData(mapp)
    
    folder = mapp.split(': ')[3]
    size = int(mapp.split(': ')[4])
    y2 = 0
    while (y2 < getMapSize(mapp)[1]):
        x2 = 0
        while (x2 < getMapSize(mapp)[0]):
            char = getMapCoords(mapp,x2,y2)
            if char != "0":
                img = getDataSprite(char[0],mapp)
                if img != "0":
                    newImage = pygame.image.load(folder + img)
                    newImage = pygame.transform.rotate(newImage, int(char[1]))
                    newImage = pygame.transform.flip(newImage,bool(char[2]),bool(char[3]))
                    screenn.blit(newImage,(size,size),((x2*size)+x,(y2*size)+y))
            x2 += 1
        y2 += 1

def drawTilesBound(screenn,mapp,x,y):
    mappList = getMapList(mapp)
    mappData = getMapData(mapp)
    color = mapp.split(': ')[3]
    
    size = int(mapp.split(': ')[4])
    y2 = 0
    while (y2 < getMapSize(mapp)[1]):
        x2 = 0
        while (x2 < getMapSize(mapp)[0]):
            char = getMapCoords(mapp,x2,y2)
            if char != "0":
                pygame.draw.rect(screenn,color,((x2*size)+x,(y2*size)+y,size,size),5)
            x2 += 1
        y2 += 1    


    
def getMapList(mapp):
    return (mapp.split(': ')[0]).split('; ')

def getMapListRaw(mapp):
    return mapp.split(': ')[0]

def getMapData(mapp):
    return (mapp.split(': ')[1]).split('; ')

def getMapDataRaw(mapp):
    return mapp.split(': ')[1]

def convertMap(listt,data):
    return listt + ": " + data

def convertMapList(listt):
    newList = ""
    i = 0
    while i < len(listt):
        newList += listt[i]
        if i != len(listt) - 1:
            newList += "; "
        i += 1
    return newList

def convertMapBits(listt):
    newList = ""
    i = 0
    while i < len(listt):
        newList += listt[i]
        if i != len(listt) - 1:
            newList += ", "
        i += 1
    return newList    

def addMapCoord(mapp,x,y,char,rotation,xbool,ybool):
    mappList = getMapList(mapp)
    bit = char + "." + rotation + "." + xbool + "." + ybool
    bitList = mappList[y].split(', ')
    # mappList[y] = mappList[y][0:x] + bit + mappList[y][x+1:len(mappList[y])]
    bitList[x] = bit
    mappList = convertMapBits(bitList)
    newList = convertMapList(mappList)
    return convertMap(newList,getMapDataRaw(mapp))

def getMapCoords(mapp,x,y):
    mappList = (mapp.split(': ')[0]).split('; ').split(', ').split('.')
    return mappList[y][x]

def getMapSize(mapp):
    mappList = (mapp.split(': ')[0]).split('; ')
    returnVal = [len(mappList[0]),len(mappList)]
    return returnVal

def getDataSprite(char,mapp):
    mappData = (mapp.split(': ')[1]).split('; ')
    print(mappData)
    returnVal = "0"
    i = 0
    while(i < len(mappData)):
        if (char == mappData[i].split(', ')[1]):
            returnVal = mappData[i].split(', ')[0]
        i += 1
    return returnVal

"""
getMapCoords(mapp1,1,1)
print(getMapSize(mapp1)) 
"""
# print(getDataSprite("B","BBAAAA; BAAAAA; AAAAAA: grass1.png, A; grass2.png, B; grass3.png, C; "))