import turtle

turtle.speed(0)

size = 33 # controls the size of the petals. All values
count = 30 # controls the count of the petals. All values

turtle.color("purple") #controls the color of the petals
turtle.pensize(3) # controls the thickness and width of each of the petals

def draw_petal():
    for i in range(20): # first petal
        turtle.forward(size / 2)
        turtle.right(3)
    turtle.right(120)
    for i in range(20): # second petal
        turtle.forward(size / 2)
        turtle.right(3)
    turtle.right(120)


for i in range(count): # draws the petals based of the count
    draw_petal()
    turtle.right(360 / count)

# def draw_stem(): # draws the stem
   # turtle.setheading(270)
   # turtle.forward(500)
#draw_stem()

turtle.hideturtle()
turtle.exitonclick()