#x1, y1 is lower left corner
def MakeGrid(x1, y1, x2, y2, lenthPoints, hightPoints):
        lenth = abs(x1 - x2)
        hight = abs(y1 - y2)
        lenthDis = lenth/(lenthPoints - 1)
        hightDis = hight/(hightPoints - 1)
        points = []
        for x in range(lenthPoints):
            for y in range(hightPoints):
                points.append([x1 + x * lenthDis, y1 + y * hightDis])
        return points

width = 0
hight = 0
def DefineScreenSize(x, y):
    global width
    global hight
    width = x
    hight = y

#-500 to 500
def CanvisToScreenPosition(x, y):
    global width
    global hight
    if width != 0 and hight != 0:
        x = x/500
        y = y/500
        return x * width / 2, y * hight / 2
    else:
        return x, y

def PenToScreenSize(size):
    return size / 100 * width
