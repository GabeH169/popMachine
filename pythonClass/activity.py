from ezgraphics import GraphicsWindow
import random

def main():
    NUM_SIDES = 3
    MAXWIN = 600

    points = []
    again = 'Y'
    while (again == 'Y') :
        #start with 3 points
        for i in range(NUM_SIDES) :
            points.append([random.randint(1,MAXWIN),
                        random.randint(1, MAXWIN)])
            
        #set up graphics window
        win = GraphicsWindow(MAXWIN, MAXWIN)
        win.setTitle("Sierpinski's Triangle")
        canvas = win.canvas()
        userBackground = input("Enter a color for the background: ")
        userForeground = input("Enter color for the foreground: ")
        canvas.setBackground(userBackground)
        canvas.setColor(userForeground)

        for point in points :
            canvas.drawOval(point[0], point[1], 3, 3)

        #start at one of the 3 points
        nextPoint = points[0]
        win.pause(100)

        #do for lots of points
        numPoints = int(input("How many points: "))
        for i in range(numPoints) :
            #randomly select a vertex
            pointNdx = random.randint(0, NUM_SIDES-1)
            #find mindpoint between the vertex and current point
            nextPoint = findMidPoint(nextPoint, points[pointNdx])
            #draw a dot
            canvas.drawOval(nextPoint[0], nextPoint[1], 2, 2)
        
        canvas.drawText(5,5, "Close this window to start again.")
        win.wait()
        win.close()
        again = input("Do you want to go again(Y/N)? ").upper()

def findMidPoint(point1, point2) :
    midx = (point1[0] + point2[0]) / 2
    midy = (point1[1] + point2[1]) / 2
    return midx, midy

main()