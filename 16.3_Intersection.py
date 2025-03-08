# Input the start point and end point of two straight lines
x1 , y1 , x2, y2 = map(int,input("Enter the start and end point of line 1 (x1, y1) and (x2, y2) :").split(","))
x3 , y3 , x4, y4 = map(int,input("Enter the start and end point of line 1 (x3, y3) and (x4, y4) :").split(","))

def Intersection(x1, y1, x2, y2, x3, y3, x4, y4):
    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y4 - y3) / (x4 - x3)

    x = ((slope1 * x1) + (y1 + y3) - (slope2 * x3)) / (slope1 - slope2)
    y = (slope1 * (x - x1)) + y1

    return(x,y)

print(Intersection(x1,y1,x2,y2,x3,y3,x4,y4))