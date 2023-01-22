import pygame




class Entity():
    def __init__(self, image):
        self.sheet = image

    #function to create surfaces for rendering an image based on given dimensions
    #sheet = sprite sheet, width = surface width
    #height = surf height, scale = image scale
    #frame = current frame, row = which row on sprite sheet
    def get_image(self, frame, row, width, height, scale, color):

        #creates a surface based on the width and height specified
        #SRCALPHA = per-pixel alpha
        image = pygame.Surface((width, height), pygame.SRCALPHA)

        #blit image onto created surface
        #image.blit(sheet, (where on window), (start x,y on sheet, ending x,y on sheet))
        image.blit(self.sheet, (0,0), [(frame * width), (row * height), width, height])

        #Scale image
        image = pygame.transform.scale(image, (width * scale, height * scale))

        #transparency
        image.set_colorkey(color)

        return image


"""
class Entity:
    def __init__ (self, frame, sheet, img_size, ent_size, scale):
        self.frame = frame
        self.sheet = sheet
        self.img_size = img_size
        self.ent_size = ent_size
        self.scale = scale

        #[0] = x, [1] = y, [2] = w, [3] = h
        self.currentFrame = [0, 0, ent_size[0], ent_size[1]]

    def __init__ (self, sheet, img_size, ent_size, scale):
        self.frame = 0
        self.sheet = sheet
        self.img_size = img_size
        self.ent_size = ent_size
        self.scale = scale

        #[0] = x, [1] = y, [2] = w, [3] = h
        self.currentFrame = [0, 0, ent_size[0], ent_size[1]]

    def changeFrame(numberFrames, row):
        if (currentFrame[0] < (ent_size[0] * (numberFrames - 1))):
            currentFrame[0] += ent_size[0] 
        else:
            currentFrame[0] = 0
"""





    
