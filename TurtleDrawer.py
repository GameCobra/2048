# Python program to draw square  
# using Turtle Programming 
import turtle  
import datetime
from ErrorHandling import *
from datetime import datetime
import time
from main import Start, Update
import Tools
t = turtle.Turtle() 
wn = turtle.Screen()
wn.tracer(0) 
t.hideturtle()

def RGB(R : float, G : float, B : float):
    """Converts 3 RGB values to their decimal equivelent

        Parameters
        ----------
        R : float, required
            Red chanel of the color
        G : float, required
            Green chanel of the color
        B : float, required
            Blue chanel of the color
        """
    return R/255, G/255, B/255

def teleport(x1 : float, y1 : float):
        """Moves the tutle to the specified Canvis position without drawing

        Parameters
        ----------
        x1 : float, required
            X positions destination
        y1 : float, required
            Y position destination
        """
        t.penup()
        t.goto(Tools.CanvisToScreenPosition(x1, y1))


def DrawQuad(x1 : float, y1 : float, x2 : float, y2 : float, PenColor = None, FillColor = None, Thickness : float = 1, curve : float = 0):
    """Draws a rectangle at the corasponding position

        Parameters
        ----------
        x1 : float, required
            X positions of first corner
        y1 : float, required
            Y position of first corner
        x2 : float, required
            X position of the second corner
        y2 : float, required
            Y position of the second corner
        PenColor : var, optional (Defalt: None)
            Color of the boarder, if omited will use fill color
        FillColor : var, optional (Defalt: None)
            Fill color of the quad, if omited the shape will not be filled
        Thickness : float, optional (Defalt: 1)
            The size of the quads boarder
        curve : float, optional (Defalt: 0)
            Defines the radius of the curve of the corners
        """

    #adjusts the size of the pen based on canvas size
    t.pensize(Tools.PenToScreenSize(Thickness))

    #Sets starting conditons based on input values
    if curve == 0:
        teleport(x1, y1)
        t.begin_fill()
    if PenColor == None and FillColor != None:
        PenColor = FillColor
    try:
        t.pencolor(PenColor[0], PenColor[1], PenColor[2])
    except:
        raise "No provided pen color or fill color"
    
    #Draws Typical quad
    #? Could be removed, else will work without this
    if curve == 0:
        t.pendown()
        t.goto(*Tools.CanvisToScreenPosition(x2, y1))
        t.goto(*Tools.CanvisToScreenPosition(x2, y2))
        t.goto(*Tools.CanvisToScreenPosition(x1, y2))
        t.goto(*Tools.CanvisToScreenPosition(x1, y1))
        t.penup()
    else:

        #Creates a new set of some starting conditions to curve the corners
        teleport(x2 - curve, y2)
        t.pendown()
        t.begin_fill()
        bez = Tools.BezierCurve3p(x2 - curve, y2, x2, y2 , x2, y2 - curve)
        for i in bez:
             t.goto(*Tools.CanvisToScreenPosition(i[0], i[1]))

        bez = Tools.BezierCurve3p(x2, y1 + curve, x2, y1 , x2 - curve, y1)
        for i in bez:
             t.goto(*Tools.CanvisToScreenPosition(i[0], i[1]))

        bez = Tools.BezierCurve3p(x1 + curve, y1, x1, y1, x1, y1 + curve)
        for i in bez:
             t.goto(*Tools.CanvisToScreenPosition(i[0], i[1]))

        bez = Tools.BezierCurve3p(x1, y2 - curve, x1, y2, x1 + curve, y2)
        for i in bez:
             t.goto(*Tools.CanvisToScreenPosition(i[0], i[1]))
        bez = Tools.BezierCurve3p(x2 - curve, y2, x2, y2 , x2, y2 - curve)
        t.goto(*Tools.CanvisToScreenPosition(*bez[0]))

        t.penup()

    #Ends the shape and resets changed values and conditions
    if FillColor != None:
        t.fillcolor(FillColor)
        t.end_fill()
    t.pensize(1)

def WriteText(text : str, x : float, y : float, size : float, color = "White", HAlign : str = "center", VAlign : str = "center", font : str = "Arial"): 
    """Writes text with the specified peramiters at the given position

        Parameters
        ----------
        text : str, required
            The Text to be writen
        x : float, required
            X position of the text
        y : float, required
            Y position of the text
        size : float, required
            The size in CP of the text
        color : str or triplet, optional (Defalt: "white")
            Color of the text
        HAlighn : str (left, center, right), optional (Defalt: "center")
            The horazontal alignment of the text
        VAlign : str (up, center, down), optional (Defalt: "center")
            The vertical alignment of the text
        Font : str, optional (Defalt: "Arial")
            The font of the text

        Raises
        ------
        InvalideFunctionArg
            If VAlign is not one of the 3 valade conditions
        TurtleError
            If HAlign is not one of the 3 valade conditions
        """
    if VAlign == "up":
        teleport(x, y)
    elif VAlign == "center":
        teleport(x, y - size * 0.75)
    elif VAlign == "down":
        teleport(x, y - size * 1.5)
    else:
        raise InvalideFunctionArg("VAlign", VAlign, ("up, center, down"))
    #print(t.pos())
    #print(f"{x} + {y}")
    t.pencolor(color)
    t.write(text, align=HAlign, font= (font, Tools.PenToScreenSize(size), "normal"))

frameDelay = 0
def SetFramerate(FPS : int):
    """Sets the max framerate of the display

        Parameters
        ----------
        FPS : int, required
            Max FPS of the display, use -1 for no max
        """
    global frameDelay
    frameDelay = 1/FPS

timeRate = 1
#Time since last frame
def DeltaTime() -> float:
    """Returns the time since the last fram
        """
    return (datetime.now().timestamp() - lastFramTime) * timeRate

def ClearScreen():
    """Clears the screen
        """
    t.clear()

#now_utc = datetime.now().timestamp()
  
#print(now_utc)


Start()

lastFramTime = 0
frame = 0
while True:
    if datetime.now().timestamp() > lastFramTime + frameDelay:
        lastFramTime = datetime.now().timestamp()
        Update(frame)
        frame += 1
        wn.update() 

wn.mainloop() 