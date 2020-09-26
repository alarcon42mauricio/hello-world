import turtle
pen = turtle.Pen('turtle')
pen.pensize(4)

pen.home()
pen.showturtle()

# Begin drawing w red pen
pen.color('red')
pen.pensize(3.14)
pen.left(135)
pen.forward(225)
pen.right(90)
pen.forward(225)
pen.right(90)
pen.forward(225)

# Begin drawing w blue pen
pen.color('blue')
pen.left(90)
pen.forward(225)
pen.right(90)
pen.forward(225)
pen.right(90)
pen.forward(135)

#Fish it
turtle.done()