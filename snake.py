import curses
from random import randint

# Initialize the screen
screen = curses.initscr()
curses.curs_set(0)
screen_height, screen_width = screen.getmaxyx()
window = curses.newwin(screen_height, screen_width, 0, 0)
window.keypad(1)
window.timeout(100)

# Initial snake position and food
snake_x = screen_width // 4
snake_y = screen_height // 2
snake = [[snake_y, snake_x], [snake_y, snake_x - 1], [snake_y, snake_x - 2]]
food = [screen_height // 2, screen_width // 2]
window.addch(food[0], food[1], curses.ACS_PI)

# Initialize game variables
score = 0
key = curses.KEY_RIGHT

# Game logic
while True:
    next_key = window.getch()
    key = key if next_key == -1 else next_key

    # Check if snake hits the wall or itself
    if (snake[0][0] in [0, screen_height] or
            snake[0][1] in [0, screen_width] or
            snake[0] in snake[1:]):
        curses.endwin()
        quit()

    # Calculate new head position
    new_head = [snake[0][0], snake[0][1]]

    # Update snake direction based on input
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    # Insert new head
    snake.insert(0, new_head)

    # Check if snake eats food
    if snake[0] == food:
        score += 1
        food = None
        while food is None:
            nf = [randint(1, screen_height - 1), randint(1, screen_width - 1)]
            food = nf if nf not in snake else None
        window.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail = snake.pop()
        window.addch(tail[0], tail[1], ' ')

    # Add new head
    window.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

    # Display score
    window.addstr(0, 2, 'Score: ' + str(score) + ' ')

    # Refresh screen
    window.refresh()

curses.endwin()
