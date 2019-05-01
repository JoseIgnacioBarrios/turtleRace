import pygame , sys

class Game():
    runners=[]
    __starLine=28
    __finishLine=620
    
    def __init__(self):
        self.__screen= pygame.display.set_mode((640,480))
        self.__background=pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera bichos")
    
    def competir(self):
        gameOver=False
        while not gameOver:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameOver=True
            self.__screen.clit(self.__background,(0,0))
            pygame.display.flip()
        
        pygame.QUIT()
        sys.exit()
    
if __name__='__main__':
    game=Game()
    pygame.fot.init()
    game.competir()