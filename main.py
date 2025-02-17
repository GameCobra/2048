
def Start():
    import TurtleDrawer as TD

def Update(frame : int):
    import TurtleDrawer as TD
    TD.ClearScreen()
    TD.DrawQuad(0, 0, frame % 50, frame % 50, TD.RGB(frame % 200, 0, 0,))
    