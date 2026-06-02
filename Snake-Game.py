import turtle
import time
import random

screen = turtle.Screen()
turtle.colormode(255)
screen.bgcolor((53,245,98))
screen.setup(width=600,height=600)
screen.title('Snake game made by Diffy02. You should subscribe to his channel')
screen.tracer(0)
list_segment = [(0,0)]

score = 0
title = turtle.Turtle()
title.color((0,0,0))
title.pensize(5)
title.penup()
title.hideturtle()
title.goto(0,260)
title.pendown()
title.write(f'score: {score}',align='center',font=("Verdana", 12, "normal"))
game_over1 = ['You Failed!','Try again next time...','GAME OVER.']

food = turtle.Turtle()
food.color('red')
food.shape('circle')
food.penup()
food.goto(0,100)
yummy = ['red','blue']

position_x = 280
position_y = 300
position_x_negative = -300
position_y_negative = -280

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

second_segments = []

for segment in list_segment:
    head = turtle.Turtle()
    head.color((23,105,42))
    head.shape('square')
    head.penup()
    head.goto(segment)
    second_segments.append(head)

state1 = True
state2 = True
state3 = True
state4 = True

def up():
    global state1
    global state2
    global state3
    global state4
    if second_segments[0].heading != DOWN and state1:
        second_segments[0].setheading(UP)
        state1 = True
        state3 = True
        state4 = True
        state2 = False
def down():
    global state1
    global state2
    global state3
    global state4
    if second_segments[0].heading != UP and state2:
        second_segments[0].setheading(DOWN)
        state2 = True
        state3 = True
        state4 = True
        state1 = False
def left():
    global state3
    global state4
    global state1
    global state2
    if second_segments[0].heading != RIGHT and state3:
        second_segments[0].setheading(LEFT)
        state3 = True
        state1 = True
        state2 = True
        state4 = False

def right():
    global state3
    global state4
    global state1
    global state2
    if second_segments[0].heading != LEFT and state4:
        second_segments[0].setheading(RIGHT)
        state4 = True
        state1 = True
        state2 = True
        state3 = False

second = 0.1
# timer = time.time()

game = True
while game:
    screen.update()
    time.sleep(second)
    for seg in range(len(second_segments) - 1,0,-1):
        pos_x = second_segments[seg - 1].xcor()
        pos_y = second_segments[seg - 1].ycor()
        second_segments[seg].goto(pos_x,pos_y)
        second_segments[seg].color((63,139,81))
        second_segments[seg].showturtle()
    second_segments[0].forward(20)

    if second_segments[0].distance(food) < 20:
        food.penup()
        x = random.randint(-14,14)*20
        y = random.randint(-14,14)*20
        food.color(random.choice(yummy))
        food.goto(x, y)
        title.clear()
        score += 1
        title.write(f'score: {score}',align='center',font=("Verdana", 12, "normal"))

        new_segment = turtle.Turtle()
        new_segment.hideturtle()
        new_segment.color((255, 255, 255))
        new_segment.shape('square')
        new_segment.penup()
        new_segment.goto(2000,2000)
        second_segments.append(new_segment)

    if second_segments[0].xcor() > position_x or second_segments[0].ycor() > position_y or second_segments[0].xcor() < position_x_negative or second_segments[0].ycor() < position_y_negative:
        game = False
        title.penup()
        title.goto(0,0)
        title.pendown()
        title.write(f'{random.choice(game_over1)}',align='center',font=('Comic Sans',30,'normal'))

    for segment in second_segments[1:]:
        if second_segments[0].distance(segment) < 15:
            game = False
            title.penup()
            title.goto(0, 0)
            title.pendown()
            title.write(f'{random.choice(game_over1)}', align='center', font=('Comic Sans', 30, 'normal'))

    # if time.time() - timer >= 5:
    #     if second > 0.01:
    #         second -= 0.01
    #     timer = time.time

    screen.listen()
    screen.onkey(up,'Up')
    screen.onkey(down, 'Down')
    screen.onkey(left,'Left')
    screen.onkey(right,'Right')

    screen.onkey(up, 'w')
    screen.onkey(down, 's')
    screen.onkey(left, 'a')
    screen.onkey(right, 'd')

turtle.done()
