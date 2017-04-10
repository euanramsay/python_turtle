import turtle

def draw_shapes(color):
	window = turtle.Screen()
	window.bgcolor(color)

	draw_square("turtle", "green")
	draw_circle("circle", "blue")
	draw_triangle("square", "pink")

	window.exitonclick()

def draw_square(shape, color):
	brad = turtle.Turtle()
	brad.shape(shape)
	brad.color(color)
	brad.speed(3)

	for x in range(0, 4):
		brad.forward(100)
		brad.right(90)

def draw_circle(shape, color):
	angie = turtle.Turtle()
	angie.shape(shape)
	angie.color(color)
	angie.circle(100)

def draw_triangle(shape, color):
	john = turtle.Turtle()
	john.shape(shape)
	john.color(color)

	for x in range(0, 3):
		john.right(120)
		john.forward(200)


draw_shapes("white")
