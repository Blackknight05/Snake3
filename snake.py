import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set the width and height of the screen (in pixels)
WIDTH, HEIGHT = 600, 400

# Set the size of each grid cell
GRID_SIZE = 20

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Define the Snake class
class Snake:
    def __init__(self):
        self.body = [(WIDTH / 2, HEIGHT / 2)]
        self.direction = "RIGHT"
        self.change_to = self.direction

    def change_direction_to(self, dir):
        if dir == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"
        if dir == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if dir == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"

    def move(self, food_pos):
        if self.direction == "RIGHT":
            new_head = (self.body[0][0] + GRID_SIZE, self.body[0][1])
        if self.direction == "LEFT":
            new_head = (self.body[0][0] - GRID_SIZE, self.body[0][1])
        if self.direction == "UP":
            new_head = (self.body[0][0], self.body[0][1] - GRID_SIZE)
        if self.direction == "DOWN":
            new_head = (self.body[0][0], self.body[0][1] + GRID_SIZE)

        self.body.insert(0, new_head)

        if self.body[0] == food_pos:
            return True
        else:
            self.body.pop()
            return False

    def check_collision(self):
        if (
            self.body[0][0] >= WIDTH
            or self.body[0][0] < 0
            or self.body[0][1] >= HEIGHT
            or self.body[0][1] < 0
        ):
            return True
        for block in self.body[1:]:
            if self.body[0] == block:
                return True
        return False

    def get_head_position(self):
        return self.body[0]

    def get_body(self):
        return self.body


# Define the Food class
class Food:
    def __init__(self):
        self.position = (
            random.randrange(0, WIDTH - GRID_SIZE, GRID_SIZE),
            random.randrange(0, HEIGHT - GRID_SIZE, GRID_SIZE),
        )
        self.is_food_on_screen = True

    def spawn_food(self):
        if not self.is_food_on_screen:
            self.position = (
                random.randrange(0, WIDTH - GRID_SIZE, GRID_SIZE),
                random.randrange(0, HEIGHT - GRID_SIZE, GRID_SIZE),
            )
            self.is_food_on_screen = True
        return self.position

    def set_food_on_screen(self, boolean):
        self.is_food_on_screen = boolean


# Main function to run the game
def main():
    snake = Snake()
    food = Food()

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction_to("LEFT")
                if event.key == pygame.K_RIGHT:
                    snake.change_direction_to("RIGHT")
                if event.key == pygame.K_UP:
                    snake.change_direction_to("UP")
                if event.key == pygame.K_DOWN:
                    snake.change_direction_to("DOWN")

        # Move the snake
        food_pos = food.spawn_food()
        if snake.move(food_pos):
            food.set_food_on_screen(False)

        # Check for collisions
        if snake.check_collision():
            break

        # Draw everything
        screen.fill(BLACK)
        for pos in snake.get_body():
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))

        pygame.display.flip()

        # Control the game's speed
        clock.tick(10)

    pygame.quit()


if __name__ == "__main__":
    main()
