import pygame, sys
from button import Button

pygame.init()

SCREEN = pygame.display.set_mode((1191, 670))
pygame.display.set_caption("Menu")

BG = pygame.image.load("sky.jpeg")
logo = pygame.image.load("logo.png")

# Set the size for the image
DEFAULT_IMAGE_SIZE = (400, 400)
  
# Scale the image to your needed size
logo = pygame.transform.scale(logo, DEFAULT_IMAGE_SIZE)
  
# Set a default position
DEFAULT_IMAGE_POSITION = (20,-50)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black") # Change background

        PLAY_TEXT = get_font(45).render("PICK A GAME.", True, "White") 
        SCREEN.blit(PLAY_TEXT, (350,170))

        GAME_1 = Button(image=None, pos=(300, 460),text_input="GAME 1", font=get_font(30), base_color="White", hovering_color="#FFB90F")
        GAME_1.changeColor(PLAY_MOUSE_POS)
        GAME_1.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME_1.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()



def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))
        SCREEN.blit(logo, DEFAULT_IMAGE_POSITION)

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        #MENU_TEXT = get_font(50).render("MAIN MENU", True, "#b68f40")
        #MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        
        TITLE = get_font(73).render("MONEYSTORY", True, "goldenrod1")
        
        OPTIONS_BUTTON = Button(image = pygame.image.load("Options Rect.png"), pos=(640, 550), text_input="INSTRUCTIONS", font= get_font(45), base_color="White", hovering_color="#FFB90F")
        PLAY_BUTTON = Button(image = pygame.image.load("Play Rect.png"), pos =(640, 400), text_input="PLAY", font= get_font(50), base_color="White", hovering_color="#FFB90F")
        
        SCREEN.blit(TITLE, (400,170))
        #SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()

        pygame.display.update()

main_menu()







