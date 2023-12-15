import pygame
import numpy as np
import time
import snake_body
import sys

def generate_food_pos():
    food_x = np.random.randint(0,50)*10
    food_y = np.random.randint(0,50)*10
    return food_x, food_y


def add_score(score):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score = " + str(score - 1), True, (255,255,255))
    window.blit(text,(0,0))
    pygame.display.flip()


def place_food(food_x, food_y):
    pygame.draw.rect(window, (255, 255, 255), (food_x, food_y, 10, 10), width=5, border_radius=10)


x = 500
y = 500
x_pos = x/2
y_pos = y/2
snake_pos_i = (x_pos, y_pos)
snake_inst = snake_body.SnakeBody(snake_pos_i)

pygame.init()

window = pygame.display.set_mode((x, y))

run = True

f_x, f_y = generate_food_pos()
place_food(f_x,f_y)
persist_food = True

direction = 1
prev_direction = direction

f_x, f_y = generate_food_pos()
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if prev_direction == 2:
                    direction = 2
                else: direction = 1

                prev_direction = direction

            if event.key == pygame.K_s:
                if prev_direction == 2:
                    direction = 1
                else: direction = 2

                prev_direction = direction

            if event.key == pygame.K_a:
                if prev_direction == 4:
                    direction = 4
                else: direction = 3

                prev_direction = direction

            if event.key == pygame.K_d:
                if prev_direction == 3:
                    direction = 3

                else:direction = 4
                prev_direction = direction

    if direction == 1:
        y_pos -= 10
    if direction == 2:
        y_pos += 10
    if direction == 3:
        x_pos -= 10
    if direction == 4:
        x_pos += 10

    snake_inst.update_snake([x_pos, y_pos])

    window.fill(0)

    place_food(f_x, f_y)

    if persist_food:
        place_food(f_x, f_y)
    else:
        f_x, f_y = generate_food_pos()
        place_food(f_x, f_y)
        persist_food = True

    for m in range(len(snake_inst.snake_to_plot)):
        pygame.draw.rect(window, (255, 0, 0), (snake_inst.snake_to_plot[m][0], snake_inst.snake_to_plot[m][1], 10, 10), width=50, border_radius=1)

    if snake_inst.fail_condition:

        for i in range(6):

            for m in range(len(snake_inst.snake_to_plot)):
                pygame.draw.rect(window, (255, 0, 255),
                                 (snake_inst.snake_to_plot[m][0], snake_inst.snake_to_plot[m][1], 10, 10), width=50,
                                 border_radius=1)
            pygame.display.update()

            time.sleep(0.1)

            for m in range(len(snake_inst.snake_to_plot)):
                pygame.draw.rect(window, (255, 255, 0),
                                 (snake_inst.snake_to_plot[m][0], snake_inst.snake_to_plot[m][1], 10, 10), width=50,
                                 border_radius=1)
            pygame.display.update()

            time.sleep(0.5)

        pygame.quit()

    time.sleep(0.2-(0.005*snake_inst.food_aquired))

    if x_pos < 0:
        x_pos = x

    if x_pos > x:
        x_pos = -10

    if y_pos < 0:
        y_pos = y

    if y_pos > y:
        y_pos = -10

    if x_pos == f_x and y_pos == f_y:
        persist_food = False
        snake_inst.food_aquired += 1

    add_score(snake_inst.food_aquired)

pygame.quit()

exit()

