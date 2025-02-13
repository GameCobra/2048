# Python program to draw square  
# using Turtle Programming 
import turtle  
from main import Start, Update
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

Start()

while True:
    Update()
    wn.update() 

wn.mainloop() 