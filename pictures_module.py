import pygame
import image_resize
import os
import config as c


class Picture:
    def __init__(self, name, era):
        self.name = name
        self.era = era
        self.path = "exposition" + "\\" + era + "\\" + name
        self.image = pygame.image.load(self.path)
        self.rect = self.image.get_rect()
        self.deafultfontsize = 30
        self.fontsize = self.deafultfontsize
        self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)
        self.text_color = self.color = (100, 100, 100)
        if self.rect.right > c.screen_width * 0.75 - 20:
            image_resize.scale_image(self.path, self.path[:-4] + " scaled.jpg", c.screen_width * 0.75 - 20)
            self.image = pygame.image.load(self.path[:-4] + " scaled.jpg")
            self.rect = self.image.get_rect()
            os.remove(self.path[:-4] + " scaled.jpg")
        self.rect.center = (c.screen_width * 0.75 // 2, c.screen_height // 2)
        if self.rect.bottom + self.fontsize * 4 > c.screen_height:
            image_resize.scale_image(self.path, self.path[:-4] + " scaled.jpg", None, c.screen_height - self.fontsize * 4)
            self.image = pygame.image.load(self.path[:-4] + " scaled.jpg")
            self.rect = self.image.get_rect()
            os.remove(self.path[:-4] + " scaled.jpg")
        self.rect.center = (c.screen_width * 0.75 // 2, c.screen_height // 2)

        self.resize_name()
        self.name_text = self.font.render(self.name[3:-4], True, self.text_color)
        self.name_text_rect = self.name_text.get_rect()
        self.name_text_rect.center = (self.rect.centerx, self.rect.bottom + self.fontsize)

        self.discription_file = open(self.path[:-4] + ".txt", "r")
        self.discription = self.discription_file.read()
        try:
            self.fontsize = self.deafultfontsize
            self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)
            self.strings = self.split_discription_to_strings()
        except:
            self.strings = []
        self.text = []
        for string in self.strings:
            self.text.append(self.font.render(string, True, self.text_color))

    def resize_name(self):
        while self.font.size(self.name)[0] > c.screen_width * 0.75:
            self.fontsize -= 1
            self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)

    def split_discription_to_strings(self):
        words = self.discription.split()
        strings = [words[0]]
        del words[0]
        index = 0
        while words:
            if self.font.size(strings[index] + " " + words[0])[0] < c.screen_width * 0.25:
                strings[index] = strings[index] + " " + words[0]
                del words[0]
            else:
                strings.append(words[0])
                del words[0]
                index += 1

        if len(strings) * self.fontsize > c.screen_height:
            self.fontsize -= 1
            self.font = pygame.font.Font('freesansbold.ttf', self.fontsize)
            strings = self.split_discription_to_strings()

        return strings

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.name_text, self.name_text_rect)
        surface.blit(c.text_alfa, (c.screen_width * 0.75, 0, c.screen_width * 0.25, c.screen_height))
        for number, string in enumerate(self.text):
            surface.blit(string, (c.screen_width * 0.75, number * self.fontsize, c.screen_width * 0.25, c.screen_height))


