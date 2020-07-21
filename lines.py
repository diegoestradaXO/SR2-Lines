from gl import Render, color

r = Render()
r.glCreateWindow(800,600)

def line(x1, y1, x2, y2):
    dy = abs(y2 - y1)
    dx = abs(x2 - x1)

    steep = dy > dx
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dy = abs(y2 - y1)
    dx = abs(x2 - x1)

    offset = 0
    threshold = dx

    y = y1
    for x in range(x1, x2):
        if(steep):
            r.glVertex(y, x)
        else:
            r.glVertex(x, y)
        
        offset += dy * 2
        if offset >= threshold:
            y += 1
            threshold += 1 * 2 * dx
        y = y1 + round(offset)

line(10,10,80,40)

