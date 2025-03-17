import TurtleDrawer
import random
import keyboard
import math
import copy
StartGrid = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
GameGrid = copy.deepcopy(StartGrid)
previousGrid = []
lastActionFrame = 0

def Start():
    import TurtleDrawer as TD
    import Tools
    TD.SetFramerate(10)
    Tools.DefineScreenSize(500, 500)            
    keyboard.on_press(on_key_press)
    #print(Tools.BezierCurve3p(0,0, 0, 100, 100, 0))



def Update(frame : int):
    global lastActionFrame
    import TurtleDrawer as TD
    import Tools
    TD.ClearScreen()
    if lastActionFrame == -1:
        lastActionFrame = frame
    SquareRadius = 125
    grid = Tools.MakeGrid(-500 + SquareRadius, -500 + SquareRadius, 500 - SquareRadius, 500 - SquareRadius, 4, 4, True)
    for item in grid:
        TD.DrawQuad(item[0]- SquareRadius, item[1] - SquareRadius, item[0] + SquareRadius, item[1] + SquareRadius, TD.RGB(155 , 135, 117), TD.RGB(189, 172, 151), 20)
    for item in grid:
        if previousGrid != [] and  GameGrid[item[2]][item[3]] == previousGrid[item[2]][item[3]]:
            item[0] += 25
            item[1] += 25
        if GameGrid[item[2]][item[3]] != "":
            TD.DrawQuad(item[0]- SquareRadius, item[1] - SquareRadius, item[0] + SquareRadius, item[1] + SquareRadius, TD.RGB(155 , 135, 117), TD.RGB(241, 174, 114), 20)
        TD.WriteText(GameGrid[item[2]][item[3]], item[0], item[1], 65, VAlign="center",  color=[1, 1, 1])
    #for item in grid:
        
        #TD.WriteText()

def on_key_press(event):
    previousGrid = copy.deepcopy(GameGrid)
    print(previousGrid)
    global lastActionFrame
    beforeGrid = copy.deepcopy(GameGrid)
    #print(f"Key {event.name} pressed")
    if event.name == "s":
        for i in range(len(GameGrid)):
            GameGrid[i] = MergeStrip(GameGrid[i])
        if beforeGrid == GameGrid and GameGrid != StartGrid:
            return
        GenerateTile()

    if event.name == "w":
        for i in range(len(GameGrid)):
            GameGrid[i] = list(reversed(MergeStrip(list(reversed(GameGrid[i])))))
        if beforeGrid == GameGrid and GameGrid != StartGrid:
            return
        GenerateTile()

    if event.name == "a":
        for i in range(len(GameGrid)):
            SetHorazontalSlice(i, MergeStrip(GetHorazontalSlice(i)))
        if beforeGrid == GameGrid and GameGrid != StartGrid:
            return
        GenerateTile()

    if event.name == "d":
        for i in range(len(GameGrid)):
            SetHorazontalSlice(i, list(reversed(MergeStrip(list(reversed(GetHorazontalSlice(i)))))))
        if beforeGrid == GameGrid and GameGrid != StartGrid:
            return
        GenerateTile()

    lastActionFrame = -1
    

    
        

def SetHorazontalSlice(y, strip):
    for i in range(len(GameGrid)):
        GameGrid[i][y] = strip[i]

def GetHorazontalSlice(y):
    strip = []
    for i in range(len(GameGrid)):
        strip.append(GameGrid[i][y])
    return  strip

def MergeStrip(strip : list):
    for i in range(len(strip)):
        if strip[i] != "":
            for j in range(1, i + 1):
                if strip[i - j] == "":
                    strip[i - j] = strip[i - j + 1]
                    strip[i - j + 1] = ""
                else:
                    if  strip[i - j] == strip[i - j + 1] and type(strip[i - j]) is int:
                        strip[i - j] = str(strip[i - j + 1] * 2)
                        strip[i - j + 1] = ""
                        break
    for i in range(len(strip)):
        if type(strip[i]) is str and strip[i] != "":
            strip[i]= int(strip[i])

    return strip

def GenerateTile():
    global GameGrid
    if IsABlank() == True:
        while True:
            xRand = random.randint(0, 3)
            yRand = random.randint(0, 3)
            if GameGrid[xRand][yRand] == "":
                GameGrid[xRand][yRand] = 2
                return

def IsABlank() -> bool:
    for i in range(len(GameGrid)):
        for j in range(len(GameGrid[0])):
            if GameGrid[i][j] == "":
                return True
    return False
    