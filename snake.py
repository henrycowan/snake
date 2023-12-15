import pygame
import numpy as np
import time
import snake_body
import sys



class Snake:

    def __init__(self):

        #/ Setting Constants/

        self.x = 500
        self.y = 500
        self.x_pos = self.x/2
        self.y_pos = self.y/2
        self.snake_pos_i = (self.x_pos, self.y_pos)
        self.snake_inst = snake_body.SnakeBody(self.snake_pos_i)
        self.persist_food = True
        self.run = True
        self.food_x, self.food_y = 0, 0
        self.direction = 1
        self.prev_direction = self.direction
        self.delay = 0.1

        #/ Start Pygame lib/
        pygame.init()

        #/create window/
        self.window = pygame.display.set_mode((self.x, self.y))

        #/create inital food coords and put on screen/
        self.generate_food_pos()
        self.place_food()

    #/generate random x,y coord for food placement/
    def generate_food_pos(self):
        self.food_x = np.random.randint(0, 50) * 10
        self.food_y = np.random.randint(0, 50) * 10

    #/add score to the screen/
    def add_score(self, score):
        font = pygame.font.SysFont(None, 25)
        text = font.render("Score = " + str(score - 1), True, (255, 255, 255))
        self.window.blit(text, (0, 0))
        pygame.display.flip()

    #/draw the food on the screen/
    def place_food(self):
        pygame.draw.rect(self.window, (255, 255, 255), (self.food_x, self.food_y, 10, 10), width=5, border_radius=10)

    def check_key_press(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if self.prev_direction == 2:
                        self.direction = 2
                    else:
                        self.direction = 1

                    self.prev_direction = self.direction

                if event.key == pygame.K_s:
                    if self.prev_direction == 2:
                        self.direction = 1
                    else:
                        self.direction = 2

                    self.prev_direction = self.direction

                if event.key == pygame.K_a:
                    if self.prev_direction == 4:
                        self.direction = 4
                    else:
                        self.direction = 3

                    self.prev_direction = self.direction

                if event.key == pygame.K_d:
                    if self.prev_direction == 3:
                        self.direction = 3

                    else:
                        self.direction = 4
                    self.prev_direction = self.direction

    def increment_position(self):
        if self.direction == 1:
            self.y_pos -= 10
        if self.direction == 2:
            self.y_pos += 10
        if self.direction == 3:
            self.x_pos -= 10
        if self.direction == 4:
            self.x_pos += 10

    def add_new_food(self):
        if self.persist_food:
            self.place_food()
        else:
            self.generate_food_pos()
            self.place_food()
            self.persist_food = True

    def draw_snake(self):
        for m in range(len(self.snake_inst.snake_to_plot)):
                pygame.draw.rect(self.window, (255, 0, 0), (self.snake_inst.snake_to_plot[m][0], self.snake_inst.snake_to_plot[m][1], 10, 10), width=50, border_radius=1)

    def run_fail_blink(self):

        for i in range(6):

            for m in range(len(self.snake_inst.snake_to_plot)):
                pygame.draw.rect(self.window, (255, 0, 255),
                                 (self.snake_inst.snake_to_plot[m][0], self.snake_inst.snake_to_plot[m][1], 10, 10),
                                 width=50,
                                 border_radius=1)
            pygame.display.update()

            time.sleep(0.1)

            for m in range(len(self.snake_inst.snake_to_plot)):
                pygame.draw.rect(self.window, (255, 255, 0),
                                 (self.snake_inst.snake_to_plot[m][0], self.snake_inst.snake_to_plot[m][1], 10, 10),
                                 width=50,
                                 border_radius=1)
            pygame.display.update()

            time.sleep(0.5)

        pygame.quit()

    def snake_wraparound(self):

        if self.x_pos < 0:
            self.x_pos = self.x

        if self.x_pos > self.x:
            self.x_pos = -10

        if self.y_pos < 0:
            self.y_pos = self.y

        if self.y_pos > self.y:
            self.y_pos = -10

    def check_if_eaten(self):

        if self.x_pos == self.food_x and self.y_pos == self.food_y:
            self.persist_food = False
            self.snake_inst.food_aquired += 1

    def increment_delay(self):
        self.delay = self.delay - (0.005 * self.snake_inst.food_aquired)

    #/run the game/
    def main(self):
        while self.run:

            self.check_key_press()

            self.increment_position()

            self.snake_inst.update_snake([self.x_pos, self.y_pos])

            self.window.fill(0)

            self.place_food()

            self.add_new_food()

            self.draw_snake()

            if self.snake_inst.fail_condition:

                self.run_fail_blink()

            self.snake_wraparound()

            time.sleep(self.delay)

            if self.check_if_eaten():
                self.increment_delay()

            self.add_score(self.snake_inst.food_aquired)

        pygame.quit()

        sys.exit()

game = Snake()
game.main()