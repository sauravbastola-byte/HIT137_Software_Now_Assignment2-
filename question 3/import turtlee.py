import turtle

def recursive_edge(t, length, depth):
    if depth == 0:
        t.forward(length)
        return

    length /= 3

    # First segment
    recursive_edge(t, length, depth - 1)

    # Downward-pointing equilateral triangle
    t.left(60)
    recursive_edge(t, length, depth - 1)

    t.right(120)
    recursive_edge(t, length, depth - 1)

    t.left(60)

    # Final segment
    recursive_edge(t, length, depth - 1)

def draw_polygon(t, sides, length, depth):
    for _ in range(sides):
        recursive_edge(t, length, depth)
        t.left(360 / sides)

# ------------------- USER INPUT -------------------

sides = int(input("Enter the number of sides: "))
length = float(input("Enter the side length: "))
depth = int(input("Enter the recursion depth: "))

# ------------------- TURTLE SETUP -------------------

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.color("cyan")
t.speed(0)
t.width(2)

# Center the drawing
t.penup()
t.goto(-length / 2, length / 3)
t.pendown()

# ------------------- DRAW -------------------

draw_polygon(t, sides, length, depth)

turtle.done()
