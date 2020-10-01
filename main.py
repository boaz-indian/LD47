from Engine import *
import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("caption")

clock = pygame.time.Clock()
BackGround = Background('hadarHashuh.png', [0,0])

crashed = False



while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    screen.fill([255, 255, 255])
    pygame.draw.rect(screen, (0, 0, 255), (200,150,130,50))
    # print(pygame.mouse.get_pos())
    # if Collision(pygame.mouse.get_pos(), [[200, 150], [350, 150], [300, 200], [200, 200]]).is_true():
    #     print("True")
    CreatePolygon(screen, (0, 0, 255), [[30,90],[90, 80], [80, 40], [30,40]]).draw()
    print(Button( [[30,90],[90, 80], [80, 40], [30,40]]).onClick())
    # Collision(pygame.mouse.get_pos(), [[30,90],[90, 80], [80, 40], [30,40]]).polygon()
    # screen.blit(BackGround.image, BackGround.rect)


    pygame.display.update()
    clock.tick(60)