#**Went through pygame tutorial by Coding with Russ**

import pygame
import entity

pygame.init()

SCREEN_WIDTH = 900 #pixels
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('ProfileSpriteSheet')

run = True

#initializing the image as a variable. Convert alpha is for pixels + transparency. 
#Speeds up performance

#Note: each sunny frame is 239 x 385 pixels
#Note: each icon is 50 x 50 pixels
sunnySize = (239, 385)
iconSize = (50,50)
textboxSize = (990, 228)

sunny_profilesheet = pygame.image.load('graphics/sunny_spritesheet.png').convert_alpha()
sunny_profile = entity.Entity(sunny_profilesheet)
sunnyScale = 1.5

textbox_img = pygame.image.load('graphics/textbox.jpeg').convert_alpha()
textbox_ent = entity.Entity(textbox_img)
textboxScale = 0.75


coin_icon = pygame.image.load('graphics/coins_icon.jpeg').convert_alpha()

WHITE = (255, 255, 255)
BLACK = pygame.Color(0,0,0)

bg_color = (WHITE) #background color fill

#create animation list
sunny_animation = []
sunny_frames = 4

#timer
last_update = pygame.time.get_ticks()
animation_delay = 250 #milliseconds

frame = 0

for i in range(sunny_frames):
    sunny_animation.append(sunny_profile.get_image(i, 0, sunnySize[0], sunnySize[1], sunnyScale, BLACK))

textbox = textbox_ent.get_image(0, 0, textboxSize[0], textboxSize[1], textboxScale, BLACK)



while run:
    
    #update background
    screen.fill(bg_color) 


    #update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_delay:
        if frame < sunny_frames-1:
            frame += 1
            last_update = current_time
        else:
            frame = 0
            last_update = current_time


    #display image over background
    #[windowname].blit(image, [x, y] on window (top left corner))
    screen.blit(sunny_animation[frame], (SCREEN_WIDTH/2 - (sunnySize[0]*sunnyScale/2), SCREEN_HEIGHT/2 - (sunnySize[1]*sunnyScale/2)))

    screen.blit(textbox, (SCREEN_WIDTH/2 - (textboxSize[0]*textboxScale/2), SCREEN_HEIGHT - (textboxSize[1]*textboxScale) - 10))

    

    #flip to update display
    pygame.display.flip()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   #If window is closed = stop 
            run = False

    pygame.display.update()             #Update the window display


pygame.quit()
