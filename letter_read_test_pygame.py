import pygame
successes, failures = pygame.init()
print("{0} successes and {1} failures".format(successes, failures))

screen = pygame.display.set_mode((720, 600))
clock = pygame.time.Clock()
FPS = 60
  # Frames per second.

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# RED = (255, 0, 0), GREEN = (0, 255, 0), BLUE = (0, 0, 255).  

cho = pygame.image.load(r'C:\Users\soarh\Desktop\circle.png')
joong = pygame.image.load(r'C:\Users\soarh\Desktop\jongjong.png')
jong = pygame.image.load(r'C:\Users\soarh\Desktop\jong.png')

chox = 200
choy = 200
joongx = 350
joongy = 180
jongx = 250
jongy = 320

pygame.display.set_caption('Dyslexia Training')
#display_surface = pygame.display.set_mode((100,150))
#display_surface.blit(cho,(40,50))

def chomove(x,y):
    screen.blit(cho,(x,y))
def joongmove(x,y):
    screen.blit(joong,(x,y))
def jongmove(x,y):
    screen.blit(jong,(x,y))


while True:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            screen.fill(WHITE)
            if event.key == pygame.K_a:
                chox-=2
                choy-=2
                joongx+=2
                jongy+=2
                chomove(chox,choy)
                joongmove(joongx,joongy)
                jongmove(jongx,jongy)
            elif event.key == pygame.K_d:
                chox+=2
                choy+=2
                joongx-=2
                jongy-=2
                chomove(chox,choy)
                joongmove(joongx,joongy)
                jongmove(jongx,jongy)
    pygame.display.update()  
