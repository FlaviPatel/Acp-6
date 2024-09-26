import turtle

turtle.title("Polygons")

# Screen
screen = turtle.Screen()
screen.bgcolor("Black")

# Turtle
t = turtle.Turtle()
t.shape('arrow')
t.color('blue')
t.speed(1)
t.pensize(5)
t.fillcolor('blue')

t.begin_fill()

# Draw Equilateral triangle
 
t.forward(100) 
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.penup()
t.end_fill()

# Draw rectangle
t.shape('arrow')
t.color('pink')
t.speed(1)
t.pensize(5)
t.fillcolor('pink')

t.begin_fill()
t.forward(90)
t.left(100)
t.pendown()
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.right(90)
t.forward(100)
t.penup()
t.end_fill()

# Draw hexagon
t.shape('arrow')
t.color('green')
t.speed(1)
t.pensize(5)
t.fillcolor('green')

t.begin_fill()
t.forward(360)
t.right(99)
t.pendown()
t.forward(80)  
t.right(60)  
t.forward(80)  
t.right(60)  
t.forward(80)  
t.right(60)  
t.forward(80)  
t.right(60)  
t.forward(80)  
t.right(60)  
t.forward(80)  
t.right(60)  
t.end_fill()

turtle.done()

