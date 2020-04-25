import pygame
import room_module


class Button:
    def __init__(self, rect, image, text):
        self.rect = pygame.Rect(rect)
        self.image = image
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = text
        self.color = (0, 0, 0)
        self.button_text = self.font.render(text, True, self.color)
        self.text_rect = self.button_text.get_rect()
        self.text_rect.center = (self.rect.centerx, self.rect.bottom + 15)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.button_text, self.text_rect)


class ExitButton(Button):
    def __init__(self, rect):
        Button.__init__(self, rect, text="", image=pygame.image.load("exit.jpg"))

    def clicked(self):
        exit()


class AntiquityButton(Button):
    def __init__(self, rect):
        Button.__init__(self, rect, text="Antiquity", image=pygame.image.load("antiquity.jpg"))

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("antiquity"))


class MiddleAgesButton(Button):
    def __init__(self, rect):
        Button.__init__(self, rect, text="Middle ages", image=pygame.image.load("middle ages.jpg"))

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Middle ages"))

