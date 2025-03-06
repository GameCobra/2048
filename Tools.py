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
    list[lenthPoints][2] (X position : float, Y position : float)
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
    (x position : float, y position : float)
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
    pensize : float
    """
    return math.floor(size / 500 * min(width, hight) / 2)

def BezierCurve3p(X1 : float, Y1 : float, X2 : float, Y2 : float, X3 : float, Y3 : float, resolution : int = 100):
    """Returns a list of bbezier curve points

    Parameters
    ----------
    X1 : float, required
        X position of 1st point
    Y1 : float, required
        Y position of 1st point
    X2 : float, required
        X position of control point
    Y2 : float, required
        Y position of control point
    X3 : float, required
        X position of 2nd point
    Y3 : float, required
        Y position of 2nd point
    resolution : int, optional (Defalt: 100)
        Controls how detailed the curve is

    Output
    ----------
    list[resolution + 1][2] (X position : float, Y position : float)
    """
    returnList = []
    for i in range(resolution + 1): 
        XV1 = X1 /resolution * (resolution - i) + X2/resolution * i
        YV1 = Y1 /resolution * (resolution - i) + Y2/resolution * i
        XV2 = X2 /resolution * (resolution - i) + X3/resolution * i
        YV2 = Y2 /resolution * (resolution - i) + Y3/resolution * i
        XV3 = XV1 /resolution * (resolution - i) + XV2/resolution * i
        YV3 = YV1 /resolution * (resolution - i) + YV2/resolution * i
        returnList.append([XV3, YV3])
    return returnList