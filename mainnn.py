
import turtle

turtle.speed(15)
size = 20   # change this to control petal size
count = 30  # change this to control petal count

turtle.color("orange")
turtle.pensize(3)

def draw_petal():
    # First half of petal
    for i in range(20):
        turtle.forward(size / 2)
        turtle.right(3)
    # Second half of petal
    turtle.right(120)
    for i in range(20):
        turtle.forward(size / 2)
        turtle.right(3)
    turtle.right(120)

# Draw petals evenly spaced
for i in range(count):
    draw_petal()
    turtle.right(360 / count)

turtle.hideturtle
turtle.exitonclick()