import turtle as tr

tr.color('blue')
tr.pensize(5)
tr.speed(15)

def circle():
    tr.circle(100)

tr.penup()
tr.back(220)
tr.pendown()
circle()

tr.penup()
tr.forward(220)
tr.pendown()
tr.color('black')
circle()

tr.penup()
tr.forward(220)
tr.pendown()
tr.color('red')
circle()

tr.penup()
tr.right(110)
tr.back(50)
tr.right(90)
tr.forward(105)
tr.pendown()
tr.color('green')
circle()

tr.penup()
tr.left(20)
tr.forward(215)
tr.pendown()
tr.color('yellow')
circle()

