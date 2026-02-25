import turtle, time, random
from utils import *
x1 = 0
y1 = 0 
# Section 1 - setup 
set_background("park")

t1 = create_sprite("pineapple",x1,y1)
#  the goal of the game is to get as many pineapples as possible on the screen
# OPTIONAL: use this invisible alien to say a message
# message_sprite = create_sprite("alien", -200,200)
# message_sprite.hideturtle()
message_sprite = create_sprite("pineapple",-200,200)
money = 0 
pineapple = 0

# Section 2 - controls
# TODO - define an action. ex: def my_control()

# TODO - choose a key to do the action. ex: window.onkeypress(my_control, "space")

# TODO - make a second control
def get_money():
    global money
   
    money += 5

window.onkeypress(get_money, "m")

def buy_pineapple():
    global pineapple, money
    if money >= 25:
        pineapple = create_sprite("pineapple", random.randint(-200,200), random.randint(-200,200))
        money -= 25
window.onkeypress(buy_pineapple,"space")

# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"Money: {money}\nPineapples: {pineapple}", font=("Arial", 30, "normal"))

    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()