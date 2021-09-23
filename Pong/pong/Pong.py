import sys
import pygame
import random

def ball_animation():
    # To let python know that a variable is already declared globally and not only locally
    global ball_speed_x, ball_speed_y, score_red, score_blue, img_red, img_blue

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Create a "bouncy" ball
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        score_red += 1
        img_red = font.render("YOU: " + str(score_red), True, light_grey)
        ball_restart()

    if ball.right >= screen_width:
        score_blue += 1
        img_blue = font.render("OPPONENT: " + str(score_blue), True, light_grey)
        ball_restart()

    # Let the player rectangles trigger a collision
    if ball.colliderect(red) or ball.colliderect(blue):
        ball_speed_x *= -1

def red_player_animation():
    red.y += red_speed
    if red.top <= 0:
        red.top = 0
    if red.bottom >= screen_height:
        red.bottom = screen_height

def blue_player_animation():
    if blue.top < ball.y:
        blue.top += blue_speed
    if blue.bottom > ball.y:
        blue.bottom -= blue_speed
    if blue.top <= 0:
        blue.top = 0
    if blue.bottom >= screen_height:
        blue.bottom = screen_height

def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x += random.choice((1, -1))


# General setup
pygame.init()
clock = pygame.time.Clock()

# Creating a window with pygame
screen_width = 800
screen_height = 600
# This line returns the "Screen" in an object
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PongGame")

# Game Rectangles
# The three lines below create three empty rectangles to draw them I need pygame.draw(surface, color, rect)
# screen_width/2 -15, screen_height/2 -15 is to perfectly center the ball as it otherwise would be a tad off the middle
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
red = pygame.Rect(screen_width - 20, screen_height/2-50, 10, 100)
blue = pygame.Rect(10, screen_height/2-50, 10, 100)

# Create Colors
bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)
light_red = (255, 127, 127)
light_blue = (179, 204, 245)

# Scoreboard
score_red = 0
score_blue = 0
font = pygame.font.SysFont(None, 24)
img_red = font.render("YOU: " + str(score_red), True, light_grey)
img_blue = font.render("OPPONENT: " + str(score_blue), True, light_grey)


# Animation needed variables
ball_speed_x = 5 * random.choice((1, -1))
ball_speed_y = 5 * random.choice((1, -1))
red_speed = 0
blue_speed = 5.5

# Running the Game
while score_red < 15 and score_blue < 15:
    #TODO: Show winner screen

    # Handling the input
    # With pygame.event.get() I'll get any event triggered by the user
    for event in pygame.event.get():
        # This just asked if the user closed the window or not
        if event.type == pygame.QUIT:
            # Closes the pyGame
            pygame.quit()
            # Closes the programme
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                red_speed += 5
            if event.key == pygame.K_UP:
                red_speed -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                red_speed -= 5
            if event.key == pygame.K_UP:
                red_speed += 5


    ball_animation()
    red_player_animation()
    blue_player_animation()


    # Visuals
    # NOTE: Everything is drawn from top to bottom
    # To fill the background
    screen.fill(bg_color)
    screen.blit(img_blue, (20, 20))
    screen.blit(img_red, (screen_width - (img_red.get_width() + 20), 20))
    pygame.draw.rect(screen, light_red, red)
    pygame.draw.rect(screen, light_blue, blue)
    pygame.draw.ellipse(screen, light_grey, ball)
    # A line to separate the sides
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))

    # Updating the window
    # This line draws the picture itself
    pygame.display.flip()
    # Limits how fast the loop runs (In this case 60 times per second)
    clock.tick(60)



