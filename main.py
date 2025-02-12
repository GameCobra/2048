# Python program to draw square  
# using Turtle Programming 
import turtle  
t = turtle.Turtle() 
wn = turtle.Screen()
wn.tracer(0) 

def teleport(x1, y1):
    t.penup()
    t.goto(x1, y1)


def DrawSquare(x1, y1, x2, y2, color):
    teleport(x1, y1)
    t.pencolor(color[0], color[1], color[2])
    t.pendown()
    t.goto(x1, y2)
    t.goto(x2, y2)
    t.goto(x2, y1)
    t.penup()
      
DrawSquare(0, 0, 100, 100, [41, 41, 253])


wn.update() 
wn.mainloop() 