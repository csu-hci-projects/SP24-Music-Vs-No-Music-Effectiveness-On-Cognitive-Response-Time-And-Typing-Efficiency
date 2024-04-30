import pygame
import random
import sys
import time

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SHAPE_RADIUS = 50
FLASH_TIME = 1.0
PAUSE_TIME = 0.5
FEEDBACK_DISPLAY_TIME = 0.65
SCORE_FILE = "scores.txt"
TIME_LIMIT = 120  # Time limit in seconds (2 minutes)

# Function to display text on the screen
def display_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

# Function to save score to a file
def save_score(score):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{score}\n")

# Main function to run the QB test
def run_qb_test():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("QB Test")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    running = False
    start_screen = True

    while start_screen:
        screen.fill(WHITE)
        display_text(screen, "QB Test", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 4))
        display_text(screen, "This test will last 2 minutes.", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 - 50))
        display_text(screen, "Press Space to Start", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 + 50))
        display_text(screen, "Press Space when you see RED", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 + 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_screen = False
                    running = True
                    start_time = time.time()  # Start time for the game

        pygame.display.flip()
        clock.tick(FPS)

    score = 0
    last_flash_time = time.time()
    last_feedback_time = 0.0
    flash_complete = True
    feedback_displayed = False

    while running:
        screen.fill(WHITE)

        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= TIME_LIMIT:
            # Time limit exceeded, end the game
            save_score(score)
            display_text(screen, f"Correct: {score}", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            running = False

        if flash_complete:
            current_color = random.choice([RED, GREEN, BLUE])
            flash_complete = False
            last_flash_time = current_time

        if current_time - last_flash_time < FLASH_TIME:
            pygame.draw.circle(screen, current_color, (WIDTH // 2, HEIGHT // 2), SHAPE_RADIUS)
        elif current_time - last_flash_time < FLASH_TIME + PAUSE_TIME:
            pass
        else:
            flash_complete = True

        # Display text for pressing space above the shapes
        display_text(screen, "Press Space when you see RED", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 4))

        if current_time - last_feedback_time < FEEDBACK_DISPLAY_TIME and feedback_displayed:
            display_text(screen, feedback_message, font, feedback_color, feedback_position)
        else:
            feedback_displayed = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not feedback_displayed:
                    if current_color == RED:
                        feedback_message = "Correct!"
                        feedback_color = GREEN
                        score += 1
                    else:
                        feedback_message = "Wrong!"
                        feedback_color = RED
                    feedback_position = (WIDTH // 2, HEIGHT // 2 + SHAPE_RADIUS + 50)
                    last_feedback_time = current_time
                    feedback_displayed = True

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    try:
        run_qb_test()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
