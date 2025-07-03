import pygame
import sys
import random
import sqlite3

# === DATABASE SETUP ===

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("snake_game.db")
cur = conn.cursor()

# Create user table to store usernames (only one column: username)
cur.execute("""
CREATE TABLE IF NOT EXISTS user (
    username TEXT PRIMARY KEY
)
""")

# Create user_score table to store level and score for each user
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    username TEXT,
    level INTEGER,
    score INTEGER,
    FOREIGN KEY (username) REFERENCES user(username)
)
""")

conn.commit()  # Save changes to database

# === GET USERNAME ===

# Ask the user to enter their username
username = input("Enter your username: ")

# Check if the user already exists in the 'user' table
cur.execute("SELECT * FROM user WHERE username=?", (username,))
user = cur.fetchone()

# If user doesn't exist, insert new user and start from level 1, score 0
if not user:
    cur.execute("INSERT INTO user(username) VALUES(?)", (username,))
    conn.commit()
    level = 1
    score = 0
else:
    # If user exists, check if score and level were saved before
    cur.execute("SELECT level, score FROM user_score WHERE username=?", (username,))
    data = cur.fetchone()
    if data:
        level, score = data  # Load previous level and score
    else:
        level, score = 1, 0  # Start fresh if no score saved

print(f"Welcome, {username}! Starting at level {level} with score {score}")

# === PYGAME SETUP ===

pygame.init()
WIDTH, HEIGHT = 600, 400  # Size of game window
CELL_SIZE = 20            # Size of each snake segment
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)  # Font for score text

# === GAME LEVELS ===

# Each level has a speed and optional wall obstacles
levels = {
    1: {'speed': 10, 'walls': []},
    2: {'speed': 15, 'walls': [(200, 200, 200, 20), (100, 100, 20, 200)]},
    3: {'speed': 20, 'walls': [(150, 150, 300, 20), (150, 230, 20, 120)]}
}

# === INITIAL SNAKE AND FOOD ===

# Snake starts with 3 blocks moving to the right
snake = [(100, 50), (80, 50), (60, 50)]
direction = (CELL_SIZE, 0)

# Generate random position for food
food = (
    random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
    random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
)

paused = False  # Pause flag

# === HELPER FUNCTIONS ===

# Draw wall rectangles on screen
def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, (255, 0, 0), wall)

# Save current progress to database
def save_progress():
    cur.execute("DELETE FROM user_score WHERE username=?", (username,))
    cur.execute(
        "INSERT INTO user_score(username, level, score) VALUES (?, ?, ?)",
        (username, level, score)
    )
    conn.commit()

# End game and save score
def game_over():
    global running
    save_progress()
    print("Game Over! Your score:", score)
    pygame.quit()
    sys.exit()

# === MAIN GAME LOOP ===

running = True
while running:
    clock.tick(levels[level]['speed'])  # Control game speed

    # Handle events (keyboard or quit)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress()
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                # Toggle pause and save progress
                paused = not paused
                if paused:
                    save_progress()

            # Control snake direction with arrow keys
            elif event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    if paused:
        continue  # If paused, skip game logic

    # === Move snake ===
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.insert(0, new_head)  # Add new head to snake

    # === Collision detection ===
    # Check if snake hits wall of screen or itself
    if (
        new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
        new_head in snake[1:]
    ):
        game_over()

    # Check if snake hits any walls for current level
    for wall in levels[level]['walls']:
        if pygame.Rect(wall).collidepoint(new_head):
            game_over()

    # === Check food collision ===
    if new_head == food:
        score += 10  # Increase score
        # Go to next level if score reaches threshold
        if score >= level * 50 and level < len(levels):
            level += 1
        # Generate new food
        food = (
            random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
        )
    else:
        snake.pop()  # Remove tail unless food is eaten

    # === Drawing everything ===
    screen.fill((0, 0, 0))  # Clear screen (black)

    draw_walls(levels[level]['walls'])  # Draw walls

    # Draw snake
    for block in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*block, CELL_SIZE, CELL_SIZE))

    # Draw food
    pygame.draw.rect(screen, (255, 255, 0), (*food, CELL_SIZE, CELL_SIZE))

    # Draw score and level info
    score_text = font.render(
        f"User: {username}  Level: {level}  Score: {score}", True, (255, 255, 255)
    )
    screen.blit(score_text, (10, 10))

    pygame.display.flip()  # Update the screen

# === Exit and cleanup ===
save_progress()
pygame.quit()
conn.close()
