import pygame
import time
import sys



#############################################

pygame.init()

scrn = pygame.display.set_mode((800, 800))
constellation_points = []
pygame.display.set_caption('Image')
check_coordinates = [100,100,100,50]
list_images = ['Ursa_Major.png']
imp = pygame.image.load(list_images[0]).convert()
background = pygame.image.load('empty_background.png').convert()


# Fonts and colors
font = pygame.font.Font(None, 64)
BLACK = (0, 0, 0)
WHITE = (255,255,255)
Col = (255,255,0)
BLUE = (0,0,255)
# Main loop
status = True
seconds = 4

def draw_constellation():
      # Fill the screen with black
    button=pygame.draw.rect(scrn,BLUE,check_coordinates)
    text = font.render('Check awnswer', True, WHITE)
    text_rect = text.get_rect(center=(50, 50))
    # Draw the lines connecting the constellation points
    if len(constellation_points) > 1:
        for i in range(len(constellation_points) - 1):
            pygame.draw.line(scrn, WHITE, constellation_points[i], constellation_points[i + 1], 2)

    # Draw the constellation points
    for point in constellation_points:
        pygame.draw.circle(scrn, WHITE, point, 5)
    mouse_x, mouse_y = pygame.mouse.get_pos()

    
    if button.collidepoint(mouse_x, mouse_y):
        next_pic=True
        return next_pic
    if next_pic==True:
      print('cool')

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
                print(constellation_points)
    pygame.display.flip()  # Update the display
         
    pygame.quit()
    sys.exit()

Col = (255,255,0)


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
    scrn.blit(background, (0, 0))
    pygame.display.flip()
    main()
    pygame.display.flip()
    

countdown(seconds)
