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

def RGB(R, G, B):
    return R/255, G/255, B/255

def teleport(x1, y1):
    t.penup()
    t.goto(Tools.CanvisToScreenPosition(x1, y1))


def DrawQuad(x1, y1, x2, y2, PenColor, FillColor = None, thickness = 1):
    t.pensize(Tools.PenToScreenSize(thickness))
    teleport(x1, y1)
    t.begin_fill()
    if PenColor == None and FillColor != None:
        PenColor = FillColor
    try:
        t.pencolor(PenColor[0], PenColor[1], PenColor[2])
    except:
        raise "No provided pen color or fill color"
    t.pendown()
    t.goto(*Tools.CanvisToScreenPosition(x2, y1))
    t.goto(*Tools.CanvisToScreenPosition(x2, y2))
    t.goto(*Tools.CanvisToScreenPosition(x1, y2))
    t.goto(*Tools.CanvisToScreenPosition(x1, y1))
    t.penup()
    if FillColor != None:
        t.fillcolor(FillColor)
        t.end_fill()
    t.pensize(1)

def WriteText(text : str, x : float, y : float, size : float, color = "White", HAlign : str = "center", VAlign : str = "center", font : str = "Arial"): 
    """Prints what the animals name is and what sound it makes.

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
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
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
def SetFramerate(FPS):
    global frameDelay
    frameDelay = 1/FPS

timeRate = 1
#Time since last frame
def DeltaTime():
    return (datetime.now().timestamp() - lastFramTime) * timeRate

def ClearScreen():
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