import turtle

# I must remind that it's a comment !

turtle.speed(6)

# First form : box
turtle.pendown()
turtle.right(-90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)

turtle.penup()

#Second form : pentagone
turtle.goto(200,0)

turtle.pendown()
turtle.right(-18)
for i in range (4) :
    turtle.forward(100)
    turtle.right(72)
turtle.forward(100)
turtle.right(90)
turtle.penup()

#Third form : ship
shipStartPos = 400
turtle.goto(shipStartPos, 15)
turtle.pendown()
# Sail part
turtle.right(90)
for i in range (3) :
    turtle.forward(150)
    turtle.right(-120)
turtle.goto(shipStartPos + 75, 15)
turtle.right(-90)
turtle.forward(132)
turtle.penup()

# Hull part
turtle.goto(shipStartPos, 0)
turtle.pendown()
turtle.right(90)
turtle.forward(150)
turtle.right(90+65)
turtle.forward(55)
turtle.right(25)
turtle.forward(55)
turtle.right(25)
turtle.forward(55)
turtle.penup()

turtle.done()