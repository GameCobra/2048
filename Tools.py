import math

#x1, y1 is lower left corner
def MakeGrid(x1, y1, x2, y2, lenthPoints, hightPoints, includePosition = False):
    """Creates a list of grid cells

    Parameters
    ----------
    x1 : float, required
        X position of bottem left corner
    y1 : float, required
        Y position of bottem left corner
    x2 : float, required
        X position of top right corner
    y2 : float, required
        Y position of top right corner
    lenthPoints : int, required
        Amount of cells lenthwise in the grid
    hightPoints : int, required
        AMount of cells hightwise in the grid
    includePosition : bool, optional (Defalt: false)
        Will add 2 extra values to the outputed lists touple for their grid position

    Output
    ----------
    - List of grid cell lists
    - Sublist Item 1: X position 
    - Sublist Item 2: Y position
    """
    lenth = abs(x1 - x2)
    hight = abs(y1 - y2)
    lenthDis = lenth/(lenthPoints - 1)
    hightDis = hight/(hightPoints - 1)
    points = []
    for x in range(lenthPoints):
        for y in range(hightPoints):
            if includePosition == False:
                points.append([x1 + x * lenthDis, y1 + y * hightDis])
            else:
                points.append([x1 + x * lenthDis, y1 + y * hightDis, x, y])

    return points

width = 0
hight = 0
def DefineScreenSize(x, y):
    """Sets the size of the custom canvas

    Parameters
    ----------
    x : int, required
        Amount of pixels in lengthwise
    y : int, required
        Amount of pixels hightwise
    """
    global width
    global hight
    width = x
    hight = y

#-500 to 500
def CanvisToScreenPosition(x, y):
    """Returns a reletive canvas position from a screen position between -500 and 500

    Parameters
    ----------
    x : float, required
        X position
    y : float, required
        Y position
    
    Output
    ----------
    - Touple
    - item1: x position
    - Item2: y position
    """
    global width
    global hight
    if width != 0 and hight != 0:
        x = x/500
        y = y/500
        return x * width / 2, y * hight / 2
    else:
        return x, y

def PenToScreenSize(size):
    """Returns a pen size to account for the modifed screen size

    Parameters
    ----------
    size : float, required
        size of the pen
    

    Output
    ----------
    - Type : Float
    - Pen size adjusted for screen size
    """
    return math.floor(size / 500 * min(width, hight) / 2)
