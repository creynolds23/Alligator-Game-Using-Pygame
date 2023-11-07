"""
Author: Conner Reynolds
Purpose: Alligator Game (Similar to the Snake game)
"""
# Main theme music came from humanoide9000

import pygame
import time
import random
import sys

pygame.init()
pygame.mixer.init()

# Load Sound files
eat_sound = pygame.mixer.Sound('531508__eponn__soft-dreamy-beep.wav')
in_game_sound = pygame.mixer.Sound('685841__humanoide9000__cinematic-battle-music-star-wars-style.mp3')
game_over_sound = pygame.mixer.Sound('382310__myfox14__game-over-arcade.wav')

distance_width = 700
distance_heigth = 500

dis = pygame.display.set_mode((distance_width, distance_heigth))
pygame.display.set_caption('Alligator game by Conner')

blue = (0, 0, 255)
red = (255, 0, 0)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)

alligator_block = 10
alligator_speed = 15
style_font = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 30)

clock = pygame.time.Clock()

# Functions to display the player's score
def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, green)
    dis.blit(value, [0, 0])

# Function to draw the player's alligator on the screen
def our_alligator(alligator_block, alligator_list):
    for x in alligator_list:
        pygame.draw.rect(dis, white, [x[0], x[1], alligator_block, alligator_block])

# Fuction to display a message on the screen
def message(msg, color):
    mesg = style_font.render(msg, True, color)
    dis.blit(mesg, [distance_width // 6, distance_heigth // 3])

# Main Game loop
def gameLoop():
    game_over = False

    while not game_over:
        in_game_sound.play(loops=-1)  # Start playing the in-game sound
        game_close = False

        x1 = distance_width // 2
        y1 = distance_heigth // 2

        x1_change = 0
        y1_change = 0

        alligator_list = []
        length_alligator = 1

        xfood = round(random.randrange(0, distance_width - alligator_block) / 10.0) * 10.0
        yfood = round(random.randrange(0, distance_width - alligator_block) / 10.0) * 10.0

        while not game_close:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -alligator_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = alligator_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -alligator_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = alligator_block
                        x1_change = 0

            if x1 >= distance_width or x1 < 0 or y1 >= distance_heigth or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change
            dis.fill(black)
            pygame.draw.rect(dis, yellow, [xfood, yfood, alligator_block, alligator_block])
            alligator_head = []
            alligator_head.append(x1)
            alligator_head.append(y1)
            alligator_list.append(alligator_head)
            if len(alligator_list) > length_alligator:
                del alligator_list[0]

            for x in alligator_list[:-1]:
                if x == alligator_head:
                    game_close = True

            our_alligator(alligator_block, alligator_list)
            your_score(length_alligator - 1)
            pygame.display.update()

            if x1 == xfood and y1 == yfood:
                eat_sound.play()  # Play the eat sound
                xfood = round(random.randrange(0, distance_width - alligator_block) / 10.0) * 10.0
                yfood = round(random.randrange(0, distance_heigth - alligator_block) / 10.0) * 10.0
                length_alligator += 1

            clock.tick(alligator_speed)

        in_game_sound.stop()  # Stop the in-game sound when the game is over
        game_over_sound.play()  # Play the game over sound

        dis.fill(black)
        message("You Lose! Press Q-Quit or C-Play", red)
        your_score(length_alligator - 1)
        pygame.display.update()

        user_input = None
        while user_input not in ('q', 'c'):
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        user_input = 'q'
                    elif event.key == pygame.K_c:
                        user_input = 'c'

        if user_input == 'q':
            game_over = True
        elif user_input == 'c':
            game_over_sound.stop()  # Stop the game over sound
            gameLoop()  # Restart the game

    pygame.quit()
    quit()

gameLoop()
