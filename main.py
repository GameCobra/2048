import TurtleDrawer
import random
import keyboard
GameGrid = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]

def Start():
    import TurtleDrawer as TD
    import Tools
    TD.SetFramerate(-1)
    Tools.DefineScreenSize(500, 500)            
    keyboard.on_press(on_key_press)



def Update(frame : int):
    import TurtleDrawer as TD
    import Tools
    TD.ClearScreen()
    SquareRadius = 125
    grid = Tools.MakeGrid(-500 + SquareRadius, -500 + SquareRadius, 500 - SquareRadius, 500 - SquareRadius, 4, 4, True)
    for item in grid:
        if GameGrid[item[2]][item[3]] == "":
            TD.DrawQuad(item[0]- SquareRadius, item[1] - SquareRadius, item[0] + SquareRadius, item[1] + SquareRadius, TD.RGB(155 , 135, 117), TD.RGB(189, 172, 151), 20)
        else:
            TD.DrawQuad(item[0]- SquareRadius, item[1] - SquareRadius, item[0] + SquareRadius, item[1] + SquareRadius, TD.RGB(155, 135, 117), TD.RGB(241, 174, 114), 20)

        TD.WriteText(GameGrid[item[2]][item[3]], item[0], item[1], 65, VAlign="center",  color=[1, 1, 1])
    #for item in grid:
        
        #TD.WriteText()

def on_key_press(event):
    GenerateTile()
    print(f"Key {event.name} pressed")
    print(GetHorazontalSlice(1))

def GetHorazontalSlice(y):
    strip = []
    for i in range(len(GameGrid)):
        strip.append(GameGrid[i][y])
    return  MergeStrip(strip)

def MergeStrip(strip : list):
    for i in range(len(strip)):
        if strip[i] != "":
            j = 1
            for j in range(i + 1):
                if strip[i - j] == "":
                    strip[i - j] = strip[i - j + 1]
                    strip[i - j + 1] = ""
                else:
                    if  strip[i - j] == strip[i - j + 1]:
                            strip[i - j] = strip[i - j + 1] * 2
                            strip[i - j + 1] = ""
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
    