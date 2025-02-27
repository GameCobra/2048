import TurtleDrawer
import random
GameGrid = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]

def Start():
    import TurtleDrawer as TD
    import Tools
    TD.SetFramerate(-1)
    Tools.DefineScreenSize(500, 500)            
    GenerateTile()
    GenerateTile()
    GenerateTile()
    GenerateTile()
    GenerateTile()


def Update(frame : int):
    import TurtleDrawer as TD
    import Tools
    TD.ClearScreen()
    SquareRadius = 125
    grid = Tools.MakeGrid(-500 + SquareRadius, -500 + SquareRadius, 500 - SquareRadius, 500 - SquareRadius, 4, 4, True)
    for item in grid:
        TD.DrawQuad(item[0]- SquareRadius, item[1] - SquareRadius, item[0] + SquareRadius, item[1] + SquareRadius, TD.RGB(155, 135, 117), TD.RGB(189, 172, 151), 20)
    for item in grid:
        TD.WriteText(GameGrid[item[2]][item[3]], item[0], item[1], 65, VAlign="center", color=[1, 1, 1])
        #TD.WriteText()

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
            if GameGrid[i][j] == 0:
                return True
    return False
    