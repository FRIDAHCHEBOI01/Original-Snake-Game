# Start coding snake game in Python
# using the turtle module library
from turtle import *
import time #time module used to control speed of the snake head bb:)
#creating an object from the screen class
my_game = Screen()
my_game.title("Original Snake game :)")
my_game.setup(width=475,height=475)
my_game.bgcolor('blanchedalmond')
my_game.bgpic('border.gif')
my_game.addshape('bb.gif')
my_game.addshape('upmouth.gif')
my_game.tracer(False) #reduces the speed of my animation
#creating the snake head
snakehead = Turtle()
snakehead.shape('upmouth.gif')
snakehead.penup()
snakehead.direction = 'stop'
#creating the snake food
snakefood = Turtle()
snakefood.shape('bb.gif')
snakefood.penup()
snakefood.goto(0,180)
#creating the text
text = Turtle()
text.penup()
text.goto(0,210)

text.hideturtle()
text.color('white')
text.write('Best Game Everrr. No lie:)', font = ('roman',13,'bold'),align ='center')

'''
After setting the setup for my game I will now write code to move the snake on the screen.
'''
def movesnake():
    if snakehead.direction == "up":
        y = snakehead.ycor()
        y += 20
        snakehead.sety(y)
    if snakehead.direction == "down":
        y = snakehead.ycor()
        y-=20
        snakehead.sety(y)
    if snakehead.direction == "right":
        x = snakehead.xcor()
        x+=20
        snakehead.setx(x)
    if snakehead.direction == "left":
        x = snakehead.xcor()
        x-=20
        snakehead.setx(x)

def upward():
    snakehead.direction = "up"
def downward():
    snakehead.direction = "down"
def right():
    snakehead.direction = "right"
def left():
    snakehead.direction = "left"
my_game.listen()

my_game.onkeypress(upward,"up")


while True:
    #update method from the screen class holds the screen for long:)
    my_game.update()
    movesnake()
    time.sleep(1)



