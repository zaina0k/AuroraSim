import pygame # type: ignore
from pygame.locals import * # type: ignore
import sys
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

Ursa_Major_answers = [[116,98],[53,238],[334,150],[344,301],[462,472],[577,634],[738,672]]

###

BLACK = (0, 0, 0)
WHITE = (255,255,255)
Col = (255,255,0)
BLUE = (0,0,255)
# Main loop
status = True
seconds = 4
###

# imp = pygame.image.load(list_images[0]).convert()
# background = pygame.image.load('empty_background.png').convert()


class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 72)
        self.title = self.title_font.render("Constellation Game", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        self.text = self.font.render("For idiot kids", True, (255, 255, 255))
        self.text_rect = self.text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 75))
        self.button = self.font.render("Start", True, (255, 255, 255))
        self.button_color = (50, 200, 50)  # RGB color for the button
        self.button_rect = pygame.Rect(600,600,100,50)
        self.button_text_rect = self.button.get_rect(center=self.button_rect.center)
        self.background = pygame.image.load("empty_background.png")

    def handle_events(self, events):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    return "reference"

    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))
        screen.blit(self.title, self.title_rect.topleft)
        screen.blit(self.text, self.text_rect.topleft)
        pygame.draw.rect(screen, self.button_color, self.button_rect)  # Draw the button
        screen.blit(self.button, self.button_text_rect)
    
class Reference:
    def __init__(self):
        self.list_ref_images = ['Ursa_Major.png', 'Orion.png', 'Cassiopeia.png', 'Pegasus.png', 'Sirius.png']
        self.index = 0
        self.background = pygame.image.load(self.list_ref_images[0])
        self.font = pygame.font.Font(None, 75)

    def update(self):
        pass    
    
    def countdown(self,seconds,screen):
        while int(seconds) >0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.background = pygame.image.load(self.list_ref_images[self.index])
            screen.blit(self.background, (0, 0))
            text_color = Col if seconds <= 15 else BLACK
            self.text = self.font.render(str(seconds), True, text_color)
            self.text_rect = self.text.get_rect(center=(700, 100))
            screen.blit(self.text, self.text_rect)
            pygame.display.flip()
            time.sleep(1)
            seconds -= 1
        return "gameplay"


    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))

class Gameplay:
    def __init__(self):
        self.list_base_images = ['Ursa_Major_no_lines.png', 'Orion_no_lines.png', 'Cassiopeia_no_lines.png', 'Pegasus_no_lines.png', 'Sirius_no_lines.png']
        self.line_started = False
        self.index = 0
        self.background = pygame.image.load(self.list_base_images[self.index])
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 72)
        self.title = self.title_font.render("Connect the stars", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 8))
        self.line_list = []

    def handle_events(self, events,screen):
        for event in events:
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                # Check if the mouse click is within 10 pixels of a point in Ursa_Major_answers
                for point in Ursa_Major_answers:
                    if abs(event.pos[0] - point[0]) <= 10 and abs(event.pos[1] - point[1]) <= 10:
                        print("Correct!")
                        if not self.line_started:
                            # Start a new line
                            self.line_started = True
                            self.start_point = event.pos
                        else:
                            # Draw the line
                            self.line_list.append([self.start_point, event.pos])
                            # self.line_list.append(pygame.line(screen, WHITE, self.start_point, event.pos, 1))

                            self.line_started = False


    def update(self):
        pass

    def draw(self, screen):
        screen.fill((0, 0, 0))
        screen.blit(self.background, (0, 0))
        screen.blit(self.title, (200, 200))
        for i in range(len(self.line_list)):
            pygame.draw.line(screen, WHITE, self.line_list[i][0], self.line_list[i][1], 2)  


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
    reference = Reference()

    while True:
        events = pygame.event.get()

        if current_screen == "main_menu":
            next_screen = main_menu.handle_events(events)
            if next_screen:
                current_screen = next_screen
        elif current_screen == "reference":
            next_screen = reference.countdown(15,screen)
            if next_screen:
                current_screen = next_screen
        elif current_screen == "gameplay":
            next_screen = gameplay.handle_events(events,screen)
            if next_screen:
                current_screen = next_screen

        if current_screen == "main_menu":
            main_menu.update()
            main_menu.draw(screen)
        elif current_screen == "reference":
            reference.update()
            reference.draw(screen,)
        elif current_screen == "gameplay":
            gameplay.update()
            gameplay.draw(screen)

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
