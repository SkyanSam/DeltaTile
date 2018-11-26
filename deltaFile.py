import pickle
import deltaBase as deltaTile

def find(string,array,num,returnNum):
    val = ""
    i = 0
    while i < len(array):
        if array[i][num] == string:
            val = array[i][returnNum]
        i += 1
    
    return val
    
def addLayer(width,height,size):
    
    mappLine = ("0.0.0, " * (width-1)) + "0.0.0; "
    mapp = mappLine * (height-1) + mappLine
    
    print("What type of map layer are you creating?")
    print("boundarymap, spritemap")
    typp = input("")
    
    location = ""
    keyy = ""
    if typp == "spritemap":
        print("Type in the tile folder location.")
        location = input("")
        
        print("Type in a key, ")
        print("Reference: [tile, key; tile, key]") 
        print("Example:[grass.png, A; stone.png, B; bric...]")
        keyy = input("")
    
    layer = str(mapp) + ": " + str(keyy) + ": " + str(typp) + ": " + str(location) + ": " + str(size)
    
    return layer
        
def addDataLayer(width,height,size):
    mappLine = ("0.0.0, " * (width-1)) + "0.0.0; "
    mapp = mappLine * (height-1) + mappLine
    
    keyy = ""
    typp = ""
    location = ""
    
    print("Wheres the tiledata located at?")
    ans = input("")
    
    tileData = ans.split(';').split(': ')
    keyy = find("key",tileData,0,1)
    typp = find("type",tileData,0,1)
    location = find("location",tileData,0,1)
    
    layer = str(mapp) + ": " + str(keyy) + ": " + str(typp) + ": " + str(location) + ": " + str(size)
    
    return layer
    
    
    
    
def addLayerMsg(width,height,size):   
    addLayerbln = True
    layers = []
    
    while addLayerbln:
        print("Want to add a layer?")
        print("yes, no")
        ans = input("")
        
        if ans == "yes":
            print("Make a NEW layer from scratch or LOAD layer data")
            print("new [N], load [L]")
            ans = input("")
            if ans == "N":
                layers = layers + [addLayer(int(width),int(height),int(size))]
            elif ans == "L":
                layers = layers + [addDataLayer(int(width),int(height),int(size))]
            
        elif ans == "no":
            addLayerbln = False
    
    i = 0
    while i < len(layers)-1:
        game_data += layers[i] + "| "
        i += 1
    game_data += layers[i]
    
    return game_data

def new():
    print("")
    game_data = ""
    
    print("Whats the tile dimensions for the tilemap?")
    width = input("Width: ")
    height = input("Height: ")
    print("Whats the tile size?")
    tSize = input("Tile Size: ")
    
    
    game_data = addLayerMsg(width,height,tSize)
    
    
    print("Where would you like to save this tilemap?")
    ans = input("")
    
    save_file = open(ans, 'w')
    save_file.write(game_data)
    save_file.close()
    
    
    
    
    
    
    
        
    
    
    

def openn():
    print("Type in the file location you want to open from.")
    location = input("")
    load_file = open(location, 'r')
    game_data = load_file.read
    load_file.close()
    
    mapSize = deltaTile.getMapSize(game_data.split('| ')[0])
    tSize = (game_data.split('| ')[0]).split(': ')[4]
    
    game_data = addLayerMsg(mapSize[0],mapSize[1],tSize)
    
    save_file = open(location, 'w')
    save_file.write(game_data)
    save_file.close()    
    
    

def main():
    print("Hey. You are using DeltaTile.")
    print("This project can be used in any way under the MIT License.")
    print("You can also use this for your games.")
    print("DeltaTile is created by SkyanSam. The owner of Skylark Studios.")
    print("Would you like to open a map and replace it or make a new map?")
    print("[O] to open a map and replace it, [N] to make a new map and save it")
    ans = input("")
    if ans == "N":
        new()
    if ans == "O":
        openn()
    

main()