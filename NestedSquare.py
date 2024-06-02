import turtle

screen=turtle.Screen()
screen.bgcolor("pink")
screen.title("python project")

pencil=turtle.Turtle()

x=150

for i in range(32):
    pencil.forward(x)
    pencil.left(90)
    x=x-5

turtle.done()    