import turtle
m=turtle.Screen()
text=m.textinput("Fon","fon rangi:")
m.bgcolor(text.lower())
def bayroq(rang,x,y):
    n=turtle.Turtle()
    n.speed(0)
    n.penup()
    n.goto(x,y)
    n.pendown()
    n.color("red",rang)
    n.begin_fill()
    n.hideturtle()
    for i in range(2):
        n.fd(300)
        n.rt(90)
        n.fd(50)
        n.rt(90)
    n.end_fill()

bayroq("blue",0,0)
bayroq("white",0,-50)
bayroq("green",0,-100)
def yulduz():
    for i in [13,23,33,43,53]:
        y=turtle.Turtle()
        y.speed(0)
        y.penup()
        y.goto(50+i,-35)
        y.pendown()
        y.color("white")
        y.hideturtle()
        y.begin_fill()
        for i in range(5):
            y.fd(10)
            y.rt(144)
        y.end_fill()
def yulduz2():
    for i in [13,23,33,43]:
        y=turtle.Turtle()
        y.speed(0)
        y.penup()
        y.goto(59+i,-20)
        y.pendown()
        y.color("white")
        y.hideturtle()
        y.begin_fill()
        for i in range(5):
            y.fd(10)
            y.rt(144)
        y.end_fill()
def yulduz3():
    for i in [13,23,33]:
        y=turtle.Turtle()
        y.speed(0)
        y.penup()
        y.goto(69+i,-7)
        y.pendown()
        y.color("white")
        y.hideturtle()
        y.begin_fill()
        for i in range(5):
            y.fd(10)
            y.rt(144)
        y.end_fill()
def oy():
    rang=["blue","white"]
    for i in [1,2]:
        o=turtle.Turtle()
        o.hideturtle()
        o.color(rang[i%2])
        o.penup()
        o.goto(40+(i*10),-45)
        o.pendown()
        o.begin_fill()
        o.circle(20)
        o.end_fill()

oy()
yulduz()
yulduz2()
yulduz3()
num=turtle.Turtle()
num.hideturtle()
num.penup()
num.goto(0,-200)
num.pendown()
num.color("Blue")
num.width(5)
num.write("O`zbekiston Respublikаsining Dаvlаt bаyrog`i \n1991 yil 18 noyabr",font=('Arial',12,'italic'))


m.exitonclick()