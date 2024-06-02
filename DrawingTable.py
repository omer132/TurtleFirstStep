import turtle

screen=turtle.Screen()
screen.bgcolor("pink")
screen.title("ömer")

x=turtle.Turtle()

def frw():
    x.forward(100)
def lft():
    x.left(90)
def rght():
    x.right(90)
def bck():
    x.backward(100)
def pncd():
    x.pendown()
def clr():
    x.clear()
def pncu():
    x.penup()
def rtrn():
    x.home()

screen.listen()
screen.onkey(key="d",fun=rght)
screen.onkey(key="a",fun=lft)
screen.onkey(key="w",fun=frw)
screen.onkey(key="s",fun=bck)
screen.onkey(key="t",fun=pncd)
screen.onkey(key="y",fun=pncu)
screen.onkey(key="x",fun=clr)
screen.onkey(key="z",fun=rtrn)


screen.exitonclick()