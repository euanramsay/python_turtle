import turtle

john = turtle.Turtle()

def draw_shapes(color):
	window = turtle.Screen()
	window.bgcolor(color)

	for i in range(0, 36):
		draw_triangle("turtle", "green", 600)
		john.right(10)
	# draw_circle("circle", "blue")
	# draw_triangle("square", "pink")

	for i in range(0, 36):
		draw_triangle("turtle", "yellow", 200)
		john.right(10)

	window.exitonclick()

# def draw_square(shape, color):
# 	brad.shape(shape)
# 	brad.color(color)
# 	brad.speed(6)

# 	for i in range(0, 4):
# 		brad.forward(100)
# 		brad.right(90)

# def draw_circle(shape, color):
# 	angie = turtle.Turtle()
# 	angie.shape(shape)
# 	angie.color(color)
# 	angie.circle(100)

def draw_triangle(shape, color, size):
	john.shape(shape)
	john.color(color)
	john.speed(9)

	for x in range(0, 3):
		john.right(160)
		john.forward(size)


draw_shapes("white")
