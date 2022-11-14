# created by yours truely

import turtle

# Basic window set up
wn = turtle.Screen()
wn.title('Tick Tac Toe by Zach Dickerson')
wn.bgcolor("Grey")
wn.setup(width=800, height=700)
wn.tracer(0)

# Making the board
line = turtle.Turtle()
line.penup()
line.goto(-100,-300)
line.pendown()
line.goto(-100,300)

line.penup()
line.goto(100,-300)
line.pendown()
line.goto(100,300)

line.penup()
line.goto(-300,-100)
line.pendown()
line.goto(300, -100)

line.penup()
line.goto(-300, 100)
line.pendown()
line.goto(300, 100)
line.hideturtle()

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.write(f"Player A: 0  Player B: 0", align="center", font=("Courier",24,"normal"))

our_C_list = []  
our_X_list = []

circle_key = {
    1:(-200,-275),
    2:(0,-275),
    3:(200,-275),
    4:(-200,-75),
    5:(0,-75),
    6:(200,-75),
    7:(-200,125),
    8:(0,125),
    9:(200, 125),
}

x_key = {
    1:(-200,-200),
    2:(0,-200),
    3:(200,-200),
    4:(-200,0),
    5:(0,0),
    6:(200,0),
    7:(-200,200),
    8:(0,200),
    9:(200,200),
}

# Drawing a X
def our_X():
    t = turtle.Turtle()
    t.up()
    t.penup()
    while True:
        try:
            user_int = int(input('Enter your X choice: '))
        except KeyError:
            print('sorry better try again')
            continue
        else:
            break
    if user_int in x_key.keys():
        our_X_list.append(user_int)
        t.goto(x_key[user_int])
        t.pendown()
        t.hideturtle()
    else:
        print('wrong')
    t.pendown()
    for angle in range(-135, 136, 90):
        length = 200
        mock = t.clone()
        mock.left(angle)
        mock.forward(length / 2)
        mock.hideturtle()
        t.hideturtle()
    t.hideturtle()
    wn.update()  
    
# Drawing our circle        
def our_circle():
    r = 75
    t = turtle.Turtle()
    t.penup()
    while True:
        try:
            user_int = int(input('Enter your C choice: '))
        except KeyError:
            print('sorry better try again')
            continue
        else:
            break
    if user_int in circle_key.keys():
        our_C_list.append(user_int)
        t.goto(circle_key[user_int])
        t.pendown()
        t.hideturtle()
    else:
        print('wrong')
    t.circle(r)
    t.hideturtle()
    wn.update()  

# winner's line
def winners_line():
    t = turtle.Turtle()
    on_tw_th = [1,2,3]
    fo_fi_si = [4,5,6]
    se_ei_ni = [7,8,9]
    on_fo_se = [1,4,7]
    tw_fi_ei = [2,5,8]
    th_si_ni = [3,6,9]
    on_fi_ni = [1,5,9]
    th_fi_se = [3,5,7]

    # for C list 
    if all(value in our_C_list for value in on_tw_th):
        # line for 123
        t.penup()
        t.goto(-300, -200)
        t.pendown()
        t.goto(300, -200)
        t.hideturtle()

    elif all(value in our_C_list for value in fo_fi_si):
        # line for 456
        t.penup()
        t.goto(-300, 0)
        t.pendown()
        t.goto(300, 0)
        t.hideturtle()

    elif all(value in our_C_list for value in se_ei_ni):
        # line for 789
        t.penup()
        t.goto(-300, 200)
        t.pendown()
        t.goto(300, 200)
        t.hideturtle()

    elif all(value in our_C_list for value in on_fo_se):
        #  line for 147
        t.penup()
        t.goto(-200, -300)
        t.pendown()
        t.goto(-200, 300)
        t.hideturtle()

    elif all(value in our_C_list for value in tw_fi_ei):
        #  line for 258
        t.penup()
        t.goto(0, -300)
        t.pendown()
        t.goto(0, 300)
        t.hideturtle()

    elif all(value in our_C_list for value in th_si_ni):
        #  line for 369
        t.penup()
        t.goto(200, -300)
        t.pendown()
        t.goto(200, 300)
        t.hideturtle()

    elif all(value in our_C_list for value in on_fi_ni):
        #  line for 159
        t.penup()
        t.goto(300, 300)
        t.pendown()
        t.goto(-300, -300)
        t.hideturtle()

    elif all(value in our_C_list for value in th_fi_se):
        #  line for 357
        t.penup()
        t.goto(300, -300)
        t.pendown()
        t.goto(-300, 300)
        t.hideturtle()

    # for X list
    if all(value in our_X_list for value in on_tw_th):
        # line for 123
        t.penup()
        t.goto(-300, -200)
        t.pendown()
        t.goto(300, -200)
        t.hideturtle()

    elif all(value in our_X_list for value in fo_fi_si):
        # line for 456
        t.penup()
        t.goto(-300, 0)
        t.pendown()
        t.goto(300, 0)
        t.hideturtle()

    elif all(value in our_X_list for value in se_ei_ni):
        # line for 789
        t.penup()
        t.goto(-300, 200)
        t.pendown()
        t.goto(300, 200)
        t.hideturtle()

    elif all(value in our_X_list for value in on_fo_se):
        #  line for 147
        t.penup()
        t.goto(-200, -300)
        t.pendown()
        t.goto(-200, 300)
        t.hideturtle()

    elif all(value in our_X_list for value in tw_fi_ei):
        #  line for 258
        t.penup()
        t.goto(0, -300)
        t.pendown()
        t.goto(0, 300)
        t.hideturtle()

    elif all(value in our_X_list for value in th_si_ni):
        #  line for 369
        t.penup()
        t.goto(200, -300)
        t.pendown()
        t.goto(200, 300)
        t.hideturtle()

    elif all(value in our_X_list for value in on_fi_ni):
        #  line for 159
        t.penup()
        t.goto(300, 300)
        t.pendown()
        t.goto(-300, -300)
        t.hideturtle()

    elif all(value in our_X_list for value in th_fi_se):
        #  line for 357
        t.penup()
        t.goto(300, -300)
        t.pendown()
        t.goto(-300, 300)
        t.hideturtle()
    t.hideturtle()
        
# Main Game Loop
while True:
    wn.update()
    our_X()
    our_circle()
    winners_line()
    



