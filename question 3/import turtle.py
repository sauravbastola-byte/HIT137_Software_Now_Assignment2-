import turtle

def recursive_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    length /= 3
    recursive_edge(t, length, depth - 1)

    t.left(60)
    recursive_edge(t, length, depth - 1)

    t.right(120)
    recursive_edge(t, length, depth - 1)

    t.left(60)
    recursive_edge(t, length, depth - 1)

def draw_polygon(t, sides, length, depth):
    for _ in range(sides):
        recursive_edge(t, length, depth)
        t.left(360 / sides)

# Turtle setup
screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.color("cyan")
t.speed(0)
t.width(2)

t.penup()
t.goto(-150, 80)
t.pendown()

# Parameters
SIDES = 4
LENGTH = 300
DEPTH = 3

draw_polygon(t, SIDES, LENGTH, DEPTH)

turtle.done()


