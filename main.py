
def Start():
    import TurtleDrawer as TD
    import Tools
    TD.SetFramerate(150)
    Tools.DefineScreenSize(500, 500)

def Update(frame : int):
    import TurtleDrawer as TD
    import Tools
    TD.ClearScreen()
    SquareRadius = 125
    grid = Tools.MakeGrid(-500 + SquareRadius, -500 + SquareRadius, 500 - SquareRadius, 500 - SquareRadius, 4, 4)
    for item in grid:
        TD.DrawQuad(item[0]- SquareRadius, item[1] - SquareRadius, item[0] + SquareRadius, item[1] + SquareRadius, TD.RGB(155, 135, 117), TD.RGB(189, 172, 151), 2)
    