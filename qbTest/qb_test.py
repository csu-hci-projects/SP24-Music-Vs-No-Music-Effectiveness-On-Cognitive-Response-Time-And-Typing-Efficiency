import pygame 
import random
import sys
import time  # Import the time module for timing

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
FLASH_TIME = 1.0  # Time in seconds for each shape to flash
PAUSE_TIME = 0.5  # Time in seconds to pause between flashes
FEEDBACK_DISPLAY_TIME = 0.65  # Time in seconds to display feedback (Correct or Wrong)
SCORE_FILE = "scores.txt"  # File to save scores

# Function to display text on the screen
def display_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)
    return text_surface.get_rect()

# Function to save score to a file
def save_score(score):
    with open(SCORE_FILE, "a") as file:
        file.write(f"{score}\n")


# Main function to run the QB test
def run_qb_test():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    pygame.display.set_caption("QB Test - Press Space for Red")
    
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    running = False
    start_screen = True
    game_ended = False
    last_flash_time = time.time()  # Track the last time a shape was flashed
    last_feedback_time = 0.0  # Track the last time feedback was displayed
    flash_complete = True  # Flag to track if a flash cycle is complete
    feedback_displayed = False  # Flag to track if feedback is currently displayed
    score = 0
    start_time = time.time()
    
    while start_screen:
        screen.fill(WHITE)
        display_text(screen, "QB Test", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 4))
        display_text(screen, "This test will exit on its own after 2 minutes.", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 - 50))
        display_text(screen, "Press Space to Start", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 + 50))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_screen = False
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_screen = False
                    running = True
                    break

        pygame.display.flip()
        clock.tick(FPS)

    last_flash_time = time.time()
    last_feedback_time = 0.0
    flash_complete = True
    feedback_displayed = False
    score = 0
    start_time = time.time()
    
    while running:
        screen.fill(WHITE)

        current_time = time.time()

        if flash_complete:
            # Generate a random color for the shape
            current_color = random.choice([RED, GREEN, BLUE])
            flash_complete = False
            last_flash_time = current_time  # Reset the last flash time

        # Determine if it's time to show the shape or pause
        if current_time - last_flash_time < FLASH_TIME:
            # Display flashing shape (circle)
            pygame.draw.circle(screen, current_color, (WIDTH // 2, HEIGHT // 2), SHAPE_RADIUS)
        elif current_time - last_flash_time < FLASH_TIME + PAUSE_TIME:
            # Pause between flashes
            pass
        else:
            # Reset for the next flash cycle
            flash_complete = True

        # Display instructions
        display_text(screen, "Press Space when you see RED", font, (0, 0, 0), (WIDTH // 2, HEIGHT - 50))



        # Check for feedback display
        if current_time - last_feedback_time < FEEDBACK_DISPLAY_TIME and feedback_displayed:
            # Display the feedback message (Correct or Wrong)
            display_text(screen, feedback_message, font, feedback_color, feedback_position)
        else:
            feedback_displayed = False

        # Event handling
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

        # Check for game end condition (e.g., after 2 mins)
        current_time = time.time()
        elapsed_time = current_time - start_time
        if elapsed_time >= 120:  # 120 seconds = 2 minutes
            save_score(score)
            display_text(screen, f"Correct: {score}", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)  # Display final score for 2 seconds
            running = False

        pygame.display.flip()  # Update display
        clock.tick(FPS)  # Cap the frame rate

    while game_ended:
        screen.fill(WHITE)
        display_text(screen, "QB Test", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 4))
        display_text(screen, "This test will exit on its own after 2 minutes.", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 - 50))
        display_text(screen, "Press Space to Start", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2 + 50))
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_ended = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_ended = False
                        running = True
                        start_time = time.time()
                        score = 0
                        break

        pygame.display.flip()
        clock.tick(FPS)


    pygame.quit()  # Clean up resources

# Run the QB test
if __name__ == "__main__":
    try:
        run_qb_test()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
