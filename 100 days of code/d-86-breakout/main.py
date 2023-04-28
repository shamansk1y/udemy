import turtle
import random

# Set up the game screen
screen = turtle.Screen()
screen.title("Breakout Game")
screen.bgcolor("black")
screen.setup(width=600, height=800)

# Set up the game elements
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -350)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 3

bricks = []
colors = ["red", "orange", "yellow", "green", "blue"]
for i in range(5):
    for j in range(10):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color(colors[i])
        brick.shapesize(stretch_wid=1, stretch_len=4)
        brick.penup()
        brick.goto(-250 + j * 50, 250 - i * 25)
        bricks.append(brick)

# Set up the score
score = 0
score_pen = turtle.Turtle()
score_pen.hideturtle()
score_pen.color("white")
score_pen.penup()
score_pen.goto(0, 350)
score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Define the paddle movement function
def move_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

def move_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 20)

# Set up the keyboard bindings
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Define the main game loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for collisions with the walls
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 390:
        ball.dy *= -1

    if ball.ycor() < -390:
        score_pen.goto(0, 0)
        score_pen.write("Game Over", align="center", font=("Courier", 24, "normal"))
        break

    # Check for collisions with the paddle
    if ball.ycor() < -340 and ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50:
        ball.dy *= -1

    # Check for collisions with the bricks
    for brick in bricks:
        if ball.distance(brick) < 30:
            brick.hideturtle()
            bricks.remove(brick)
            score += 10
            score_pen.clear()
            score_pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
            ball.dy *= -1

    # Check if all the bricks are destroyed
    if not bricks:
        score_pen.goto(0, 0)
        score_pen.write("Level Complete", align="center", font=("Courier", 24, "normal"))
        break

# Wait for the user to close the window
screen.mainloop()
