import turtle

turtle.tracer(0, 0)

size = 10 # controls the size of the structure. All values
count = 5 # controls the count of the flower petals. All values





def draw_petal():
    for _ in range(2):
        for i in range(20):
            turtle.forward(size / 2)
            turtle.right(3)
        turtle.right(120)

def draw_leaf():
        for i in range(20): # first petal
            turtle.forward(size / 3)
            turtle.right(3)
        turtle.right(120)
        for i in range(20): # second petal
            turtle.forward(size / 3)
            turtle.right(3)
        turtle.right(120)

def draw_stem():
    turtle.penup()
    turtle.setposition(0,100)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color("green")
    turtle.setheading(270)
    turtle.forward(12*size)
    turtle.setheading(180)
    draw_leaf()
    for i in range (2):
        turtle.setheading(270)
        turtle.forward(50)
        turtle.setheading(70-20*i)
        draw_leaf()
        turtle.setheading(270)
        turtle.forward(50)
        turtle.setheading(180+20*i)
        draw_leaf()
    turtle.setheading(270)
    turtle.forward(200)
    turtle.color("cyan") #controls the color of the petals
    turtle.pensize(3) # controls the thickness and width of each of the petals
    turtle.penup()
    turtle.setposition(0,100)
    turtle.setheading(0)
    turtle.pendown()

draw_stem()
for i in range(count): # draws the petals based of the count
    draw_petal()
    turtle.right(360 / count)


# def draw_stem(): # draws the stem
   # turtle.setheading(270)
   # turtle.forward(500)
#draw_stem()

turtle.hideturtle()
turtle.update()
turtle.exitonclick()