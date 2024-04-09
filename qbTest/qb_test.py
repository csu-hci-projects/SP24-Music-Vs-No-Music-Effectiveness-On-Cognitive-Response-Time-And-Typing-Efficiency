import pygame # type: ignore
import random

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
SHAPE_COLORS = [RED, GREEN, BLUE]
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
    pygame.display.set_caption("QB Test - Press Space for Correct Color")

    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    running = True
    current_color = random.choice(SHAPE_COLORS)
    start_time = pygame.time.get_ticks()
    correct_shape_displayed = False

    while running:
        screen.fill(WHITE)
        current_time = (pygame.time.get_ticks() - start_time) / 1000.0

        # Display flashing shape
        if current_time % (2 * FLASH_TIME) < FLASH_TIME:
            pygame.draw.circle(screen, current_color, (WIDTH // 2, HEIGHT // 2), SHAPE_RADIUS)

        # Check for user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if current_color == RED:
                        correct_shape_displayed = True
                    else:
                        correct_shape_displayed = False

        # Display instructions and feedback
        display_text(screen, "Press Space when you see RED", font, BLACK, (WIDTH // 2, HEIGHT - 50))

        if correct_shape_displayed:
            display_text(screen, "Correct!", font, GREEN, (WIDTH // 2, HEIGHT // 2 + SHAPE_RADIUS + 50))
        else:
            display_text(screen, "Wrong!", font, RED, (WIDTH // 2, HEIGHT // 2 + SHAPE_RADIUS + 50))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

# Run the QB test
run_qb_test()
