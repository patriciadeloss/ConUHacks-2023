#**Went through pygame tutorial by Coding with Russ**

import pygame
import entity
import console_Tutorial


def sunny_display():

    #pygame.init()

    SCREEN_WIDTH = 900 #pixels
    SCREEN_HEIGHT = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('ProfileSpriteSheet')

    run = True
    doInfo = False
    doTut = False

    #initializing the image as a variable. Convert alpha is for pixels + transparency. 
    #Speeds up performance

    #Note: each sunny frame is 239 x 385 pixels
    #Note: each icon is 50 x 50 pixels
    sunnySize = (239, 385)
    iconSize = (50,50)
    textboxSize = (990, 228)
    arrowSize = (530, 287)

    sunny_profilesheet = pygame.image.load('graphics/sunny_spritesheet.png').convert_alpha()
    sunny_profile = entity.Entity(sunny_profilesheet)
    sunnyScale = 1.75
    sunnyRow = 0

    textbox_img = pygame.image.load('graphics/textbox.jpeg').convert_alpha()
    textbox_ent = entity.Entity(textbox_img)
    textboxScale = 0.75

    arrow_img = pygame.image.load('graphics/arrow.jpeg').convert_alpha()
    arrow_ent = entity.Entity(arrow_img)
    arrowScale = 1

    coin_img = pygame.image.load('graphics/coins_icon.jpeg').convert_alpha()
    coin_ent = entity.Entity(coin_img)
    coinScale = 0.75

    health_img = pygame.image.load('graphics/health_icon.jpeg').convert_alpha()
    health_ent = entity.Entity(health_img)
    healthScale = 0.75

    happy_img = pygame.image.load('graphics/happiness_icon.jpeg').convert_alpha()
    happy_ent = entity.Entity(happy_img)
    happyScale = 0.75

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
        sunny_animation.append(sunny_profile.get_image(i, sunnyRow, sunnySize[0], sunnySize[1], sunnyScale, BLACK))

    textbox = textbox_ent.get_image(0, 0, textboxSize[0], textboxSize[1], textboxScale, BLACK)

    coin_icon = coin_ent.get_image(0, 0, iconSize[0], iconSize[1], coinScale, BLACK)

    health_icon = health_ent.get_image(0, 0, iconSize[0], iconSize[1], healthScale, BLACK)

    happiness_icon = happy_ent.get_image(0, 0, iconSize[0], iconSize[1], happyScale, BLACK)



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

        #textbox
        screen.blit(textbox, (SCREEN_WIDTH/2 - (textboxSize[0]*textboxScale/2), SCREEN_HEIGHT - (textboxSize[1]*textboxScale) - 10))

        #health icon
        screen.blit(health_icon, (10, 10))

        #coin icon
        screen.blit(coin_icon, (10, iconSize[0]*coinScale + 15))

        #hunger icon
        screen.blit(happiness_icon, (10, iconSize[0]*happyScale*2 + 20))

    
        #flip to update display
        pygame.display.flip()

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   #If window is closed = stop 
                run = False

        pygame.display.update()             #Update the window display

        '''
        if doInfo == False:
            console_Tutorial.Info()
            doInfo = True
        elif doTut == False:
            console_Tutorial.Tutorial()
            doTut = True
        '''

    pygame.quit()

sunny_display()
