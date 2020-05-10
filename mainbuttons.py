import pygame
import room_module
import image_resize
import os


class Button:
    def __init__(self, scale_factor, x, y, image_path, text):
        self.scale_factor = scale_factor
        self.x = x
        self.y = y
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        if scale_factor < 1:
            image_resize.scale_image(self.image_path, self.image_path[:-4] + "scaled.jpg",
                                     self.rect.width * scale_factor)
            self.image = pygame.image.load(self.image_path[:-4] + "scaled.jpg")
            self.rect = self.image.get_rect()
            os.remove(self.image_path[:-4] + "scaled.jpg")
        self.rect.left = self.x
        self.rect.top = self.y
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.text = text
        self.color = (255, 255, 255)
        self.button_text = self.font.render(text, True, self.color, (0, 0, 0))
        self.text_rect = self.button_text.get_rect()
        self.text_rect.center = (self.rect.centerx, self.rect.bottom + 15)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.button_text, self.text_rect)


class ExitButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text="", image_path="covers\\exit.jpg")

    def clicked(self):
        exit()


class AntiquityButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text=" Antiquity ", image_path="covers\\antiquity.jpg")

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Antiquity"))


class MiddleAgesButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text=" Middle ages ", image_path="covers\\middle ages.jpg")

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Middle ages"))


class RenaissanceButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text=" Renaissance ", image_path="covers\\Renaissance.jpg")

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Renaissance"))


class RealismButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text=" Classical art ", image_path="covers\\Realism.jpg")

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Classicism, romanticism, realism"))


class ModernismButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text=" Modernism ", image_path="covers\\Modernism.jpg")

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Modernism"))


class ContemporaryArtButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text=" Contemporary art ", image_path="covers\\Contemporary art.jpg")

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Contemporary art"))


class OrientalArtButton(Button):
    def __init__(self, scale_factor, x, y):
        Button.__init__(self, scale_factor, x, y, text=" Oriental art ", image_path="covers\\Oriental art.jpg")

    def clicked(self):
        room_module.room_loop(room_module.get_pictures("Oriental art"))
