import turtle

FACE_COLOR='yellow'
EYE_COLOR='black'
MOUTH_COLOR='red'


t = turtle.Turtle()

def face():
    t.fillcolor(FACE_COLOR)
    t.begin_fill()
    t.circle(100)
    t.end_fill()


def eyes():
    t.fillcolor(EYE_COLOR)
    

    t.penup()
    t.goto(-40, 120)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

   
    t.penup()
    t.goto(40, 120)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()


def mouth():
    t.fillcolor(MOUTH_COLOR)
    t.penup()
    t.goto(-30, 60)
    t.pendown()
    t.right(90)
    t.circle(30, 180)


face()
eyes()
mouth()

turtle.done()

