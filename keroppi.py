import turtle
import math

kero = turtle.Turtle()
kero.hideturtle()
turtle.hideturtle()
# kero.shape("turtle")
kero.speed(0)

#BG SETUP
screen = turtle.getscreen()
screen.setup(1000,1000)

#BG
colors = ["pink","ivory"]
kero.width(200)

start = -430
for i in range(0,4):
    for g in colors:
        kero.color(g)
        kero.penup()
        kero.goto(start,-500)
        kero.pendown()
        kero.seth(90)
        kero.forward(1200)
        start += 150

kero.width(7)

#head
def drawHead(x,y,radius_red,radius_blue,tilt):
    kero.color("black","green yellow")
    kero.up()
    kero.goto(x,y)
    kero.begin_fill()
    kero.seth(90+tilt)
    kero.fd((radius_red-radius_blue)*math.sqrt(2)/2)
    kero.left(135)
    kero.fd(radius_red)
    kero.down()
    kero.seth(-45+tilt)
    kero.circle(radius_red,90,100)
    kero.circle(radius_blue,90,100)
    kero.circle(radius_red,90,100)
    kero.circle(radius_blue,90,100)
    kero.end_fill()
#eyes
def drawEyes(startX):
    
    kero.penup()
    kero.goto(startX,150)
    kero.seth(90)
    kero.color("black","white")
    kero.pendown()
    kero.begin_fill()
    kero.circle(100)
    kero.end_fill()
    
    kero.penup()
    kero.color("black")
    
    if (startX != 0):
        kero.goto(60,150)
    else:
        kero.goto(-60,150)
    kero.dot(75)
    kero.back(10)
    kero.sety(160)
    kero.color("white")
    kero.dot(20)

#mouth
def drawMouth(dist):
    kero.penup()
    kero.color("black")
    kero.goto(0,-190)
    kero.pendown()
    kero.left(60)
    kero.forward(dist)
    kero.back(dist)
    
    kero.seth(90)
    kero.pendown()
    kero.right(55)
    kero.forward(dist)

def drawCheeks(startX):
    kero.penup()
    kero.goto(startX,0)
    kero.color("pink")
    kero.dot(100)
    
def drawHands():
    kero.goto(-170,-145)
    kero.color("black","green yellow")
    kero.pendown() #RIGHT HAND
    kero.begin_fill() #BEGIN FILL
    kero.seth(270)
    
    kero.right(15)
    kero.forward(90)
    
    kero.right(130)
    kero.forward(20)
    
    
    kero.left(70)
    kero.forward(20)
    kero.right(90)
    kero.forward(20)
    kero.left(70)
    kero.forward(20)
    
    kero.seth(40)
    kero.forward(95)
    kero.end_fill() #END FILL
    kero.penup()
    
    kero.goto(170,-145) #RIGHT HAND
    kero.pendown()
    kero.begin_fill() #BEGIN FILL
    kero.seth(270)
    
    kero.left(15)
    kero.forward(90)
    
    kero.left(130)
    kero.forward(20)
    
    
    kero.right(70)
    kero.forward(20)
    kero.left(90)
    kero.forward(20)
    kero.right(70)
    kero.forward(20)
    
    kero.seth(140)
    kero.forward(95)
    kero.end_fill() #END FILL
    kero.penup()

def drawBody():
    kero.penup()
    kero.goto(-170,-145)
    kero.color("black","ivory")
    kero.pendown()
    kero.begin_fill() #BEGIN FILL
    kero.seth(270)
    
    kero.right(15)
    kero.forward(175)
    kero.penup()
    
    kero.back(175)
    kero.seth(0)
    kero.pendown()
    kero.forward(340)
    
    kero.seth(270)
    kero.left(15)
    kero.forward(175)
    
    
    kero.seth(180)
    kero.goto(-215,-314.04)
    kero.end_fill() #END FILL
    kero.penup()
    
    
    #stripes
    kero.penup()
    kero.goto(-170,-145)
    for i in range(0,2):
        
        kero.seth(0)
        kero.color("salmon")
        kero.pendown()
        
        kero.forward(50)
        kero.begin_fill()
        kero.forward(100)
        kero.right(90)
        kero.forward(162)
        kero.right(90)
        kero.forward(100)
        kero.right(90)
        kero.forward(162)
        kero.end_fill()
        
        kero.seth(0)
        kero.forward(93)
        
    kero.penup()
    kero.goto(0,-230)
    drawBow(40)

#feet
def drawFeet():
    kero.color("black","green yellow")
    
    kero.pendown()
    kero.right(10)
    kero.begin_fill()
    kero.forward(50)
    
    kero.seth(0)
    kero.left(45)
    
    for i in range(0,2):
        kero.forward(40)
        kero.right(90)
        kero.forward(40)
        kero.left(90)
    kero.seth(100)
    kero.forward(50)
    kero.seth(180)
    kero.forward(100)
    kero.end_fill()
    
    kero.penup()


def drawBow(bow):
    
    kero.seth(180)
    kero.color("black")
    kero.pendown()
    kero.begin_fill()
    kero.right(30)
    kero.forward(bow)
    kero.seth(270)
    kero.forward(bow)
    kero.left(120)
    kero.forward(bow)
    kero.end_fill()

    kero.begin_fill()
    kero.forward(bow)
    kero.right(120)
    kero.forward(bow)
    kero.right(120)
    kero.forward(bow)
    kero.end_fill()
    kero.penup()


#KEROPPI
drawBody()
drawHead(0,0,300,150,0)
drawEyes(0)
drawEyes(200)
drawMouth(175)
drawCheeks(-170)
drawCheeks(170)

#left foot setup
kero.penup()
kero.goto(-215,-330.04)
kero.forward(30)
kero.seth(270)
kero.forward(3)
drawFeet()

#right foot setup
kero.goto(215.29,-314.04)
kero.forward(130)
kero.seth(270)
drawFeet()

kero.penup()

drawHands()
turtle.done()