import pygame # type: ignore
from pygame.locals import * # type: ignore
import sys
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 750

class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 72)
        self.title = self.title_font.render("Constellation Game", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.text = self.font.render("Press SPACE to start", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 150))
        self.button = self.font.render("Start", True, (255, 255, 255))
        self.button_color = (50, 200, 50)  # RGB color for the button
        self.button_rect = pygame.Rect(SCREEN_WIDTH - 250, SCREEN_HEIGHT - 100, 200, 60)



    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    return "gameplay"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title, self.title_rect.topleft)
        screen.blit(self.text, self.text_rect.topleft)
        screen.blit(self.button, self.button_rect.bottomright)

class Gameplay:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title = self.font.render("Gameplay", True, (255, 255, 255))

    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.title, (200, 200))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Constellation Drawer")

    clock = pygame.time.Clock()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    current_screen = "main_menu"
    main_menu = MainMenu()
    gameplay = Gameplay()

    while True:
        events = pygame.event.get()

        if current_screen == "main_menu":
            next_screen = main_menu.handle_events(events)
            if next_screen:
                current_screen = next_screen
        elif current_screen == "gameplay":
            next_screen = gameplay.handle_events(events)
            if next_screen:
                current_screen = next_screen

        if current_screen == "main_menu":
            main_menu.update()
            main_menu.draw(screen)
        elif current_screen == "gameplay":
            gameplay.update()
            gameplay.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
