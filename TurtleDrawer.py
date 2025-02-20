# Python program to draw square  
# using Turtle Programming 
import turtle  
import datetime
from main import Start, Update
from datetime import datetime
t = turtle.Turtle() 
wn = turtle.Screen()
wn.tracer(0) 


def RGB(R, G, B):
    return R/255, G/255, B/255

def teleport(x1, y1):
    t.penup()
    t.goto(x1, y1)


def DrawQuad(x1, y1, x2, y2, color, fill:bool = False):
    teleport(x1, y1)
    t.begin_fill()
    t.color(color[0], color[1], color[2])
    t.pendown()
    t.goto(x1, y2)
    t.goto(x2, y2)
    t.goto(x2, y1)
    t.goto(x1, y1)
    t.penup()
    if fill == True:
        t.end_fill()

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

def CanvisToScreenPosition(x, y):
    pass

def DefineScreenSize(x, y):
    pass
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