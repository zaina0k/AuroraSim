import pygame
import time


pygame.init()


scrn = pygame.display.set_mode((750, 750))


pygame.display.set_caption('Image')


imp = pygame.image.load("big-dipper.jpg").convert()
imp_2 = pygame.image.load("stock.jpg").convert()

# Fonts and colors
font = pygame.font.Font(None, 64)
BLACK = (0, 0, 0)
Col = (255,255,0)

# Main loop
status = True
seconds = 10

def countdown(seconds):
    while seconds > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        scrn.blit(imp, (0, 0))
        text_color = Col if seconds <= 10 else BLACK
        text = font.render(str(seconds), True, text_color)
        text_rect = text.get_rect(center=(200, 200))
        scrn.blit(text, text_rect)
        pygame.display.flip()
        time.sleep(1)
        seconds -= 1
    scrn.blit(imp_2, (0,0))
    scrn.fill(BLACK)
    
    pygame.display.flip()
    

countdown(seconds)
