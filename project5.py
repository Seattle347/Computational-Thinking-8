import turtle, math, time, random
from utils import *

# Section 1: Setup
x1=-250
y1=0
x2=250
y2=0




# TODO - create your player character and any other sprites
s1 = create_sprite("pineapple",x1,y1)
s2 = create_sprite("mango",x2,y2)
set_background("cornfield")

tagger = "pineapple"

def move_up():
    x = s1.xcor()
    y = s1.ycor() + 44
    s1.goto(x,y)

def move_down():
    x = s1.xcor()
    y = s1.ycor() - 44
    s1.goto(x,y)

def move_left():
    x = s1.xcor() - 44
    y = s1.ycor()
    s1.goto(x,y)

def move_right():
    x = s1.xcor() + 44
    y = s1.ycor()
    s1.goto(x,y)

def draw():
    s1.pendown()

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right, "d")

def move_up():
    x = s2.xcor()
    y = s2.ycor() + 45
    s2.goto(x,y)

def move_down():
    x = s2.xcor()
    y = s2.ycor() - 45
    s2.goto(x,y)

def move_left():
    x = s2.xcor() - 45
    y = s2.ycor()
    s2.goto(x,y)

def move_right():
    x = s2.xcor() + 45
    y = s2.ycor()
    s2.goto(x,y)

window.onkeypress(move_up, "Up")
window.onkeypress(move_down, "Down")
window.onkeypress(move_left, "Left")
window.onkeypress(move_right, "Right")
    
        


# TODO - set the starting value for your variables
sprite_list = []

# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    if get_distance(s1,s2) < 200:
        if tagger == "mango":
            s1.write("Tag!", font=("Arial", 15, "normal"))
            tagger = "pineapple"
        elif tagger == "pineapple":
            s2.write("Tag!", font=("Arial", 15, "normal"))
            tagger = "mango"
            s1.write("Tag!", font=("Arial", 15, "normal"))

        if i >= 8 * 100: 
           break
    

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")
print("The winner is", tagger)