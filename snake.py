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

# Set up the display
WIDTH, HEIGHT = 600, 400
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Snake variables
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]
snake_direction = "RIGHT"
change_to = snake_direction
snake_speed = 10

# Food variables
food_pos = [random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
            random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE]
food_spawn = True

# Score variable
score = 0

# Function to display the score
def display_score(score):
    font = pygame.font.SysFont("arial", 25)
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, [0, 0])

# Main game function
def main():
    global change_to, snake_direction, food_pos

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = "UP"
                elif event.key == pygame.K_DOWN:
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT:
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    change_to = "RIGHT"

        if change_to == "UP" and snake_direction != "DOWN":
            snake_direction = "UP"
        if change_to == "DOWN" and snake_direction != "UP":
            snake_direction = "DOWN"
        if change_to == "LEFT" and snake_direction != "RIGHT":
            snake_direction = "LEFT"
        if change_to == "RIGHT" and snake_direction != "LEFT":
            snake_direction = "RIGHT"

        if snake_direction == "UP":
            snake_pos[1] -= GRID_SIZE
        if snake_direction == "DOWN":
            snake_pos[1] += GRID_SIZE
        if snake_direction == "LEFT":
            snake_pos[0] -= GRID_SIZE
        if snake_direction == "RIGHT":
            snake_pos[0] += GRID_SIZE

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (WIDTH//GRID_SIZE)) * GRID_SIZE,
                        random.randrange(1, (HEIGHT//GRID_SIZE)) * GRID_SIZE]
        food_spawn = True

        screen.fill(WHITE)

        for pos in snake_body:
            pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE))

        pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], GRID_SIZE, GRID_SIZE))

        # Check if the snake hits itself or the wall
        if snake_pos[0] < 0 or snake_pos[0] > WIDTH - GRID_SIZE:
            game_over = True
        if snake_pos[1] < 0 or snake_pos[1] > HEIGHT - GRID_SIZE:
            game_over = True
        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over = True

        display_score(score)

        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(snake_speed)

    pygame.quit()

if __name__ == "__main__":
    main()
