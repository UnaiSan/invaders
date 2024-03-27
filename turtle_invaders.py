import turtle
import random
import time

window = turtle.Screen()
window.tracer(0)
window.setup(width=0.5, height=0.75)
window.bgcolor(0.2, 0.2, 0.2)
window.title("Turtle invaders!")

LEFT = -window.window_width() / 2
RIGHT = window.window_width() / 2
TOP = window.window_height() / 2
BOTTOM = -window.window_height() / 2
GUTTER = 0.025 * window.window_width()

FLOOR_LEVEL = 0.9 * BOTTOM

CANNON_STEP = 10
LASER_LENGTH = 20
LASER_SPEED = 10
ALIEN_SPAWN_INTERVAL_SECONDS = 1.2
ALIEN_SPEED = 2

lasers = []
aliens = []

def draw_cannon():
    cannon.clear()
    cannon.turtlesize(1, 4)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 10)
    cannon.turtlesize(1, 1.5)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 20)
    cannon.turtlesize(0.8, 0.3)
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL)

def move_left():
    new_x = cannon.xcor() - CANNON_STEP
    if new_x >= LEFT + GUTTER:
        cannon.setx(new_x)
        draw_cannon()

def move_right():
    new_x = cannon.xcor() + CANNON_STEP
    if new_x <= RIGHT - GUTTER:
        cannon.setx(new_x)
        draw_cannon()

def create_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color(1, 0, 0)
    laser.hideturtle()
    laser.setposition(cannon.position())
    laser.setheading(90.0)

    laser.forward(20)
    laser.pendown()
    laser.pensize(5)

    lasers.append(laser)

def move_laser(laser: turtle.Turtle):
    laser.clear()
    laser.forward(LASER_SPEED)
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)

def create_alien():
    alien = turtle.Turtle()
    alien.penup()
    alien.turtlesize(1.5)
    alien.setposition(
        x=random.randint(
            a=int(LEFT + GUTTER),
            b=int(RIGHT - GUTTER),
        ),
        y=TOP,
    )
    alien.shape("turtle")
    alien.setheading(-90.0)
    alien.color(random.random(), random.random(), random.random())
    aliens.append(alien)

if __name__ == "__main__":
    
    cannon = turtle.Turtle()
    cannon.penup()
    cannon.color(1, 1, 1)
    cannon.shape("square")
    cannon.setposition(0, FLOOR_LEVEL)

    window.onkeypress(move_left, "Left")
    window.onkeypress(move_right, "Right")
    window.onkeypress(turtle.bye, "q")
    window.onkeypress(create_laser, "space")
    window.listen()

    draw_cannon()

    alien_timer = 0
    while True:
        for laser in lasers.copy():
            move_laser(laser)
            if laser.ycor() > TOP:
                laser.clear()
                laser.hideturtle()
                lasers.remove(laser)
                turtle.turtles().remove(laser)

        if time.time() - alien_timer > ALIEN_SPAWN_INTERVAL_SECONDS:
            create_alien()
            alien_timer = time.time()
        
        for alien in aliens:
            alien.forward(ALIEN_SPEED)

        window.update()

    turtle.done()
