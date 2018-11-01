import turtle
import os
import math
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
screen = turtle.Screen()

border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#setting score to start
score = 0;
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


#create player
playerImg = "playerResize.gif"
screen.addshape(playerImg)

player = turtle.Turtle()
player.color("green")
player.shape(playerImg)
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

#make bad guys
#setting number of badGuys with a list
badGuyImg = "badguyfull.gif"
screen.addshape(badGuyImg)
number_of_badGuys = 5
badGuys = []
for i in range(number_of_badGuys):
    badGuys.append(turtle.Turtle())

for badGuy in badGuys:
    # badGuy = turtle.Turtle()
    badGuy.color("red")
    badGuy.shape(badGuyImg)
    badGuy.penup()
    badGuy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    badGuy.setposition(x, y)

badGuySpeed = 2

# #make pew pews
pew = turtle.Turtle()
pew.color("yellow")
pew.shape("circle")
pew.penup()
pew.speed(0)
pew.setheading(90)
pew.shapesize(0.3, 0.3)
pew.hideturtle()
pewSpeed = 30

pewState = "ready"

#moving the guy
playerSpeed = 15
def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)

def pew_pew():
    #Declare bulletstate as a global bc i think ill be able to change
    #it later externally for like idk hits some shit or fires on some shit right?
    global pewState
    if pewState == "ready":
        pewState = "fire"
        x =  player.xcor()
        y =  player.ycor() + 10
        pew.setposition(x, y)
        pew.showturtle()
        pewState = "ready"

def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False

turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(pew_pew, "space")


#game loop (main logic)
while True:
    for badGuy in badGuys:
        #moving badGuy
        x = badGuy.xcor()
        x += badGuySpeed
        badGuy.setx(x)

        #bad guy movement
        if badGuy.xcor() > 280:
            for e in badGuys:
                y = e.ycor()
                y -= 40
                e.sety(y)
            badGuySpeed *= -1

        if badGuy.xcor() < -280:
            for e in badGuys:
                y = e.ycor()
                y -= 40
                e.sety(y)
            badGuySpeed *= -1

        if isCollision(pew, badGuy):
            pew.hideturtle()
            pewState = "ready"
            pew.setposition(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            badGuy.setposition(x, y)
            score += 10
            scorestring =  "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))


        if isCollision(badGuy, player):
            player.hideturtle()
            badGuy.hideturtle()
            print ("Game Over")
            break

    #moving pews
    y = pew.ycor()
    y += pewSpeed
    pew.sety(y)

    if pew.ycor() > 290:
        pew.hideturtle()
        pewState = "ready"




        #reverse if it reaches border


#testttttt




delay = wn.mainloop()
