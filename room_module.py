import pygame
import os
import config as c
import pictures_module


def get_pictures(era):
    pictures_list = []
    pictures_names_list = sorted(os.listdir("exposition" + "\\" + era))
    for picture in pictures_names_list:
        if picture.endswith(".jpg"):
            pictures_list.append(pictures_module.Picture(picture, era))

    return pictures_list


def room_loop(pictures_list):
    pressed = True
    current_picture_index = 0
    while pressed:
        current_picture = pictures_list[current_picture_index]
        c.screen.fill((0, 0, 0))
        current_picture.draw(c.screen)
        for i in pygame.event.get():
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE:
                    pressed = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    if current_picture_index > 0:
                        current_picture_index -= 1
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_RIGHT:
                    if current_picture_index < len(pictures_list)-1:
                        current_picture_index += 1


        c.clock.tick(c.FPS)
        pygame.display.update()