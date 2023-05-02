import turtle
import random
import time

# Set up the game window
window = turtle.Screen()
window.bgcolor("black")
window.title("Space Invaders")

# Create the player's spaceship
player = turtle.Turtle()
player.shape("triangle")
player.color("white")
player.penup()
player.speed(0)
player.setposition(0, -250)

# Set the player's movement speed
player_speed = 15

# Create a list of aliens
aliens = []
for i in range(5):
    alien = turtle.Turtle()
    alien.shape("circle")
    alien.color("green")
    alien.penup()
    alien.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    alien.setposition(x, y)
    aliens.append(alien)

# Set the alien movement speed
alien_speed = 2

# Create a list of bullets
bullets = []
for i in range(3):
    bullet = turtle.Turtle()
    bullet.shape("triangle")
    bullet.color("yellow")
    bullet.penup()
    bullet.speed(0)
    bullet.setheading(90)
    bullet.hideturtle()
    bullets.append(bullet)

# Set the bullet speed
bullet_speed = 20

# Set the score to 0
score = 0

# Set up the score display
score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.setposition(-280, 250)
score_string = "Score: %s" % score
score_display.write(score_string, False, align="left", font=("Arial", 14, "normal"))

# Set up the game over message
gameover_display = turtle.Turtle()
gameover_display.color("white")
gameover_display.penup()
gameover_display.hideturtle()
gameover_display.setposition(0, 0)

# Define the player's movement functions
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += player_speed
    if x > 280:
        x = 280
    player.setx(x)

# Set up the keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

# Start the game loop
while True:
    # Move the aliens
    for alien in aliens:
        x = alien.xcor()
        x += alien_speed
        alien.setx(x)
        # Check for collisions with the player's spaceship
        if alien.distance(player) < 20:
            gameover_display.write("Game Over", False, align="center", font=("Arial", 24, "normal"))
            time.sleep(3)
            window.bye()

        # Check for collisions with the bullets
        for bullet in bullets:
            if bullet.isvisible() and alien.distance(bullet) < 20:
                bullet.hideturtle()
                alien.hideturtle()
                aliens.remove(alien)
                score += 10
                score_string = "Score: %s" % score
                score_display.clear()
                score_display.write(score_string, False, align="left", font=("Arial", 14, "normal"))

    # Move the bullets
    for bullet in bullets:
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)

        # Check for collisions with the aliens
        for alien in aliens:
            if alien.isvisible() and alien.distance(bullet) < 20:
                bullet.hideturtle()
                alien.hideturtle()
                aliens.remove(alien)
                score += 10
                score_string = "Score: %s" % score
                score_display.clear()
                score_display.write(score_string, False, align="left", font=("Arial", 14, "normal"))

        # Check for collisions with the barriers
        # TODO: Implement barriers

        # Check if the bullet has gone offscreen
        if bullet.ycor() > 275:
            bullet.hideturtle()

    # Check if the player has won the game
    if not aliens:
        gameover_display.write("You Win!", False, align="center", font=("Arial", 24, "normal"))
        time.sleep(3)
        window.bye()

    # Delay the game loop
    time.sleep(0.05)
turtle.mainloop()
