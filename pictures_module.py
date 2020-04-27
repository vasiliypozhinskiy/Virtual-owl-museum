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
        self.font_size = self.deafultfontsize
        self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
        self.text_color = self.color = (100, 100, 100)
        if self.rect.height + self.font_size * 4 > c.screen_height:
            image_resize.scale_image(self.path, self.path[:-4] + " scaled.jpg", None,
                                     c.screen_height - self.font_size * 4)
            self.image = pygame.image.load(self.path[:-4] + " scaled.jpg")
            self.rect = self.image.get_rect()
            os.remove(self.path[:-4] + " scaled.jpg")
        if self.rect.width > c.screen_width * 0.75 - 20:
            image_resize.scale_image(self.path, self.path[:-4] + " scaled.jpg", c.screen_width * 0.75 - 20)
            self.image = pygame.image.load(self.path[:-4] + " scaled.jpg")
            self.rect = self.image.get_rect()
            os.remove(self.path[:-4] + " scaled.jpg")
        self.rect.center = (c.screen_width * 0.75 // 2, c.screen_height // 2)

        self.resize_name()
        self.name_text = self.font.render(self.name[4:-4], True, self.text_color)
        self.name_text_rect = self.name_text.get_rect()
        self.name_text_rect.center = (self.rect.centerx, self.rect.bottom + self.font_size)
        try:
            self.description_file = open(self.path[:-4] + ".txt")
            self.description = self.description_file.read()
            self.description_file.close()
        except FileNotFoundError:
            self.description_file = open(self.path[:-4] + ".txt", "w")
            self.description_file.close()
            self.description_file = open(self.path[:-4] + ".txt", "r")
            self.description = self.description_file.read()
            self.description_file.close()
        try:
            self.font_size = self.deafultfontsize
            self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
            self.strings = self.split_discription_to_strings()
        # description file is empty
        except IndexError:
            self.strings = []
        self.text = []
        for string in self.strings:
            self.text.append(self.font.render(string, True, self.text_color))

    def resize_name(self):
        while self.font.size(self.name)[0] > c.screen_width * 0.75:
            self.font_size -= 1
            self.font = pygame.font.Font('freesansbold.ttf', self.font_size)

    def split_discription_to_strings(self):
        words = self.description.split()
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

        if len(strings) * self.font_size > c.screen_height:
            self.font_size -= 1
            self.font = pygame.font.Font('freesansbold.ttf', self.font_size)
            strings = self.split_discription_to_strings()

        return strings

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        surface.blit(self.name_text, self.name_text_rect)
        surface.blit(c.text_alfa, (c.screen_width * 0.75, 0, c.screen_width * 0.25, c.screen_height))
        for number, string in enumerate(self.text):
            surface.blit(string, (c.screen_width * 0.75, number * self.font_size,
                                  c.screen_width * 0.25, c.screen_height))
