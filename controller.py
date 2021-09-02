import pygame,sys

class Controller:
    def __init__(self,view, model):
        self.view= view
        self.model = model
        pygame.init()

    def updateController(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
