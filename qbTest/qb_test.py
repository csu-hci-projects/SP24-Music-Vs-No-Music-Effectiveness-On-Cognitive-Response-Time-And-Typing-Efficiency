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
FEEDBACK_DISPLAY_TIME = 2.0  # Time in seconds to display feedback (Correct or Wrong)

# Function to display text on the screen
def display_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)
    return text_surface.get_rect()

# Main function to run the QB test
def run_qb_test():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("QB Test - Press Space for Red")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    running = True
    last_flash_time = time.time()  # Track the last time a shape was flashed
    last_feedback_time = 0.0  # Track the last time feedback was displayed
    flash_complete = True  # Flag to track if a flash cycle is complete
    feedback_displayed = False  # Flag to track if feedback is currently displayed

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
                    else:
                        feedback_message = "Wrong!"
                        feedback_color = RED
                    feedback_position = (WIDTH // 2, HEIGHT // 2 + SHAPE_RADIUS + 50)
                    last_feedback_time = current_time
                    feedback_displayed = True

        pygame.display.flip()  # Update display
        clock.tick(FPS)  # Cap the frame rate

    pygame.quit()  # Clean up resources

# Run the QB test
if __name__ == "__main__":
    try:
        run_qb_test()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
