# Python program to draw square  
# using Turtle Programming 
import turtle  
import datetime
from main import Start, Update
from datetime import datetime
from Tools import *
import Tools
t = turtle.Turtle() 
wn = turtle.Screen()
wn.tracer(0) 
t.hideturtle()

def RGB(R, G, B):
    return R/255, G/255, B/255

def teleport(x1, y1):
    t.penup()
    t.goto(CanvisToScreenPosition(x1, y1))


def DrawQuad(x1, y1, x2, y2, PenColor, FillColor = None, thickness = 1):
    t.pensize(thickness)
    teleport(x1, y1)
    t.begin_fill()
    t.pencolor(PenColor[0], PenColor[1], PenColor[2])
    t.pendown()
    t.goto(*CanvisToScreenPosition(x2, y1))
    t.goto(*CanvisToScreenPosition(x2, y2))
    t.goto(*CanvisToScreenPosition(x1, y2))
    t.goto(*CanvisToScreenPosition(x1, y1))
    t.penup()
    if FillColor != None:
        t.fillcolor(FillColor)
        t.end_fill()
    t.pensize(1)

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