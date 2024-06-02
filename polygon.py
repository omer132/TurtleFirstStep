import turtle

screen=turtle.Screen()
screen.bgcolor("pink")
screen.title("python project")

pencil=turtle.Turtle()

NumberOfEdges=int(input("enter number of edges:    "))
angle=360.0

for i in range(NumberOfEdges):
    x=angle/NumberOfEdges
    pencil.right(x)
    pencil.forward(100)

turtle.done()