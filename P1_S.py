import pygame

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((600,300))

b1 = pygame.Rect(100,100,50,50)
w1 = pygame.Rect(100,150,50,50)

b2 = pygame.Rect(150,150,50,50)
w2 = pygame.Rect(150,100,50,50)

b3 = pygame.Rect(200,100,50,50)
w3 = pygame.Rect(200,150,50,50)

b4 = pygame.Rect(250,150,50,50)
w4 = pygame.Rect(250,100,50,50)

b5 = pygame.Rect(300,100,50,50)
w5 = pygame.Rect(300,150,50,50)

b6 = pygame.Rect(350,150,50,50)
w6 = pygame.Rect(350,100,50,50)

b7 = pygame.Rect(400,100,50,50)
w7 = pygame.Rect(400,150,50,50)

b8 = pygame.Rect(450,150,50,50)
w8 = pygame.Rect(450,100,50,50)

while True:    
    screen.fill((150,75,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(screen,(0,0,0),b1)
    pygame.draw.rect(screen,(255,255,255),w1)
    
    pygame.draw.rect(screen,(0,0,0),b2)
    pygame.draw.rect(screen,(255,255,255),w2)
    
    pygame.draw.rect(screen,(0,0,0),b3)
    pygame.draw.rect(screen,(255,255,255),w3)
    
    pygame.draw.rect(screen,(0,0,0),b4)
    pygame.draw.rect(screen,(255,255,255),w4)
    
    pygame.draw.rect(screen,(0,0,0),b5)
    pygame.draw.rect(screen,(255,255,255),w5)
    
    pygame.draw.rect(screen,(0,0,0),b6)
    pygame.draw.rect(screen,(255,255,255),w6)
    
    pygame.draw.rect(screen,(0,0,0),b7)
    pygame.draw.rect(screen,(255,255,255),w7)
    
    pygame.draw.rect(screen,(0,0,0),b8)
    pygame.draw.rect(screen,(255,255,255),w8)
    
    pygame.display.update()