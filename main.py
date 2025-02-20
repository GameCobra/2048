
def Start():
    import TurtleDrawer as TD
    TD.SetFramerate(-1)

def Update(frame : int):
    import TurtleDrawer as TD
    TD.ClearScreen()
    for x in range(4):
        for y in range(4):
            TD.DrawQuad((x - 2) * 200, (y - 2) * 200, (x - 2) * 200 + 100, (y - 2) * 200 + 100, TD.RGB(200, 0, 0,), True)
    