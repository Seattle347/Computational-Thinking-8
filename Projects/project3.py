import turtle, time, random
from utils import *

# Section 1 - Variables
# TODO - add starting values for all the variables
x1 = -260
y1 = 200
x2 = -260
y2 = 0
x3 = -260
y3 = -150
x4 = -260
y4 = -215


# Section 2 - Setup
# # TODO - use your own background, and set your four turtles to images of your choice
set_background("underwater")
t1 = create_sprite("lasagna",x1,y1)
t2 = create_sprite("bike",x2,y2)
t3 = create_sprite("cool_dog",x3,y3)
t4 = create_sprite("basketball",x4,y4)


# # Section 3 - Racing
# # TODO - set how much each variable changes by and increase the number of repeats to at least 30
# # TODO - explain here which sprites are faster or slower
for i in range(15):
    x1 += 15
    x2 += 35
    x3 += 27
    x4 += 32

    t1.goto(x1, y1)
    t2.goto(x2, y2)
    t3.goto(x3, y3)
    t4.goto(x4, y4)

    window.update()
    time.sleep(0.1)


# # Section 4 - Winner
# # TODO - complete the elif for player 2 winning
# # TODO - write another elif for player 3 and player 4
if x1 >= x2 and x1 >= x3 and x1 >= x4:
    print("lasagna wins!")
elif x2 >= x1 and x2 >= x3 and x2 >=x4:
   print("bike wins!")
elif x3 >= x1 and x3 >= x2 and x3 >=x4:
    print ("cool_dog wins!")
elif x4 >= x1 and x4 >= x2 and x4 >=x3:
    print("basketball wins")


turtle.exitonclick()