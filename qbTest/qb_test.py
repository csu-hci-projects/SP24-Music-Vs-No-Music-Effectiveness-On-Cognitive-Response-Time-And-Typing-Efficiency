import pygame # type: ignore
import random
import sys

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SHAPE_RADIUS = 50
FLASH_TIME = 1.0  # Time in seconds for each shape to flash

# Function to display text on the screen
def display_text(screen, text, font, color, position):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=position)
    screen.blit(text_surface, text_rect)

# Main function to run the QB test
def run_qb_test():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("QB Test - Press Space for Red")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    running = True

    while running:
        screen.fill(WHITE)

        # Generate a random color for the shape
        current_color = random.choice([RED, GREEN, BLUE])

        # Display flashing shape (circle)
        current_time = pygame.time.get_ticks() / 1000.0  # Convert to seconds
        if current_time % (2 * FLASH_TIME) < FLASH_TIME:
            pygame.draw.circle(screen, current_color, (WIDTH // 2, HEIGHT // 2), SHAPE_RADIUS)

        # Display instructions and feedback text
        display_text(screen, "Press Space when you see RED", font, BLACK, (WIDTH // 2, HEIGHT - 50))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if current_color == RED:
                        display_text(screen, "Correct!", font, GREEN, (WIDTH // 2, HEIGHT // 2 + SHAPE_RADIUS + 50))
                    else:
                        display_text(screen, "Wrong!", font, RED, (WIDTH // 2, HEIGHT // 2 + SHAPE_RADIUS + 50))

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
