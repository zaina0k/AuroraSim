import pygame  # type: ignore
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Constellation Drawer")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Constellation points
constellation_points = []

def draw_constellation():
    screen.fill(BLACK)  # Fill the screen with black

    # Draw the lines connecting the constellation points
    if len(constellation_points) > 1:
        for i in range(len(constellation_points) - 1):
            pygame.draw.line(screen, WHITE, constellation_points[i], constellation_points[i + 1], 2)

    # Draw the constellation points
    for point in constellation_points:
        pygame.draw.circle(screen, WHITE, point, 5)

    pygame.display.flip()  # Update the display

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                constellation_points.append((x, y))
                draw_constellation()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
