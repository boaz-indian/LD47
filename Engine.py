import pygame, os
import keyboard
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


class Background(pygame.sprite.Sprite):
    # This class create a background
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class CreatePolygon:
    # this class create a polygons
    def __init__(self, screen, color, points, width=0):
        self.screen, self.color, self.points, self.width = screen, color, points, width

    def draw(self):
        pygame.draw.polygon(self.screen, self.color, self.points, self.width)


class CreateImage:
    # This class create a image
    def __init__(self, screen, path, cord):
        self.path, self.cord, self.screen = path, cord, screen
        self.image = pygame.image.load(os.path.join(self.path))

    def draw(self):
        self.screen.blit(self.image, self.cord)

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))


class Button:
    # This class is to make a rect button
    # points = [[upperleftx, upperlefty],  [lowerrightx, lowerrighty]] tip the first point is the first two
    # digit you entered the rect and the second you should test
    def __init__(self, points):
        self.points = points

    def onClick(self):
        x, y = pygame.mouse.get_pos()
        # print(x, y)
        # self.points[0][0] < x < self.points[1][0] and self.points[0][1] < y < self.points[1][1]
        # print(pygame.mouse.get_pressed()[0])
        if pygame.mouse.get_pressed()[0] and Collision(pygame.mouse.get_pos(), self.points).polygon():
            return True
        else:
            return False

    def onHover(self):
        x, y = pygame.mouse.get_pos()
        # self.points[0][0] < x < self.points[1][0] and self.points[0][1] < y < self.points[1][1]
        if Collision(pygame.mouse.get_pos(), self.points).polygon():
            return True
        else:
            return False


class Text:
    def __init__(self, screen, text, cord, size, color,  font='freesansbold.ttf'):
        self.screen, self.text, self.cord, self.size, self.font, self.color = screen, text, cord, size, font, color
        self.font = pygame.font.Font(self.font, self.size)
        self.text = self.font.render(self.text, False, self.color)
        self.textRect = self.text.get_rect()
        self.textRect.center = (self.cord[0] // 2, self.cord[1] // 2)

    def draw(self):
        self.screen.blit(self.text, self.textRect)


class Sound:
    def __init__(self, path):
        self.sound = pygame.mixer.Sound(path)

    def play(self):
        self.sound.play()

    def playOnRepeat(self):
        self.sound.play(-1)

    def stop(self):
        self.sound.stop()

    def stopAll(self):
        pygame.mixer.music.stop()

    def pauseAll(self):
        pygame.mixer.music.pause()

    def resumeAll(self):
        pygame.mixer.music.unpause()


class KeyBoard:
    @staticmethod
    def getHotKey():
        return keyboard.get_hotkey_name()

    @staticmethod
    def isPressed(key):
        return keyboard.is_pressed(key)


class Collision:
    def __init__(self, cords1, cords2): # 1 is x, y and 2 is (x, y) * 4 for a rect
        self.cords1, self.cords2 = cords1, cords2

    def is_true(self):
        x, y = self.cords1
        if self.cords2[0][0] < x < self.cords2[1][0] and self.cords2[0][1] < y < self.cords2[3][1]:
            print("true")

    def polygon(self):
        point = Point(self.cords1)
        polygon = Polygon(self.cords2)
        return polygon.contains(point)

