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
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("QB Test - Press Space for Red")
    
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    running = True
    start_time = time.time()
    
    while running:
        screen.fill(WHITE)
        current_time = time.time()
        turn_start_time = current_time  # Start of the current turn
        
        num_tries = 0
        score = 0
        
        while current_time - start_time < 120:  # 120 seconds = 2 minutes
            screen.fill(WHITE)
            current_time = time.time()
            
            # Check if current turn has exceeded 2 minutes
            if current_time - turn_start_time >= 120:
                break
            
            current_color = random.choice([RED, GREEN, BLUE])
            
            pygame.draw.circle(screen, current_color, (WIDTH // 2, HEIGHT // 2), SHAPE_RADIUS)
            display_text(screen, "Press Space when you see RED", font, (0, 0, 0), (WIDTH // 2, HEIGHT - 50))
            
            pygame.display.flip()
            clock.tick(FPS)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        num_tries += 1
                        if current_color == RED:
                            score += 1
                            feedback_message = "Correct!"
                            feedback_color = GREEN
                        else:
                            feedback_message = "Wrong!"
                            feedback_color = RED
                            
                        display_text(screen, feedback_message, font, feedback_color, (WIDTH // 2, HEIGHT // 2 + SHAPE_RADIUS + 50))
                        pygame.display.flip()
                        time.sleep(FEEDBACK_DISPLAY_TIME)  # Display feedback for a short time
        
        # Save the score for the turn
        save_score(score)
        
        # Display final score for the turn
        screen.fill(WHITE)
        display_text(screen, f"Correct: {score}", font, (0, 0, 0), (WIDTH // 2, HEIGHT // 2))
        pygame.display.flip()
        time.sleep(2)  # Display final score for 2 seconds

    pygame.quit()

if __name__ == "__main__":
    try:
        run_qb_test()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit(1)
